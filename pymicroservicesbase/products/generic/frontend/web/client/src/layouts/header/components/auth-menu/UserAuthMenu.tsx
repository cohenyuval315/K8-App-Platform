"use client";
import { useState } from 'react';

const UserAuthMenu = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false); // Manage user login state

  const handleLogin = () => setIsLoggedIn(true);
  const handleLogout = () => setIsLoggedIn(false);

  return (
    <div className="flex items-center space-x-4">
      {/* User Menu - Conditional rendering based on login state */}
      {!isLoggedIn ? (
        <div className="flex items-center space-x-2">
          <button onClick={handleLogin} className="px-4 py-2 bg-blue-500 text-white rounded-md">Login</button>
          <button className="px-4 py-2 bg-green-500 text-white rounded-md">Sign Up</button>
        </div>
      ) : (
        <div className="relative">
          <button className="px-4 py-2 bg-gray-800 text-white rounded-md">User Menu</button>
          {/* Dropdown for logged in user */}
          <div className="absolute top-full right-0 mt-2 bg-white text-black shadow-lg rounded-md w-48">
            <ul>
              <li><a href="/profile" className="block px-4 py-2">Profile</a></li>
              <li><a href="/settings" className="block px-4 py-2">Settings</a></li>
              <li><button onClick={handleLogout} className="block w-full px-4 py-2 text-left">Logout</button></li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};

export default UserAuthMenu;
