'use client'

import NProgress from 'nprogress';
import { useActionState, useEffect } from 'react'
import React from 'react'
import { Logout } from '../../app/dashboard/actions'

const initialState = {
  message: '',
}

export default function LogoutForm() {
  const [state, formAction, pending] = useActionState(Logout, initialState)

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
    <form action={formAction} className="flex justify-center items-center space-x-4 p-4">
      <button
        className={`px-6 py-2 text-white font-semibold rounded-lg shadow-md
          ${pending ? 'bg-gray-400' : 'bg-red-600 hover:bg-red-700'} transition-all`}
        disabled={pending}>
        {pending ? 'Logging out...' : 'Logout'}
      </button>
    </form>
  )
}
