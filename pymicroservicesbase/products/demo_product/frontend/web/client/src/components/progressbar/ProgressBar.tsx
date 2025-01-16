"use client"
import NextNProgress from 'nextjs-progressbar';

export default function ProgressBar() {
  return (
    <>
      <NextNProgress
        color="#4e54c8"
        startPosition={0.3}
        stopDelayMs={200}
        height={4}
        showOnShallow={true}
      />
    </>
  );
}
