// components/ButtonBase.tsx
import React from 'react';

interface ButtonBaseProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline';
}

const ButtonBase: React.FC<ButtonBaseProps> = ({
  variant = 'primary',
  children,
  className = '',
  ...props
}) => {
  const baseClasses = 'px-4 py-2 rounded transition duration-200';
  const variantClasses = {
    primary: 'bg-blue-500 text-white hover:bg-blue-600',
    secondary: 'bg-gray-500 text-white hover:bg-gray-600',
    outline: 'border border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white',
  };

  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};

export default ButtonBase;
