"use client";

import { useEffect, useState } from "react";
import CookieConsentBanner from "./CookieConsentBanner";
import { useCookies } from "react-cookie";

export default function VerifyCookies({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const testCookieName = "testcookie";
  const testCookieValue = "test";
  const testCookiePath = "/";
  const [cookieEnabled, setCookieEnabled] = useState(true);

  const [cookies, setCookie, removeCookie] = useCookies([testCookieName]);

//   useEffect(() => {
//     const checkCookies = () => {
//       // Check if cookies are enabled in the browser

//       let isCookieEnabled = false;
//       if (navigator == undefined) {
//         isCookieEnabled = true;
//       } else {
//         isCookieEnabled = navigator.cookieEnabled;
//       }
//       console.log("cookies", cookies)
//       if (!isCookieEnabled) {
//         console.error("Cookies are disabled");
//         window.location.href = "/no-cookies";
//         return;
//       }
//       console.log("cookies", cookies)
//       // Set the test cookie if cookies are enabled
//       setCookie(testCookieName, testCookieValue, { path: testCookiePath, secure: true, httpOnly: false, maxAge: 10 });

//       // Check if the cookie is set
//       if (cookies[testCookieName] === testCookieValue) {
//         console.log("nah");
//         // If the cookie exists, mark it as enabled and remove the test cookie
//         setCookieEnabled(true);
//         // removeCookie(testCookieName, { path: testCookiePath, secure: true, httpOnly: false, maxAge: 10 });
//       } else {
//         console.error("Test cookie failed - cookies are disabled");
//         // window.location.href = "/no-cookies";
//       }
//     };
//     checkCookies();
//   }, []);

//   useEffect(() => {
//     if (cookies[testCookieName] === testCookieValue) {
//         console.log("nah");
//         setCookieEnabled(true);
//       }else{
//         setCookieEnabled(false);
//       }
//   },[cookies])

  return (
    <>
      {cookieEnabled && (
        <>
          {children}
          <CookieConsentBanner />
        </>
      )}
    </>
  );
}
