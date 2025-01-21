"use client"

import { useState } from "react";
import Drawer from "./Drawer";
import Header from "./Header";


export default function DashboardLayout({
  drawerMenuItems,
  headerMenuItems,
  user,
  children }: { headerMenuItems:any, drawerMenuItems:any, user?: { email:string, name: string; avatar?: string } | undefined, children: React.ReactNode }) {
    const [isDrawerOpen, setDrawerOpen] = useState(false);


    return (
      <div className="flex h-screen bg-gray-100">
        <Drawer
         user={user}
           menuItems={drawerMenuItems}
          isOpen={isDrawerOpen}
          onClose={() => setDrawerOpen(false)}
        />
        <div className="flex flex-col flex-1">
          <Header
          user={user}
          menuItems={headerMenuItems}
          onMenuClick={() => setDrawerOpen(!isDrawerOpen)} />
          <main className="p-6 flex-1 overflow-y-auto">{children}</main>
        </div>
      </div>
    );
  }
