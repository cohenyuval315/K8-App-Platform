"use server"
import apiClient from '@/api/client'
import { revalidatePath } from "next/cache";
import { redirect } from 'next/navigation';
import { z } from "zod";

export async function updateUserProfile(prevState: {
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
  const response = await apiClient.updateUserProfile(newUserData);
  if (response.ok){
    redirect("/register/success");
    return {
      message: "Success"
    }
  }

  if (!response.ok){
    const results = await response.json()
    const errs = results['errors']
    return {
      errors: {
        "profile": [...errs]
      },
      message: "Fail To update profile"
    }
  }


}
