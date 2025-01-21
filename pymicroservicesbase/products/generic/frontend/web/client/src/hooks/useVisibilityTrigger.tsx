"use client"

import { useEffect, useRef, useState } from 'react';

const useVisibilityTrigger = (
  options?: IntersectionObserverInit,
  retrigger:boolean=false
): [React.RefObject<HTMLDivElement>, boolean] => {
  const [isVisible, setIsVisible] = useState(false);
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        } else {
          if(retrigger){
            setIsVisible(false);
          }

        }
      },
      options
    );

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => {
      if (ref.current) {
        observer.unobserve(ref.current);
      }
    };
  }, [options]);

  return [ref, isVisible];
};

export default useVisibilityTrigger;
