"use server"
import apiClient from '@/api/client'
import { revalidatePath } from "next/cache";
import { redirect } from 'next/navigation';

export async function Logout(prevState: {
  message:string,
},formData: FormData) {
  const response = await apiClient.logout();
  if (response.ok){
    redirect("/")
  }else{
    console.error(response);
    redirect("/")
  }

}


export async function fetchUser(){
    const userResponse = await apiClient.getUser();
    if (userResponse.ok){
      const res = await userResponse.json()
      const data = res['data'];
      return data;
    }else if (userResponse.status == 401){
      redirect("/unauthenticated")
    }
    else {
      redirect("/login")
    }
  }
