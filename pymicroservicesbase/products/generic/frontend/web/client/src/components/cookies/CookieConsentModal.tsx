'use client';

import { useState } from 'react';
import { useCookies } from "react-cookie";

interface Preferences {
  essential: boolean;
  commercial: boolean;
  analytics: boolean;
  marketing: boolean;
}

interface CookieConsentModalProps {
  onClose: () => void;
}

const CookieConsentModal: React.FC<CookieConsentModalProps> = ({ onClose }) => {
  const [cookies, setCookie] = useCookies(["cookiePreferences"]);
  const [preferences, setPreferences] = useState<Preferences>({
    essential: true, // Default to 'on' for essential cookies
    commercial: true, // Default to 'on' for commercial cookies
    analytics: true,  // Default to 'on' for analytics cookies
    marketing: true,  // Default to 'on' for marketing cookies
  });

  const handleToggle = (category: keyof Preferences) => {
    setPreferences((prev) => ({
      ...prev,
      [category]: !prev[category],
    }));
  };

  const handleSave = () => {
    setCookie("cookiePreferences", preferences, { path: "/", maxAge: 31536000, secure:true, httpOnly:true,sameSite:"strict" });
    onClose();
  };

  const handleCancel = () => {
    onClose(); // Close the modal without saving
  };

  return (
    <div className="fixed top-0 left-0 right-0 bottom-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      {/* Modal container with improved styling */}
      <div className="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 p-10 rounded-2xl w-full max-w-xl shadow-2xl">
        {/* Modal Title */}
        <h2 className="text-3xl font-semibold mb-4 text-center">Customize Cookie Preferences</h2>
        <p className="text-sm mb-6 text-center">Select your cookie preferences below. You can update these at any time.</p>

        {/* Preferences Options */}
        <div className="space-y-8">
          {/* Essential Cookies */}
          <div className="flex justify-between items-center">
            <div className="flex-1">
              <label className="font-medium text-xl">Essential Cookies</label>
              <p className="text-sm text-gray-600 dark:text-gray-400">Required for site functionality. Cannot be disabled.</p>
            </div>
            <div className="flex items-center">
              <label className="relative inline-flex items-center cursor-not-allowed">
                <input
                  type="checkbox"
                  checked={preferences.essential}
                  disabled
                  className="sr-only peer"
                />
                <div className="w-12 h-6 bg-gray-500 rounded-full dark:bg-gray-600 peer-checked:bg-gray-500 after:content-[''] after:absolute after:left-0 after:top-0 after:bg-white after:border-gray-300 after:rounded-full after:h-6 after:w-6 after:transition-all peer-checked:after:translate-x-full"></div>
              </label>
            </div>
          </div>

          {/* Commercial Cookies */}
          <div className="flex justify-between items-center">
            <div className="flex-1">
              <label className="font-medium text-xl">Commercial Cookies</label>
              <p className="text-sm text-gray-600 dark:text-gray-400">Used for personalized advertisements.</p>
            </div>
            <div className="flex items-center">
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={preferences.commercial}
                  onChange={() => handleToggle('commercial')}
                  className="sr-only peer"
                />
                <div className="w-12 h-6 bg-gray-300 rounded-full dark:bg-gray-600 peer-checked:bg-green-500 peer-checked:after:translate-x-full peer-checked:after:bg-white peer-checked:after:border-green-500 after:content-[''] after:absolute after:left-0 after:top-0 after:bg-white after:border-gray-300 after:rounded-full after:h-6 after:w-6 after:transition-all"></div>
              </label>
            </div>
          </div>

          {/* Analytics Cookies */}
          <div className="flex justify-between items-center">
            <div className="flex-1">
              <label className="font-medium text-xl">Analytics Cookies</label>
              <p className="text-sm text-gray-600 dark:text-gray-400">Used for website analytics to improve performance.</p>
            </div>
            <div className="flex items-center">
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={preferences.analytics}
                  onChange={() => handleToggle('analytics')}
                  className="sr-only peer"
                />
                <div className="w-12 h-6 bg-gray-300 rounded-full dark:bg-gray-600 peer-checked:bg-green-500 peer-checked:after:translate-x-full peer-checked:after:bg-white peer-checked:after:border-green-500 after:content-[''] after:absolute after:left-0 after:top-0 after:bg-white after:border-gray-300 after:rounded-full after:h-6 after:w-6 after:transition-all"></div>
              </label>
            </div>
          </div>

          {/* Marketing Cookies */}
          <div className="flex justify-between items-center">
            <div className="flex-1">
              <label className="font-medium text-xl">Marketing Cookies</label>
              <p className="text-sm text-gray-600 dark:text-gray-400">Used for personalized marketing campaigns.</p>
            </div>
            <div className="flex items-center">
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={preferences.marketing}
                  onChange={() => handleToggle('marketing')}
                  className="sr-only peer"
                />
                <div className="w-12 h-6 bg-gray-300 rounded-full dark:bg-gray-600 peer-checked:bg-green-500 peer-checked:after:translate-x-full peer-checked:after:bg-white peer-checked:after:border-green-500 after:content-[''] after:absolute after:left-0 after:top-0 after:bg-white after:border-gray-300 after:rounded-full after:h-6 after:w-6 after:transition-all"></div>
              </label>
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="mt-8 flex justify-center space-x-6">
          <button
            onClick={handleSave}
            className="bg-green-600 text-white px-8 py-3 rounded-full shadow-lg hover:bg-green-700 transition"
          >
            Save Preferences
          </button>
          <button
            onClick={handleCancel}
            className="bg-red-600 text-white px-8 py-3 rounded-full shadow-lg hover:bg-red-700 transition"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
};

export default CookieConsentModal;
