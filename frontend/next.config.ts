import type { NextConfig } from "next";
import path from "node:path";
const config: NextConfig = {
  // Preserve the repository's authored AGENTS.md; dev must not generate new instructions.
  agentRules: false,
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
