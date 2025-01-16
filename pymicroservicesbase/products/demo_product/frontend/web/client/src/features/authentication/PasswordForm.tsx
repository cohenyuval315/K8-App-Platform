"use client"

import React, { useActionState, useEffect, useState } from 'react';
import NProgress from 'nprogress';
import Motion from '@/components/motions/Motion';
import { LoginWithPassword } from '@/app/login/actions';


const initialState = {
  message:"",
  errors:null
}

const PasswordForm = () => {
  const [state, formAction, pending] = useActionState(LoginWithPassword, initialState);
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
      className="max-w-md mx-auto bg-white shadow-lg rounded-lg p-4"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -50 }}
      transition={{ duration: 0.5 }}
    >
        <form action={formAction}>
          <div className="mb-4">
                <input
                id={"identifier"}
                name={"identifier"}
                disabled={pending}
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                type="text"
                value={formData["identifier"] || ""}
                placeholder="username or name@gmail.com"
                onChange={handleChange}
                />
                {state?.errors?.["identifier"] && <span className="text-red-500 text-sm">{state?.errors?.["identifier"]}</span>}
          </div>
          <div className="mb-6">
              <input
              id={"password"}
              name={"password"}
                disabled={pending}
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                type="password"
                placeholder="password"
                value={formData["password"] || ""}
                onChange={handleChange}
              />
              {state?.errors?.["password"] && <span className="text-red-500 text-sm">{state?.errors?.["password"]}</span>}
          </div>

            {state?.errors?.login?.length > 0 && (
                state.errors.login.map((err, index) => (

                  <Motion
                    key={index}
                    type='div'
                    className="mt-4 text-center text-red-500"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.5 }}
                  >
                    <span className="text-red-500 text-sm">{err?.message}</span>
                  </Motion>
                ))
            )}
          <div className="flex items-center justify-between mb-4">
              <button
              className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="submit"
              disabled={pending}

              >
                  {pending ? "Loading..." : "Login"}
              </button>
          </div>
        </form>
    </Motion>
  );
};

export default PasswordForm;
