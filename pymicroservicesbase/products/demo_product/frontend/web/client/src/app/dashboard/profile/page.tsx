import apiClient from "@/api/client";
import ProfileForm from "../../../features/authentication/ProfileForm";
import { fetchUser } from "../actions";
import React, { Suspense } from "react";

export async function getUserProfile(){

}

export default async function Page() {
  // Get artist information
  const user = await fetchUser()

  const userData = {
    firstName: user?.firstName || "",
    lastName: user?.lastName || "",
    email: user?.email || "",
    username: user?.username || "",
    phoneNumber: user?.phoneNumber || "",
    dateOfBirth: user?.dateOfBirth || "",
    address: user?.address || "",
  };

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="w-full max-w-4xl">
          <ProfileForm userData={userData} />
        </div>
      </div>
    </Suspense>
  );
}
