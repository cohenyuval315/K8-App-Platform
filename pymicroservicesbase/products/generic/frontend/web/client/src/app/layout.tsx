import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "../styles/globals.css";
import Main from "@/layouts/main/Main";
import WebContainer from "@/layouts/containers/WebContainer";
import LayoutContainer from "@/layouts/containers/LayoutContainer";
import { Suspense } from "react";
import VerifyCookies from "@/components/cookies/VerifyCookies";
import ProgressBar from "@/components/progressbar/ProgressBar";
import AppProviders from "./Providers";
import Footer from "@/layouts/footer/Footer";

const inter = Inter({ subsets: ["latin"] });



export const metadata: Metadata = {
  title: "Demo",
  description: "Demo",
};

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AppProviders>
            <WebContainer>
              <LayoutContainer>
                <Main>
                  <Suspense>
                    <VerifyCookies>
                      {children}
                    </VerifyCookies>
                    <ProgressBar/>
                  </Suspense>
                </Main>
              </LayoutContainer>
            </WebContainer>
        </AppProviders>
      </body>
    </html>
  );
}
