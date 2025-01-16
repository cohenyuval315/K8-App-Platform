// components/UserNavigationMenu.tsx
"use client"
import ButtonBase from '@/components/general/buttons/ButtonBase';
import DropdownBase from '@/components/general/dropdown/DropdownBase';
import React, { useState } from 'react';

const UserNavigationMenu: React.FC = ({}) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const handleLogin = () => {
    setIsLoggedIn(true);
    setIsDropdownOpen(false); // Close dropdown if it's open
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
    setIsDropdownOpen(false); // Close dropdown on logout
  };

  const toggleDropdown = () => {
    setIsDropdownOpen((prev) => !prev);
  };
  const options = ['Option 1', 'Option 2', 'Option 3', 'Option 4'];

  return (
    <div className="relative inline-block text-left">
      <div>
        {!isLoggedIn ? (
          <div className="flex space-x-4">
            <ButtonBase onClick={handleLogin} variant="primary">
              Log In
            </ButtonBase>
            <ButtonBase variant="secondary">Sign Up</ButtonBase>
          </div>
        ) : (
          <div>
            <ButtonBase
              onClick={toggleDropdown}
              className="flex items-center"
            >
              <img
                src="/path/to/user/icon.png" // Replace with your user icon path
                alt="User Icon"
                className="w-6 h-6 mr-2"
              />
              User Menu
            </ButtonBase>
            <DropdownBase
                options={options}
                // followMouse={true}
            />
            {/* {isDropdownOpen && (
              <div className="absolute right-0 mt-2 w-48 bg-white border border-gray-300 rounded shadow-lg z-20">
                <ButtonBase
                  onClick={handleLogout}
                  className="block text-left w-full"
                >
                  Logout
                </ButtonBase>
                <ButtonBase className="block text-left w-full">
                  Profile
                </ButtonBase>
                <ButtonBase className="block text-left w-full">
                  Settings
                </ButtonBase>
                <ButtonBase className="block text-left w-full">
                  Dashboard
                </ButtonBase>
              </div>
            )} */}
          </div>
        )}
      </div>
    </div>
  );
};

export default UserNavigationMenu;
