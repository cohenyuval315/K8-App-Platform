// import apiClient from "@/api/client";
// import { protectedRoutes,publicRoutes } from "@/constants";
import { notFound, redirect } from "next/navigation";


// export async function fetchUser(){
//   const userResponse = await apiClient.getUser();
//   if (userResponse.ok){
//     const res = await userResponse.json()
//     const data = res['data'];
//     return data;
//   }
//   // redirect("/unauthenticated");
//   const user = await fetchUser();
//   console.log("NICE?")
// }

export default async function Page({
      params,
    }: {
      params: Promise<{ slug: string }>
    }) {
      const p =await params;
      console.log(p);
      // const { user } = await apiClient.getUserData();
      // if (!user) {
      //   redirect("/login"); // Redirect to login if not authenticated
      // }

      // const allowRoutes = ["/signup", "/login"]
      // const { slug } = await params
      // if (!allowRoutes.includes(slug)){
      //   const isAuthenticated = await getAuthentication();
      //   if (!isAuthenticated) {
      //       redirect("/login");
      //   }
      // }
      return notFound();
    }
