"use client";

import React, { useState } from "react";
import { motion } from "framer-motion";
import PasswordForm from "./PasswordForm";
import MagicLinkForm from "./MagicLinkForm";
import TOTPForm from "./TOTPForm"; // TOTP (Two-Factor Authentication) form
import apiClient from "@/api/client";
import Motion from "@/components/motions/Motion";
// import { LoginWithPassword } from '@/app/login/actions';
// Login methods configuration


const LoginForm: React.FC<any> = ({loginConfig}: {loginConfig:any}) => {
  const loginMethods = loginConfig["login_methods"]

  const [activeMethod, setActiveMethod] = useState(loginMethods[0]); // Default to Password
  const [loading, setLoading] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false); // To handle multi-step forms (e.g., password > TOTP)

  // Method to change the active form based on the user choice
  const changeActiveMethod = (methodId: string) => {
    const selectedMethod = loginMethods.find((method) => method.id === methodId);
    if (selectedMethod) {
      setActiveMethod(selectedMethod);
    }
  };

  // Handle login logic (submit credentials, etc.)
  const handleLogin = async (method: string, data: any) => {

  };

  // Framer Motion animation variants
  const containerVariants = {
    hidden: { opacity: 0, scale: 0.95 },
    visible: { opacity: 1, scale: 1, transition: { duration: 0.5 } },
  };

  const formTransitionVariants = {
    hidden: { opacity: 0, y: -20 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.4 } },
  };

  return (
    <Motion
      type="div"
      className="flex justify-center"
      initial="hidden"
      animate="visible"
      variants={containerVariants}
    >
      <div className="w-full max-w-xs">
        <Motion type="h2"
          className="text-3xl font-bold text-center mb-6 text-gray-700"
          variants={containerVariants}
        >
          Welcome Back
        </Motion>

        {/* Avatar (Optional) */}
        <div className="flex justify-center mb-6">
          <Motion
            type="img"
            src="assets/defaultavatar.jpg"
            alt="Logo"
            className="rounded-full"
            style={{
              height: 200,
              width: 200,
              scale: 1,
              pointerEvents: "none",
              userSelect: "none",
            }}
            variants={containerVariants}
          />
        </div>

        {/* Displaying Active Form */}
        <h2 className="text-center text-2xl font-bold mb-4 text-gray-800">{activeMethod.title}</h2>
        <Motion
          type="div"
          className="bg-gray-700 shadow-md rounded px-8 pt-6 pb-8 mb-4 py-4"
          variants={containerVariants}
        >

          {React.createElement(activeMethod.formComponent)}
        </Motion>

        <div className="flex flex-col items-center gap-4 mb-4">
          {loginConfig["login_methods"]
            .filter((method) => method.id !== activeMethod.id) // Hide current method
            .map((method) => (
              <Motion
                type="button"
                key={method.id}
                onClick={() => changeActiveMethod(method.id)}
                disabled={loading}
                className="w-full bg-gray-500 hover:bg-gray-900 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mb-2"
                variants={formTransitionVariants}
              >
                {method.title}
              </Motion>
            ))}
        </div>

        {/* External Login Options */}
        <Motion
          type="div"
          className="flex items-center justify-between mb-4"
          variants={containerVariants}
        >
          <button
            disabled={loading}
            className="bg-gray-800 hover:bg-gray-900 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full flex items-center justify-center"
            type="button"
          >
            <i className="fab fa-google mr-2"></i> Google
          </button>
        </Motion>
      </div>
    </Motion>
  );
};

export default LoginForm;
