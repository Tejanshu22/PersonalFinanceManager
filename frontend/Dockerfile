FROM node:22-bookworm-slim AS build
WORKDIR /workspace/frontend
ENV NEXT_TELEMETRY_DISABLED=1
COPY frontend/package*.json ./
RUN npm ci --no-fund
COPY frontend ./
COPY config /workspace/config
COPY docs/design/day05/sample-finance.json /workspace/docs/design/day05/sample-finance.json
RUN npm run build

FROM node:22-bookworm-slim
WORKDIR /workspace/frontend
ENV NODE_ENV=production NEXT_TELEMETRY_DISABLED=1
COPY --from=build --chown=node:node /workspace /workspace
USER node
EXPOSE 3000
CMD ["./node_modules/.bin/next", "start", "--hostname", "0.0.0.0"]
