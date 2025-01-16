'use client';

import { useState, useEffect } from 'react';
import CookieConsentModal from './CookieConsentModal';
import { useCookies } from "react-cookie";

const cookiePreferences = "cookiePreferences";
const path = "/";
const maxAge = 31536000; // 1 year
const defaultPreferences = {
  essential: true,
  commercial: false,
  analytics: false,
  marketing: false,
};

const CookieConsentBanner: React.FC = ({


}) => {
  const [showBanner, setShowBanner] = useState<boolean>(false);
  const [showModal, setShowModal] = useState<boolean>(false);
  const [cookies, setCookie] = useCookies([cookiePreferences]);


  // Check if the user has already set cookie preferences
  useEffect(() => {
    if (cookies.cookiePreferences) {
      setShowBanner(false); // Don't show the banner if preferences are already saved
    } else {
      setShowBanner(true); // Show the banner if preferences are not set
    }
  }, [cookies.cookiePreferences]);

  const handleAccept = () => {
    // Set default preferences as "accepted" (all cookies enabled)
    const defaultPreferences = {
      essential: true,
      commercial: true,
      analytics: true,
      marketing: true,
    };
    setCookie(cookiePreferences, defaultPreferences, { path: path, maxAge: maxAge }); // Save for 1 year
    setShowBanner(false); // Hide the banner after accepting
  };

  const handleReject = () => {
    const defaultPreferences = {
      essential: true,
      commercial: false,
      analytics: false,
      marketing: false,
    };
    setCookie(cookiePreferences, defaultPreferences, { path: path, maxAge: maxAge });
    setShowBanner(false);
  };

  const handleCustomize = () => {
    setShowModal(true); // Show the modal for customizing preferences
  };

  return (
    <>
      {showBanner && (
        <div className="transition-opacity duration-500 opacity-100 fixed bottom-0 left-0 right-0 bg-gray-800 text-white p-6 z-50">
          <div className="max-w-screen-lg mx-auto flex flex-col sm:flex-row items-center justify-between space-y-4 sm:space-y-0">
            <p className="text-sm sm:text-base text-center sm:text-left flex-1">
              We use cookies to improve your experience. By clicking "Accept All" or continuing to browse, you consent to our use of cookies.
            </p>
            <div style={{
              flex:1/8,
            }}>
            </div>
            <div className="flex justify-between w-full sm:w-auto space-x-4">
              <button
                onClick={handleAccept}
                className="w-full sm:w-auto bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700 transition duration-300"
              >
                Accept All
              </button>
              <button
                onClick={handleCustomize}
                className="w-full sm:w-auto bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition duration-300"
              >
                Customize
              </button>
              <button
                onClick={handleReject}
                className="w-full sm:w-auto bg-red-600 text-white px-6 py-3 rounded-lg hover:bg-red-700 transition duration-300"
              >
                Reject All
              </button>
            </div>
          </div>
        </div>
      )}

      {showModal && (
          <div className="transition-opacity duration-500 opacity-100">
            <CookieConsentModal onClose={() => setShowModal(false)} />
          </div>
        )}
    </>
  );
};

export default CookieConsentBanner;
