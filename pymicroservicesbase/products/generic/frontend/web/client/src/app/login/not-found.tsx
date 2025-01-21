"use cliebnt"

import React from 'react';
import Link from 'next/link';

const NotFoundPage: React.FC = () => {
  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        height: '80vh',
        textAlign: 'center',
        padding: '0 20px',
      }}
    >
      <h1 style={{ fontSize: '3rem', marginBottom: '1rem', color: '#333' }}>
        404 - Page Not Found
      </h1>
      <p style={{ fontSize: '1.2rem', marginBottom: '2rem', color: '#666' }}>
        Oops! The page you're looking for doesn't exist.
      </p>
      <Link href="/">
          Go Back Home
      </Link>
    </div>
  );
};

export default NotFoundPage;
