FROM node:22-bookworm-slim AS dependencies
WORKDIR /workspace/frontend
ENV NEXT_TELEMETRY_DISABLED=1
COPY frontend/package*.json ./
RUN npm ci --no-fund

FROM dependencies AS build
ENV BUILD_STANDALONE=1
# Inspect the actual filtered context BEFORE COPY. Fail closed without printing values.
RUN --mount=type=bind,target=/context find /context -name '.env*' -print > /tmp/context-env-paths \
    && test ! -s /tmp/context-env-paths && rm /tmp/context-env-paths
COPY frontend ./
COPY config /workspace/config
COPY docs/design/day05/sample-finance.json /workspace/docs/design/day05/sample-finance.json
RUN npm run build && mkdir -p public

FROM node:22-bookworm-slim
WORKDIR /app
ENV NODE_ENV=production NEXT_TELEMETRY_DISABLED=1 HOSTNAME=0.0.0.0 PORT=3000
# Traced server dependencies only; no full workspace or development node_modules.
COPY --from=build --chown=node:node /workspace/frontend/.next/standalone ./
COPY --from=build --chown=node:node /workspace/frontend/.next/static ./frontend/.next/static
COPY --from=build --chown=node:node /workspace/frontend/public ./frontend/public
USER node
EXPOSE 3000
CMD ["node", "frontend/server.js"]
