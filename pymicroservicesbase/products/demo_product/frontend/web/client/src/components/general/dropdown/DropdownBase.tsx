// components/Dropdown.tsx
import React, { useEffect, useRef, useState } from 'react';
import { motion } from 'framer-motion';

interface DropdownProps {
  options: string[];
  followMouse?: boolean;
}

const DropdownBase: React.FC<DropdownProps> = ({ options, followMouse = false }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [position, setPosition] = useState<{ x: number; y: number }>({ x: 0, y: 0 });
  const dropdownRef = useRef<HTMLDivElement | null>(null);
  const buttonRef = useRef<HTMLButtonElement | null>(null); // Ref for the button

  // Toggle dropdown on button click
  const handleClick = () => {
    setIsOpen((prev) => !prev);

    if (buttonRef.current && !followMouse) {
      const buttonRect = buttonRef.current.getBoundingClientRect();
      setPosition({
        x: buttonRect.left + window.scrollX, // Adjust for scrolling
        y: buttonRect.bottom + window.scrollY // Place dropdown below the button
      });
    }
  };

  // Handle outside click
  const handleClickOutside = (event: MouseEvent) => {
    if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
      setIsOpen(false);
    }
  };

  // Add event listener for clicks outside the dropdown
  useEffect(() => {
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  useEffect(() => {
    if (followMouse && isOpen) {
      const handleMouseMove = (e: MouseEvent) => {
        setPosition({ x: e.pageX, y: e.pageY });
      };
      window.addEventListener('mousemove', handleMouseMove);
      return () => {
        window.removeEventListener('mousemove', handleMouseMove);
      };
    }
  }, [followMouse, isOpen]);

  return (
    <div>
      <button
        onClick={handleClick}
        ref={buttonRef} // Attach ref to button
        className="border px-4 py-2 rounded"
      >
        Toggle Dropdown
      </button>

      {isOpen && (
        <motion.div
          ref={dropdownRef}
          className="absolute bg-white border border-gray-300 rounded shadow-lg z-20"
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 0.95 }}
          style={{
            left: `${position.x}px`,
            top: `${position.y}px`,
            backgroundColor: 'red', // Just for visibility, can be removed
            position: 'absolute'
          }}
        >
          <ul className="p-2">
            {options.map((option, index) => (
              <li key={index} className="px-4 py-2 hover:bg-gray-200 cursor-pointer">
                {option}
              </li>
            ))}
          </ul>
        </motion.div>
      )}
    </div>
  );
};

export default DropdownBase;
