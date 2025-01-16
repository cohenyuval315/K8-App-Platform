import apiClient from '@/api/client';
import dynamic from 'next/dynamic';
import { GetServerSideProps } from 'next';

export interface LoginFormConfigProps {
    loginConfig: {
      enableOAuth: boolean;
      oauthProviders: string[];
      allowUsernamePassword: boolean;
      allowPhoneLogin: boolean;
      allowGuest:boolean;

    };
}
// app/components/LoginConfig.tsx (Server Component)

import React from 'react';

export default async function LoginConfig() {
  const response = await apiClient.ping();
  // const response = await fetch('h', {
  //   next: { revalidate: 60 }, // Revalidate every 60 seconds for caching
  // });
  console.log(response);

  // Pass the configuration to the client component
  return (
    <div>
      {/* Pass data as props to the client component */}
      <LoginForm loginConfig={loginConfig} />
    </div>
  );
}

// Import Client Component


const LoginForm = dynamic(() => import('./LoginForm'), { ssr: false }); // Make sure it's a client component
