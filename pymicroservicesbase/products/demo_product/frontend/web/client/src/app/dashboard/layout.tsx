// export const dynamic = 'force-dynamic'
// import apiClient from "@/api/client";
import DashboardLayout from "@/components/dashboard/DashboardLayout";
// import { headers } from "next/headers";
import {fetchUser} from "./actions";


// getstaticprops config menu items

//   const refreshResponse = await apiClient.refreshUser();
//   if (refreshResponse.ok){
//       const freshUserResponse = await apiClient.getUser();
//       const res = await freshUserResponse.json()
//       const data = res['data'];
//       return data;
//   }
//   redirect("/unauthenticated");
// }

const drawerMenuItems = [
  { name: "Home", href: "/dashboard" },
  { name: "Sessions", href: "/dashboard/sessions" },
  { name: "Services", href: "/dashboard/services" },
  { name: "Products", href: "/dashboard/products" },
  { name: "Profile", href: "/dashboard/profile" },
  { name: "Users", href: "/dashboard/users" },
];

const headerMenuItems = [
  { name: "Profile", href: "/dashboard" },
  { name: "Logout", href: "/dashboard/demo" },
];



export default async function Layout({ children }: { children: React.ReactNode }) {
  const user = await fetchUser();
  return (
    <DashboardLayout
      user={user}
      drawerMenuItems={drawerMenuItems}
      headerMenuItems={headerMenuItems}
    >
      {children}
    </DashboardLayout>
  );
}
