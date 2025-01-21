"use server"
import apiClient from '@/api/client'
import { revalidatePath } from "next/cache";
import { redirect } from 'next/navigation';


export async function getUserSessions(){
    const response = await apiClient.getUserSessions();
    if (response.ok){
        const result = await response.json();
        const data = result['data']
        return data
    }else{
        console.error(response);
        return {};
    }
}
