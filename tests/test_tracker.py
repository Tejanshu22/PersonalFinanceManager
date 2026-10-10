import importlib.util
from pathlib import Path
import unittest
import csv
import json
import tempfile
from unittest.mock import patch

SCRIPT=Path(__file__).resolve().parents[1]/'scripts'/'sync_progress.py'
spec=importlib.util.spec_from_file_location('sync_progress',SCRIPT)
tracker=importlib.util.module_from_spec(spec); spec.loader.exec_module(tracker)

class TrackerTests(unittest.TestCase):
    def test_only_closed_verified_is_done(self):
        issue={'title':'[FIN-001] Deliver feature','state':'closed','labels':[{'name':'verified'}]}
        self.assertEqual(tracker.issue_state(issue),'Verified Done')
        issue['labels']=[]
        self.assertEqual(tracker.issue_state(issue),'Needs Review')
    def test_blocked_open_and_reopened_verified_issue(self):
        self.assertEqual(tracker.issue_state({'state':'open','labels':['blocked']}),'Blocked')
        self.assertEqual(tracker.issue_state({'state':'open','labels':['verified']}),'Planned')
    def test_refuse_ambiguous_duplicate_titles(self):
        issue={'title':'[FIN-001] Implement','state':'open','labels':[]}
        with self.assertRaises(ValueError):tracker.map_issues([issue,dict(issue)])
    def test_issue_title_prefix_only(self):
        self.assertEqual(tracker.parse_issue_title({'title':'[FIN-042] Title'}),'FIN-042')
        self.assertIsNone(tracker.parse_issue_title({'title':'Refers to FIN-042'}))
    def test_status_defaults_to_planned(self):
        self.assertEqual(tracker.status_for({'id':'FIN-555'},{}),'Planned')

    def test_generate_checks_only_verified_and_produces_docs(self):
        fixtures=[
            {'id':'FIN-001','name':'Test feature A','release':'V1','category':'Core','priority':'P0',
             'target_day':1,'acceptance':'Verified output','owner':'Developer'},
            {'id':'FIN-002','name':'Test feature B','release':'V1','category':'Core','priority':'P0',
             'target_day':2,'acceptance':'Verified output','owner':'Developer'}]
        days=[{'id':'DAY-001','day':1,'week':1,'phase':'Build','task':'Test first day',
               'acceptance':'Artifact reviewed','owner':'Developer'}]
        issues=[
           {'title':'[FIN-001] Test feature A','state':'closed',
             'closed_at':'2026-10-11T11:00:00Z','html_url':'https://github.com/example/issues/1',
             'labels':[{'name':'verified'}]},
           {'title':'[FIN-002] Test feature B','state':'open','labels':[{'name':'in-progress'}]},
           {'title':'[DAY-001] First day','state':'closed','labels':[]}
        ]
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            (root/'config').mkdir()
            (root/'docs').mkdir()
            (root/'tracking').mkdir()
            (root/'config'/'brand.json').write_text(json.dumps({'display_name':'TestApp'}))
            with patch.object(tracker,'ROOT',root):
                output,_=tracker.generate(fixtures,days,issues,'2026-10-11 11:00 UTC')
            self.assertEqual(output[0]['done'],'☑')
            self.assertEqual(output[1]['done'],'☐')
            self.assertIn('Verified Done', (root/'docs'/'PROGRESS.md').read_text())
            self.assertIn('FIN-001',(root/'docs'/'COMPLETION_LOG.md').read_text())
            self.assertNotIn('FIN-002',(root/'docs'/'COMPLETION_LOG.md').read_text())
            with (root/'tracking'/'Daily_Checklist.csv').open(encoding='utf-8-sig') as f:
                rows=list(csv.DictReader(f))
            self.assertEqual(rows[0]['Status'],'Needs Review')
            self.assertEqual(rows[0]['Done'],'☐')


if __name__=='__main__':unittest.main()
