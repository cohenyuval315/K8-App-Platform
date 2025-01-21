import apiClient from "@/api/client";
import ProfileClient from "./ProfileClient";
import { fetchUser } from "../../actions";
import React, { Suspense } from "react";

export async function getUserProfile(){
  apiClient.getUserProfile()
}

export default async function Page({
  params,
}: {
  params: Promise<{ user_id: string }>
}) {
  const { user_id } = await params
  // Get artist information
  const user = await fetchUser()

  const userData = {
    firstName: user?.firstName || "John",
    lastName: user?.lastName || "Doe",
    email: user?.email || "john.doe@example.com",
    username: user?.username || "johndoe",
    phoneNumber: user?.phoneNumber || "+1234567890",
    dateOfBirth: user?.dateOfBirth || "1990-01-01",
    address: user?.address || "123 Main Street, Anytown, USA",
  };

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="w-full max-w-4xl">
          <ProfileClient userData={userData} />
        </div>
      </div>
    </Suspense>
  );
}
