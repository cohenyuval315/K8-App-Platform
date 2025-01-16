"use client";

import Link from "next/link";

export default function Drawer({
  menuItems,
  isOpen,
  onClose,
  user,
}: {
  menuItems: { name: string; href: string }[];
  isOpen: boolean;
  onClose: () => void;
  user?: { name: string; avatar?: string } | null; // User is passed as a prop
}) {
  return (
    <div
      className={`fixed top-0 left-0 z-50 h-full bg-white shadow-lg transition-transform transform ${
        isOpen ? "translate-x-0" : "-translate-x-full"
      }`}
      style={{ width: "250px" }}
    >
      {/* Drawer Header */}
      <div className="flex flex-col items-center justify-center p-6 border-b">
        {user ? (
          <>
            {/* User Avatar */}
            <img
              src={user.avatar || "/assets/defaultavatar.jpg"}
              alt="User Avatar"
              className="h-16 w-16 rounded-full mb-3"
            />
            {/* User Name */}
            <span className="text-lg font-semibold text-gray-800">{user.name}</span>
          </>
        ) : (
          <>
            {/* Skeleton Avatar */}
            <div className="h-16 w-16 bg-gray-200 rounded-full animate-pulse mb-3"></div>
            {/* Skeleton Name */}
            <div className="h-4 w-24 bg-gray-200 rounded animate-pulse"></div>
          </>
        )}
      </div>

      {/* Drawer Menu Items */}
      <nav className="space-y-2 px-4 py-6">
        {menuItems.map((item) => (
          <Link
            key={item.name}
            href={item.href}
            className="block text-gray-700 hover:bg-gray-100 p-2 rounded transition"
          >
            {item.name}
          </Link>
        ))}
      </nav>

      {/* Close Button */}
      <button
        onClick={onClose}
        className="absolute top-4 right-4 text-gray-500 hover:text-black"
      >
        ✕
      </button>
    </div>
  );
}
