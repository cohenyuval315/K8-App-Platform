// app/global-error.tsx

'use client';

import React, { useEffect } from 'react';

type GlobalErrorProps = {
  error: Error & { digest?: string };
  reset: () => void;
};

const GlobalError: React.FC<GlobalErrorProps> = ({ error, reset }) => {
  useEffect(() => {
    console.error(error);
  },[error]);
  return (
    <html>
      <body>
        <div className="global-error">
          <h1>Something went wrong!</h1>
          <p>{error.message}</p>
          <button onClick={() => reset()}>Try again</button>
          <style jsx>{`
            .global-error {
              display: flex;
              flex-direction: column;
              justify-content: center;
              align-items: center;
              height: 100vh;
              text-align: center;
              background-color: #ffeeee;
              color: #cc0000;
            }
            button {
              margin-top: 20px;
              padding: 10px 20px;
              background-color: #cc0000;
              color: #fff;
              border: none;
              border-radius: 5px;
              cursor: pointer;
            }
            button:hover {
              background-color: #a30000;
            }
          `}</style>
        </div>
      </body>
    </html>
  );
};

export default GlobalError;
