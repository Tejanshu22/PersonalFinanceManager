CREATE SCHEMA ledger;
REVOKE ALL ON SCHEMA ledger FROM PUBLIC;
CREATE TABLE ledger.ledger_owner (
 id uuid PRIMARY KEY, created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
 write_version bigint NOT NULL DEFAULT 0
);
CREATE TABLE ledger.financial_account (
 id uuid PRIMARY KEY, owner_id uuid NOT NULL REFERENCES ledger.ledger_owner(id),
 kind text NOT NULL CHECK(kind IN ('bank','cash','credit_card')),
 currency text NOT NULL CHECK(currency='INR'),
 label text NOT NULL CHECK(length(label) BETWEEN 1 AND 100),
 created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
 UNIQUE(owner_id,id)
);
CREATE TABLE ledger.ledger_source (
 id uuid PRIMARY KEY, owner_id uuid NOT NULL, account_id uuid NOT NULL,
 source_key text NOT NULL CHECK(length(source_key) BETWEEN 1 AND 128),
 format text NOT NULL CHECK(length(format) BETWEEN 1 AND 40),
 parser_version text NOT NULL CHECK(length(parser_version) BETWEEN 1 AND 40),
 period_start date NOT NULL CHECK(isfinite(period_start)),
 period_end date NOT NULL CHECK(isfinite(period_end) AND period_end >= period_start),
 created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
 FOREIGN KEY(owner_id,account_id) REFERENCES ledger.financial_account(owner_id,id),
 UNIQUE(owner_id,account_id,source_key), UNIQUE(owner_id,account_id,id)
);
CREATE TABLE ledger.source_row (
 id uuid PRIMARY KEY, owner_id uuid NOT NULL, account_id uuid NOT NULL, source_id uuid NOT NULL,
 row_key text NOT NULL CHECK(length(row_key) BETWEEN 1 AND 128),
 original_amount_text text NOT NULL CHECK(length(original_amount_text)<=80),
 original_direction_text text NOT NULL CHECK(length(original_direction_text)<=40),
 original_posted_date_text text NOT NULL CHECK(length(original_posted_date_text)<=80),
 original_transaction_date_text text CHECK(length(original_transaction_date_text)<=80),
 original_value_date_text text CHECK(length(original_value_date_text)<=80),
 original_description text CHECK(length(original_description)<=500),
 created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
 FOREIGN KEY(owner_id,account_id,source_id) REFERENCES ledger.ledger_source(owner_id,account_id,id),
 UNIQUE(owner_id,source_id,row_key), UNIQUE(owner_id,account_id,id)
);
CREATE TABLE ledger.canonical_transaction (
 id uuid PRIMARY KEY, owner_id uuid NOT NULL, account_id uuid NOT NULL, source_row_id uuid NOT NULL,
 amount numeric NOT NULL CHECK(amount>0 AND amount<1000000000000000000 AND amount=trunc(amount,2)),
 direction text NOT NULL CHECK(direction IN ('debit','credit')),
 currency text NOT NULL CHECK(currency='INR'),
 posted_date date NOT NULL CHECK(isfinite(posted_date)),
 transaction_date date CHECK(isfinite(transaction_date)), value_date date CHECK(isfinite(value_date)),
 created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
 FOREIGN KEY(owner_id,account_id) REFERENCES ledger.financial_account(owner_id,id),
 FOREIGN KEY(owner_id,account_id,source_row_id) REFERENCES ledger.source_row(owner_id,account_id,id),
 UNIQUE(owner_id,source_row_id), UNIQUE(owner_id,id)
);
CREATE INDEX transaction_period ON ledger.canonical_transaction(owner_id,posted_date,id);
CREATE INDEX transaction_account_period ON ledger.canonical_transaction(owner_id,account_id,posted_date,id);
CREATE TABLE ledger.classification_event (
 id uuid PRIMARY KEY, owner_id uuid NOT NULL, transaction_id uuid NOT NULL,
 revision integer NOT NULL CHECK(revision>=0),
 category text NOT NULL CHECK(category IN ('unknown','income','consumption','internal_transfer','card_repayment','investment','refund','reversal')),
 review_status text NOT NULL CHECK(review_status IN ('needs_review','confirmed')),
 actor_kind text NOT NULL CHECK(actor_kind IN ('synthetic_owner','system')),
 actor_owner_id uuid,
 previous_event_id uuid, undo_of_event_id uuid,
 reason text CHECK(length(reason)<=300), created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
 CHECK((actor_kind='system' AND actor_owner_id IS NULL) OR
       (actor_kind='synthetic_owner' AND actor_owner_id IS NOT NULL AND actor_owner_id=owner_id)),
 CHECK(category!='unknown' OR review_status='needs_review'),
 FOREIGN KEY(owner_id,transaction_id) REFERENCES ledger.canonical_transaction(owner_id,id),
 UNIQUE(owner_id,transaction_id,revision), UNIQUE(owner_id,transaction_id,id),
 FOREIGN KEY(owner_id,transaction_id,previous_event_id) REFERENCES ledger.classification_event(owner_id,transaction_id,id),
 FOREIGN KEY(owner_id,transaction_id,undo_of_event_id) REFERENCES ledger.classification_event(owner_id,transaction_id,id)
);
CREATE TABLE ledger.transaction_link (
 id uuid PRIMARY KEY, owner_id uuid NOT NULL, from_transaction_id uuid NOT NULL, to_transaction_id uuid NOT NULL,
 kind text NOT NULL CHECK(kind IN ('transfer','repayment','refund','reversal')),
 actor_owner_id uuid NOT NULL CHECK(actor_owner_id=owner_id),
 reason text NOT NULL CHECK(length(reason) BETWEEN 1 AND 300),
 created_at timestamptz NOT NULL DEFAULT clock_timestamp(),
 revoked_at timestamptz, revocation_actor_owner_id uuid, revocation_reason text,
 CHECK(from_transaction_id!=to_transaction_id),
 CHECK((revoked_at IS NULL AND revocation_actor_owner_id IS NULL AND revocation_reason IS NULL) OR
       (revoked_at IS NOT NULL AND revocation_actor_owner_id IS NOT NULL AND revocation_actor_owner_id=owner_id
        AND revocation_reason IS NOT NULL AND length(revocation_reason) BETWEEN 1 AND 300 AND revoked_at>=created_at)),
 FOREIGN KEY(owner_id,from_transaction_id) REFERENCES ledger.canonical_transaction(owner_id,id),
 FOREIGN KEY(owner_id,to_transaction_id) REFERENCES ledger.canonical_transaction(owner_id,id)
);
CREATE UNIQUE INDEX link_pair ON ledger.transaction_link(owner_id,from_transaction_id,to_transaction_id) WHERE revoked_at IS NULL;
CREATE INDEX link_from ON ledger.transaction_link(owner_id,from_transaction_id);
CREATE INDEX link_to ON ledger.transaction_link(owner_id,to_transaction_id);
CREATE TABLE ledger.account_coverage (
 id uuid PRIMARY KEY, owner_id uuid NOT NULL, account_id uuid NOT NULL,
 period_start date NOT NULL CHECK(isfinite(period_start)),
 period_end date NOT NULL CHECK(isfinite(period_end) AND period_end>=period_start),
 status text NOT NULL CHECK(status IN ('unknown','partial','complete')),
 reconciliation_status text NOT NULL CHECK(reconciliation_status IN ('unavailable','failed','passed')),
 reason_codes text[] NOT NULL DEFAULT '{}', updated_at timestamptz NOT NULL DEFAULT clock_timestamp(),
 FOREIGN KEY(owner_id,account_id) REFERENCES ledger.financial_account(owner_id,id),
 UNIQUE(owner_id,account_id,period_start,period_end)
);

CREATE FUNCTION ledger.immutable() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN RAISE EXCEPTION 'immutable_ledger_record' USING ERRCODE='23514'; END $$;
CREATE FUNCTION ledger.lock_owner() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
 -- A real version update serializes writes per owner. At stronger isolation a stale
 -- writer receives a serialization failure rather than validating a stale snapshot.
 UPDATE ledger.ledger_owner SET write_version=write_version+1 WHERE id=NEW.owner_id;
 IF NOT FOUND THEN RAISE EXCEPTION 'owner_unavailable' USING ERRCODE='23503'; END IF;
 RETURN NEW;
END $$;
DO $$ DECLARE t text; BEGIN
 FOREACH t IN ARRAY ARRAY['financial_account','ledger_source','source_row','canonical_transaction','classification_event'] LOOP
  EXECUTE format('CREATE TRIGGER immutable_record BEFORE UPDATE OR DELETE ON ledger.%I FOR EACH ROW EXECUTE FUNCTION ledger.immutable()',t);
 END LOOP;
 FOREACH t IN ARRAY ARRAY['financial_account','ledger_source','source_row','canonical_transaction','classification_event','transaction_link','account_coverage'] LOOP
  EXECUTE format('CREATE TRIGGER a_owner_lock BEFORE INSERT ON ledger.%I FOR EACH ROW EXECUTE FUNCTION ledger.lock_owner()',t);
 END LOOP;
END $$;

CREATE FUNCTION ledger.check_classification() RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE tx record; prior record; target record; restored record;
BEGIN
 SELECT t.*,a.kind INTO tx FROM ledger.canonical_transaction t JOIN ledger.financial_account a
 ON (a.owner_id,a.id)=(t.owner_id,t.account_id) WHERE t.owner_id=NEW.owner_id AND t.id=NEW.transaction_id;
 IF NOT FOUND THEN RAISE EXCEPTION 'transaction_unavailable' USING ERRCODE='23503'; END IF;
 SELECT * INTO prior FROM ledger.classification_event WHERE owner_id=NEW.owner_id AND transaction_id=NEW.transaction_id ORDER BY revision DESC LIMIT 1;
 IF NOT FOUND THEN
  IF NEW.revision!=0 OR NEW.category!='unknown' OR NEW.review_status!='needs_review'
    OR NEW.previous_event_id IS NOT NULL OR NEW.undo_of_event_id IS NOT NULL OR NEW.actor_kind!='system' THEN
   RAISE EXCEPTION 'invalid_initial_classification' USING ERRCODE='23514'; END IF;
 ELSE
  IF NEW.revision!=prior.revision+1 OR NEW.previous_event_id IS DISTINCT FROM prior.id OR NEW.actor_kind!='synthetic_owner' THEN
   RAISE EXCEPTION 'stale_correction' USING ERRCODE='23514'; END IF;
 END IF;
 IF (NEW.category='income' AND (tx.direction!='credit' OR tx.kind='credit_card'))
 OR (NEW.category IN ('consumption','investment') AND tx.direction!='debit')
 OR (NEW.category='internal_transfer' AND tx.kind='credit_card')
 OR (NEW.category='card_repayment' AND NOT ((tx.kind='credit_card' AND tx.direction='credit') OR (tx.kind IN ('bank','cash') AND tx.direction='debit')))
 OR (NEW.category IN ('refund','reversal') AND tx.direction!='credit') THEN
  RAISE EXCEPTION 'incompatible_classification' USING ERRCODE='23514'; END IF;
 IF NEW.undo_of_event_id IS NOT NULL THEN
  SELECT * INTO target FROM ledger.classification_event WHERE owner_id=NEW.owner_id AND transaction_id=NEW.transaction_id AND id=NEW.undo_of_event_id;
  IF NOT FOUND OR target.revision=0 OR target.id!=prior.id THEN RAISE EXCEPTION 'invalid_undo' USING ERRCODE='23514'; END IF;
  SELECT * INTO restored FROM ledger.classification_event WHERE id=target.previous_event_id;
  IF NEW.category!=restored.category OR NEW.review_status!=restored.review_status THEN
   RAISE EXCEPTION 'invalid_undo_value' USING ERRCODE='23514'; END IF;
 END IF;
 IF NEW.revision>0 THEN
  UPDATE ledger.transaction_link SET revoked_at=clock_timestamp(),revocation_actor_owner_id=NEW.owner_id,
   revocation_reason='classification_changed' WHERE owner_id=NEW.owner_id AND revoked_at IS NULL
   AND (from_transaction_id=NEW.transaction_id OR to_transaction_id=NEW.transaction_id);
 END IF;
 NEW.created_at=clock_timestamp();
 RETURN NEW;
END $$;
CREATE TRIGGER b_classification BEFORE INSERT ON ledger.classification_event FOR EACH ROW EXECUTE FUNCTION ledger.check_classification();
CREATE FUNCTION ledger.initial_classification() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
 INSERT INTO ledger.classification_event(id,owner_id,transaction_id,revision,category,review_status,actor_kind)
 VALUES(gen_random_uuid(),NEW.owner_id,NEW.id,0,'unknown','needs_review','system'); RETURN NEW;
END $$;
CREATE TRIGGER initial_classification AFTER INSERT ON ledger.canonical_transaction FOR EACH ROW EXECUTE FUNCTION ledger.initial_classification();

CREATE FUNCTION ledger.check_link() RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE f record; t record; fc record; tc record; allocated numeric;
BEGIN
 SELECT x.*,a.kind INTO f FROM ledger.canonical_transaction x JOIN ledger.financial_account a ON (a.owner_id,a.id)=(x.owner_id,x.account_id)
 WHERE x.owner_id=NEW.owner_id AND x.id=NEW.from_transaction_id;
 IF NOT FOUND THEN RAISE EXCEPTION 'transaction_unavailable' USING ERRCODE='23503'; END IF;
 SELECT x.*,a.kind INTO t FROM ledger.canonical_transaction x JOIN ledger.financial_account a ON (a.owner_id,a.id)=(x.owner_id,x.account_id)
 WHERE x.owner_id=NEW.owner_id AND x.id=NEW.to_transaction_id;
 IF NOT FOUND THEN RAISE EXCEPTION 'transaction_unavailable' USING ERRCODE='23503'; END IF;
 SELECT * INTO fc FROM ledger.classification_event WHERE owner_id=NEW.owner_id AND transaction_id=f.id ORDER BY revision DESC LIMIT 1;
 SELECT * INTO tc FROM ledger.classification_event WHERE owner_id=NEW.owner_id AND transaction_id=t.id ORDER BY revision DESC LIMIT 1;
 IF f.direction!='debit' OR t.direction!='credit' OR f.currency!=t.currency OR fc.review_status!='confirmed' OR tc.review_status!='confirmed' OR NEW.revoked_at IS NOT NULL THEN
  RAISE EXCEPTION 'invalid_link' USING ERRCODE='23514'; END IF;
 IF EXISTS(SELECT 1 FROM ledger.transaction_link WHERE owner_id=NEW.owner_id AND revoked_at IS NULL AND to_transaction_id=t.id) THEN
  RAISE EXCEPTION 'credit_already_allocated' USING ERRCODE='23514'; END IF;
 IF NEW.kind IN ('transfer','repayment') THEN
  IF f.id=t.id OR f.account_id=t.account_id OR f.amount!=t.amount OR f.kind NOT IN ('bank','cash')
   OR EXISTS(SELECT 1 FROM ledger.transaction_link WHERE owner_id=NEW.owner_id AND revoked_at IS NULL AND from_transaction_id=f.id) THEN
   RAISE EXCEPTION 'invalid_pair' USING ERRCODE='23514'; END IF;
  IF NEW.kind='transfer' AND (t.kind NOT IN ('bank','cash') OR fc.category!='internal_transfer' OR tc.category!='internal_transfer') THEN
   RAISE EXCEPTION 'invalid_transfer' USING ERRCODE='23514'; END IF;
  IF NEW.kind='repayment' AND (t.kind!='credit_card' OR fc.category!='card_repayment' OR tc.category!='card_repayment') THEN
   RAISE EXCEPTION 'invalid_repayment' USING ERRCODE='23514'; END IF;
 ELSE
  IF fc.category!='consumption' OR tc.category!=NEW.kind THEN RAISE EXCEPTION 'invalid_refund' USING ERRCODE='23514'; END IF;
  SELECT coalesce(sum(x.amount),0) INTO allocated FROM ledger.transaction_link l JOIN ledger.canonical_transaction x ON (x.owner_id,x.id)=(l.owner_id,l.to_transaction_id)
   WHERE l.owner_id=NEW.owner_id AND l.from_transaction_id=f.id AND l.revoked_at IS NULL;
  IF allocated+t.amount>f.amount OR (NEW.kind='reversal' AND t.amount!=f.amount) THEN
   RAISE EXCEPTION 'refund_overallocated' USING ERRCODE='23514'; END IF;
 END IF;
 NEW.created_at=clock_timestamp(); RETURN NEW;
END $$;
CREATE TRIGGER b_link BEFORE INSERT ON ledger.transaction_link FOR EACH ROW EXECUTE FUNCTION ledger.check_link();
CREATE FUNCTION ledger.revoke_link() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
 UPDATE ledger.ledger_owner SET write_version=write_version+1 WHERE id=OLD.owner_id;
 IF OLD.revoked_at IS NOT NULL OR NEW.revoked_at IS NULL OR
  (to_jsonb(NEW)-ARRAY['revoked_at','revocation_actor_owner_id','revocation_reason']) IS DISTINCT FROM
  (to_jsonb(OLD)-ARRAY['revoked_at','revocation_actor_owner_id','revocation_reason']) THEN
  RAISE EXCEPTION 'immutable_link' USING ERRCODE='23514'; END IF;
 NEW.revoked_at=clock_timestamp(); RETURN NEW;
END $$;
CREATE TRIGGER revoke_only BEFORE UPDATE ON ledger.transaction_link FOR EACH ROW EXECUTE FUNCTION ledger.revoke_link();
CREATE TRIGGER no_link_delete BEFORE DELETE ON ledger.transaction_link FOR EACH ROW EXECUTE FUNCTION ledger.immutable();
CREATE FUNCTION ledger.coverage_update() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
 IF (NEW.id,NEW.owner_id,NEW.account_id,NEW.period_start,NEW.period_end) IS DISTINCT FROM
    (OLD.id,OLD.owner_id,OLD.account_id,OLD.period_start,OLD.period_end) THEN
  RAISE EXCEPTION 'immutable_coverage_scope' USING ERRCODE='23514'; END IF;
 UPDATE ledger.ledger_owner SET write_version=write_version+1 WHERE id=OLD.owner_id;
 NEW.updated_at=clock_timestamp(); RETURN NEW;
END $$;
CREATE TRIGGER coverage_scope BEFORE UPDATE ON ledger.account_coverage FOR EACH ROW EXECUTE FUNCTION ledger.coverage_update();
CREATE TRIGGER no_coverage_delete BEFORE DELETE ON ledger.account_coverage FOR EACH ROW EXECUTE FUNCTION ledger.immutable();
