import React from 'react';
import RegisterForm from '@/features/authentication/RegisterForm';
import Link from 'next/link';


const initialState = {
  message: '',
}

export default function Page(){
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col justify-center items-center">
      {/* Header with Login Button */}
      <div className="bg-blue-600 w-full py-4 flex justify-between items-center px-6 text-white">
        <div>
          <h1 className="text-2xl font-bold">Our Platform</h1>
        </div>
        <div>
          <Link href="/login" className="bg-white text-blue-600 px-4 py-2 rounded-lg font-semibold hover:bg-gray-200">
              Login
          </Link>
        </div>
      </div>

      <div className="w-full max-w-3xl p-8 bg-white shadow-lg rounded-lg mt-6" style={{ color: "black" }}>
        <RegisterForm
          fields={fields}
        />
      </div>
    </div>
  );
};


// we will use it to get register fields

// export async function getStaticProps() {
//   const res = await fetch('https://jsonplaceholder.typicode.com/posts');
//   const data = await res.json();

//   return {
//     props: { data },
//     revalidate: 10, // Revalidate every 10 seconds
//   };
// }
// config.ts


export interface FormField {
  name: string;
  type: string;
  title: string;
  description: string;
  required?: boolean;  // Make the required flag optional
  options?: string[];  // For select fields
  link?: string;  // Used for terms and conditions or other links
}

export const fields: FormField[] = [
  {
    name: 'email',
    type: 'email',
    title: 'Email',
    description: 'We will send a verification link to your email.',
    required: true,
  },
  {
    name: 'password',
    type: 'password',
    title: 'Password',
    description: 'Choose a secure password.',
    required: true,
  },
  {
    name: 'confirmPassword',
    type: 'password',
    title: 'Confirm Password',
    description: 'Re-enter your password for confirmation.',
    required: true,
  },
  {
    name: 'gender',
    type: 'select',
    title: 'Gender',
    description: 'Please select your gender.',
    required: false,
    options: ['Male', 'Female', 'Other'],
  },
  {
    name: 'birthDate',
    type: 'date',
    title: 'Birth Date',
    description: 'Select your date of birth.',
    required: false,
  },
  {
    name: 'phone',
    type: 'tel',
    title: 'Phone Number',
    description: 'Enter your phone number.',
    required: false,
  },
  {
    name: 'newsletter',
    type: 'checkbox',
    title: 'Newsletter',
    description: 'Sign up for our newsletter to receive updates.',
    required: false,
  },
  {
    name: 'terms',
    type: 'checkbox',
    title: 'I agree to the Terms & Conditions',
    description: 'You must accept the terms to register.',
    required: true,
    link: '/terms-and-conditions',
  },
];
