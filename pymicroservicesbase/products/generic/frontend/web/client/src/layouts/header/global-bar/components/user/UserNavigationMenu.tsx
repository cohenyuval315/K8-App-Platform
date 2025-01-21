// components/UserNavigationMenu.tsx
"use client"
import ButtonBase from '@/components/general/buttons/ButtonBase';
import DropdownBase from '@/components/general/dropdown/DropdownBase';
import Link from 'next/link';
import React, { useState } from 'react';

const UserNavigationMenu: React.FC = ({}) => {
  return (
    <div className="relative inline-block text-left">
      <div>
        <div className="flex space-x-4">
          <Link
            href={"/login"}
          >
            LOGIN
          </Link>
          <Link
            href={"/signup"}
          >
            SIGNUP
          </Link>
        </div>
      </div>
    </div>
  );
};

export default UserNavigationMenu;
