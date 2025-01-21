"use server"
import apiClient from '@/api/client'
import { revalidatePath } from "next/cache";
import { redirect } from 'next/navigation';
import { z } from "zod";

export async function registerUser(prevState: {
  message:string,
  errors: object | null
},formData: FormData) {
  const registerSchema = z.object({
    // firstName: z.string(),
    // lastName: z.string(),
    // userName: z.string(),
    email: z.string({
      invalid_type_error: 'Invalid Email',
    }).email(),
    phone: z.string({
      invalid_type_error: 'Invalid PhoneNumber',
    }).transform(data => Number(data)).optional(),
    password: z.string({
      invalid_type_error: 'Invalid Password',
    }).min(4),
    confirmPassword: z.string({
      invalid_type_error: 'Invalid Confirm Password',
    }).min(4),
    // avatar: z.string().optional(),
    // isVerified: z.boolean().optional()
  })
  .superRefine(({ confirmPassword, password }, ctx) => {
  if (confirmPassword !== password) {
    ctx.addIssue({
      code: "custom",
      message: "The passwords did not match",
      path: ['confirmPassword']
    });
  }
  })



  const validatedFields = registerSchema.safeParse({
    email: formData.get('email'),
    password: formData.get('password'),
    confirmPassword: formData.get('confirmPassword'),
  })
  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    }
  }

  const newUserData = {};
  formData.forEach((value, key) => {
    newUserData[key] = value;
  });
  const response = await apiClient.register(newUserData);
  if (response.ok){
    redirect("/register/success");
    return {
      message: "Success"
    }
  }

  if (!response.ok){
    const results = await response.json()
    const errors = results['errors']
    console.log(results)
    return {
      errors: {
        "register": errors
      },
      message: "Fail To Register"
    }
  }


}
