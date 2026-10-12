import type { Metadata } from "next";
import brand from "../../config/brand.json";
import "./globals.css";
export const metadata: Metadata = {
  title: `${brand.display_name} — Your money. In perspective.`,
  description: brand.tagline,
  robots: { index: false, follow: false },
};
export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
