"use client"

import React from 'react';

export default function Loading() {
  return (
    <div className="loading">
      <p>Loading About Page...</p>
      <style jsx>{`
        .loading {
          display: flex;
          justify-content: center;
          align-items: center;
          height: 50vh;
          font-size: 1.2rem;
          color: #777;
        }
      `}</style>
    </div>
  );
}
