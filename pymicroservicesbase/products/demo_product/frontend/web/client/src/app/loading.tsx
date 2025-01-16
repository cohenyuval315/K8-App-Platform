"use client"

import React from 'react';

export default function Loading() {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-900 dark:bg-gray-800">
      <div className="text-center">
        <svg className="animate-spin h-12 w-12 text-blue-400 dark:text-blue-300 mx-auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="12" cy="12" r="10" />
          <path d="M12 2a10 10 0 0 1 10 10h-2a8 8 0 0 0-8-8V2z" />
        </svg>
        <p className="mt-4 text-lg font-semibold text-gray-200 dark:text-gray-300">Loading...</p>
      </div>
    </div>
  );
}
