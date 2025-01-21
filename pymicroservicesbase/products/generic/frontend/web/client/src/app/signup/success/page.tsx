"use client"
import React, { useEffect } from 'react';
import NProgress from "nprogress"
import { useRouter } from 'next/navigation';

const RegisterSuccessPage: React.FC = () => {
    const router = useRouter()
    useEffect(() => {
        NProgress.start()
        setTimeout(() => {
            router.replace("/login")
            NProgress.done()

        }, 3000)
    },[])
  return (
    <div className="min-h-screen bg-gray-100 flex justify-center items-center" style={{
        color:"black"
    }}>
      <div className="text-center max-w-md p-8 bg-white shadow-lg rounded-lg">
        <h2 className="text-3xl font-semibold text-green-500 mb-4">Registration Successful!</h2>
        <p className="text-lg">Thank you for registering. A confirmation email has been sent to you.</p>
        <a href="/login" className="mt-6 text-blue-500 hover:underline">Go to Login</a>
      </div>
    </div>
  );
};

export default RegisterSuccessPage;
