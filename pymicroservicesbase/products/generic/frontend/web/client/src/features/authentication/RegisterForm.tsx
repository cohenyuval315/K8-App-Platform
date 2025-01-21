"use client"

import NProgress from 'nprogress';
import React, { useActionState, useEffect, useState } from 'react';
import Motion from '@/components/motions/Motion';
import { registerUser } from '@/app/signup/actions';

const initialState = {
  message: "",
  errors: null
};

export interface FormField {
    name: string;
    type: string;
    title: string;
    description: string;
    required?: boolean;  // Make the required flag optional
    options?: string[];  // For select fields
    link?: string;  // Used for terms and conditions or other links
  }

interface RegisterFormProps {
  fields: FormField[];
  formAction: (formData: FormData) => void
  confirmText: string;
}

const RegisterForm: React.FC<RegisterFormProps> = ({
  fields,
  // formAction
}) => {
  // console.log(process.env)
  const [state, formAction, pending] = useActionState(registerUser, initialState);
  const [formData, setFormData] = useState<any>({});


  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    // @ts-ignore
    const { name, value, type, checked } = e.target;
    setFormData((prev:any) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  useEffect(() => {
    if (pending) {
      NProgress.start();
    } else {
      NProgress.done();
    }

    return () => {
      NProgress.done();
    };
  }, [pending]);

  return (
    <Motion
      type='div'
      className="max-w-3xl mx-auto p-8 bg-white shadow-lg rounded-lg w-full text-black"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-3xl font-semibold text-center mb-6">Register</h2>
      <form action={formAction} >


        {fields.map((field) => (
          <div key={field.name} className="mb-6">
            <label htmlFor={field.name} className="block text-lg font-medium">
              {field.title}
              {field.required && <span className="text-red-500">*</span>} {/* Mark required fields */}
            </label>
            <small className="text-gray-500 block">{field.description}</small>

            {/* Render input field based on type */}
            {field.type === 'email' && (
              <input
                disabled={pending}
                type="email"
                name={field.name}
                id={field.name}
                value={formData[field.name] || ''}
                onChange={handleChange}
                className="w-full p-4 mt-2 border border-gray-300 rounded-lg"
                placeholder={`Enter your ${field.title.toLowerCase()}`}
              />
            )}

            {field.type === 'password' && field.name !== 'confirmPassword' && (
              <input
                type="password"
                disabled={pending}
                name={field.name}
                id={field.name}
                value={formData[field.name] || ''}
                onChange={handleChange}
                className="w-full p-4 mt-2 border border-gray-300 rounded-lg"
                placeholder={`Enter your ${field.title.toLowerCase()}`}
              />
            )}

            {field.name === 'confirmPassword' && (
              <input
                type="password"
                disabled={pending}
                name={field.name}
                id={field.name}
                value={formData[field.name] || ''}
                onChange={handleChange}
                className="w-full p-4 mt-2 border border-gray-300 rounded-lg"
                placeholder={`Re-enter your password`}
              />
            )}

            {field.type === 'select' && field.options && (
              <select
                name={field.name}
                id={field.name}
                disabled={pending}
                value={formData[field.name] || ''}
                onChange={handleChange}
                className="w-full p-4 mt-2 border border-gray-300 rounded-lg"
              >
                <option value="">Select {field.title}</option>
                {field.options.map((option, idx) => (
                  <option key={idx} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            )}

            {field.type === 'tel' && (
              <input
                type="tel"
                name={field.name}
                disabled={pending}
                id={field.name}
                value={formData[field.name] || ''}
                onChange={handleChange}
                className="w-full p-4 mt-2 border border-gray-300 rounded-lg"
                placeholder="Enter your phone number"
              />
            )}

            {field.type === 'date' && (
              <input
                type="date"
                name={field.name}
                disabled={pending}
                id={field.name}
                value={formData[field.name] || ''}
                onChange={handleChange}
                className="w-full p-3 border border-gray-300 rounded-lg"
              />
            )}

            {field.type === 'checkbox' && (
              <div className="flex items-center mt-2">
                <input
                  type="checkbox"
                  name={field.name}
                  id={field.name}
                  disabled={pending}
                  checked={formData[field.name] || false}
                  onChange={handleChange}
                  className="mr-2"
                />
                <label htmlFor={field.name}>{field.title}</label>
                {field.link && (
                  <a href={field.link} className="text-blue-600 hover:underline ml-2" target="_blank" rel="noopener noreferrer">
                    {field.title}
                  </a>
                )}
              </div>
            )}

            {state?.errors?.[field.name] && <span className="text-red-500 text-sm">{state?.errors?.[field.name]}</span>}
          </div>
        ))}

            {state?.errors?.register?.length > 0 && (
                state.errors.register.map((err, index) => (

                  <Motion
                  key={index}
                  type='div'
                  className="mt-4 text-center text-red-500"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 0.5 }}
                >
                    <span className="text-red-500 text-sm">{err.message}</span>
                      </Motion>
                ))
            )}



        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-4 rounded-lg mt-4"
          disabled={pending}
        >
          {pending ? 'Submitting...' : 'Register'}

        </button>
      </form>




    </Motion>
  );
};

export default RegisterForm;


// export const SignupFormSchema = z.object({
//   name: z
//     .string()
//     .min(2, { message: 'Name must be at least 2 characters long.' })
//     .trim(),
//   email: z.string().email({ message: 'Please enter a valid email.' }).trim(),
//   password: z
//     .string()
//     .min(8, { message: 'Be at least 8 characters long' })
//     .regex(/[a-zA-Z]/, { message: 'Contain at least one letter.' })
//     .regex(/[0-9]/, { message: 'Contain at least one number.' })
//     .regex(/[^a-zA-Z0-9]/, {
//       message: 'Contain at least one special character.',
//     })
//     .trim(),
// })

// export type FormState =
//   | {
//       errors?: {
//         name?: string[]
//         email?: string[]
//         password?: string[]
//       }
//       message?: string
//     }
//   | undefined
