'use server'
import { cookies } from 'next/headers'

import apiClient from "@/api/client"
import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { z } from "zod";


export async function LoginWithTokens(){
    const response = await apiClient.loginTokens()
    if (!response.ok){
        redirect("/unauthenticated");
        return {
          message: "Success"
        }
      }
    return response;
}



export async function LoginWithPassword(prevState: {
  message:string,
  errors: object | null
},formData: FormData) {


    const loginSchema = z.object({
        identifier: z.string({
          invalid_type_error: 'Invalid Username or Email',
        }).refine(
          (value) => {
            const isEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value); // Simple email regex
            const isUsername = /^[a-zA-Z0-9_]{3,}$/.test(value); // Username: Alphanumeric with underscores, min 3 chars
            return isEmail || isUsername;
          },
          { message: "Identifier must be a valid email or username (min 3 characters)." }
        ),
        password: z.string({
          invalid_type_error: 'Invalid Password',
        }).min(4, { message: "Password must be at least 4 characters long." }),
      });
      console.log(formData)
  const validatedFields = loginSchema.safeParse({
    identifier: formData.get('identifier'),
    password: formData.get('password'),
  })
  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    }
  }

  const userCreds = {};
  formData.forEach((value, key) => {
    userCreds[key] = value;
  });
  const response = await apiClient.loginPassword(userCreds);
  if (!response.ok){
    const results = await response.json()
    const errs = results['errors']

    return {
      errors: {
        "login": [...errs]
      },
      message: "Fail To Login"
    }
  }


  if (response.ok){
    await setCookies(response);
    redirect("/dashboard");
  }

}


async function setCookies(response: Response) {
    const cookieStore = await cookies();
    const setCookieHeaders = response.headers.getSetCookie();
    if (setCookieHeaders) {
        setCookieHeaders.forEach(cookieHeader => {
            const cookieParts = cookieHeader.split(';');
            const [cookie] = cookieParts;
            const [cookieName, cookieValue] = cookie.split('=');
            if (cookieName && cookieValue) {
                cookieStore.set(cookieName, cookieValue);
            }
        });
    }
}


async function deleteCookies() {
    const cookieStore = await cookies();
    const cookiesOptions = [
        "sessionId",
        "sessionToken",
        "csrfToken",
        "accessToken",
        "idToken",
        "refreshToken",
    ];
    cookiesOptions.forEach(cookieOption => {
        cookieStore.delete(cookieOption);
    });

}
