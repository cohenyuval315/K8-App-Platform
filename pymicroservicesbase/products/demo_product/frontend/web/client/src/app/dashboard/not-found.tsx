"use client";

import React from "react";

const NotFoundPage: React.FC = () => {
  return (
    <div className="flex flex-1 h-full  flex-col items-center justify-center text-black">
      <h1 className="text-6xl font-extrabold text-red-500">404</h1>
      <h2 className="mt-4 text-2xl font-semibold">Page Not Found</h2>
      <p className="mt-2 text-center text-gray-400">
        Sorry, the page you were looking for doesn’t exist or has been moved.
      </p>
      <button
        onClick={() => window.location.href = '/dashboard'}
        className="mt-6 rounded-lg bg-blue-600 px-6 py-3 text-white shadow-lg transition-transform hover:scale-105 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2 focus:ring-offset-gray-900"
      >
        Back to Home
      </button>
      <div className="mt-8 text-sm text-gray-500">
        If you think this is a mistake, please contact support.
      </div>
    </div>
  );
};

export default NotFoundPage;
