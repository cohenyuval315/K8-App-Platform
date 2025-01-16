"use client"
import Link from "next/link";
import { useState } from "react";
import LogoutForm from "../../features/authentication/LogoutForm"

export default function Header({ user, menuItems, onMenuClick }: { user?: {email:string , name:string,avatar?:any},menuItems: {name:string, href:string, onClick?: () => {}}[], onMenuClick: () => void }) {
  const [isMenuOpen, setMenuOpen] = useState(false);

  return (
    <header className="flex justify-between items-center bg-white shadow px-6 py-4">
      <button onClick={onMenuClick} className="text-xl text-gray-500 hover:text-gray-800">
        ☰
      </button>
      <div className="relative">
        <button
          onClick={() => setMenuOpen(!isMenuOpen)}
          className="flex items-center space-x-2 text-sm font-medium text-gray-700 hover:text-gray-900"
        >
          {user ? (
            <>
            <span>{user.email}</span>
            {user.avatar ? user.avatar : (
              <img src="/assets/defaultavatar.jpg" alt="User Avatar" className="h-12 w-12 rounded-full"  />
            )}
            </>
          ): (
            <>
            {/* Skeleton loader for the name */}
            <div className="h-4 w-24 bg-gray-200 rounded animate-pulse"></div>

            {/* Skeleton loader for the avatar */}
            <div className="h-12 w-12 bg-gray-200 rounded-full animate-pulse"></div>
          </>
          )}


        </button>
        {isMenuOpen && (
          <div className="absolute right-0 mt-2 w-48 bg-white border rounded shadow">
            {menuItems.map((item) => {
              return (
                <Link
                  className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                  href={item.href}
                  key={item.name}
                  onClick={item.onClick}
                >
                  {item.name}
                </Link>
              )
            })}
          </div>
        )}
         {user && <LogoutForm/>}
      </div>
    </header>
  );
}
