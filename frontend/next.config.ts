import type { NextConfig } from "next";
import path from "node:path";
const config: NextConfig = {
  // Preserve the repository's authored AGENTS.md; dev must not generate new instructions.
  agentRules: false,
  // Containers use the traced server; native npm build/start keeps its existing workflow.
  output: process.env.BUILD_STANDALONE === "1" ? "standalone" : undefined,
  outputFileTracingRoot: path.resolve(__dirname, ".."),
  turbopack: { root: path.resolve(__dirname, "..") },
  poweredByHeader: false,
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "no-referrer" },
          {
            key: "Permissions-Policy",
            value: "geolocation=(self), camera=(), microphone=()",
          },
          { key: "X-Frame-Options", value: "DENY" },
        ],
      },
    ];
  },
};
export default config;
