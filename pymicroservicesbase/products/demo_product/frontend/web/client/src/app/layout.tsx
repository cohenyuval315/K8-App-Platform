import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "../styles/globals.css";
import Header from "@/layouts/header/Header";
import Main from "@/layouts/main/Main";
import Footer from "@/layouts/footer/footer";
import StoreProvider from "./StoreProvider";
import WebContainer from "@/layouts/containers/WebContainer";
import LayoutContainer from "@/layouts/containers/LayoutContainer";
import GlobalBar from "@/layouts/header/global-bar/GlobalBar";
import LocalBar from "@/layouts/header/local-bar/LocalBar";
import { layoutConfig } from "@/config";
import CookieConsentBanner from "@/components/cookies/CookieConsentBanner";
import { Suspense } from "react";
import VerifyCookies from "@/components/cookies/VerifyCookies";
import ProgressBar from "@/components/progressbar/ProgressBar";
import apiClient from "@/api/client";
import { redirect } from "next/navigation";

const inter = Inter({ subsets: ["latin"] });



export const metadata: Metadata = {
  title: "Demo",
  description: "Demo",
};

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) { // TODO layout config injection here.


  return (
    <html lang="en">
      <body className={inter.className}>
        <StoreProvider>
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
        </StoreProvider>
      </body>
    </html>
  );
}
