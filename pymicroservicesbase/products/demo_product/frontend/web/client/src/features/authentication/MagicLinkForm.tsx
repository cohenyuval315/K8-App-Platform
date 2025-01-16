"use client";
import React, { useState } from "react";
import { motion } from "framer-motion";

const MagicLinkForm = () => {
  const [step, setStep] = useState(1); // Track current step
  const [emailOrPhone, setEmailOrPhone] = useState("");
  const [code, setCode] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSendCode = async () => {
    if (!emailOrPhone) {
      alert("Please enter a valid email or phone number.");
      return;
    }

    setLoading(true);
    try {
      // Mock API call
      await new Promise((resolve) => setTimeout(resolve, 1000));
      setStep(2); // Proceed to code input
    } catch (error) {
      console.error("Error sending code:", error);
      alert("Failed to send code. Try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleVerifyCode = async () => {
    if (!code) {
      alert("Please enter the verification code.");
      return;
    }

    setLoading(true);
    try {
      // Mock API call
      await new Promise((resolve) => setTimeout(resolve, 1000));
      alert("Login successful!");
      // Handle login success (e.g., redirect or store token)
    } catch (error) {
      console.error("Error verifying code:", error);
      alert("Invalid code. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <motion.div
      className="max-w-md mx-auto bg-white shadow-lg rounded-lg p-4"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -50 }}
      transition={{ duration: 0.5 }}
    >
      {step === 1 && (
        <motion.div
          key="step1"
        >
          <p className="text-gray-600 mb-6">
            Enter your email or phone number to receive a login code.
          </p>
          <input
            type="text"
            placeholder="Enter your email or phone"
            value={emailOrPhone}
            onChange={(e) => setEmailOrPhone(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring focus:ring-blue-200"
          />
          <button
            onClick={handleSendCode}
            disabled={loading}
            className={`w-full py-3 text-white font-bold rounded ${
              loading
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-blue-500 hover:bg-blue-600"
            }`}
          >
            {loading ? "Sending..." : "Send Code"}
          </button>
        </motion.div>
      )}

      {step === 2 && (
        <motion.div
          key="step2"
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -50 }}
          transition={{ duration: 0.5 }}
        >
          <h2 className="text-2xl font-bold mb-4 text-gray-800">
            Enter Verification Code
          </h2>
          <p className="text-gray-600 mb-6">
            A code has been sent to <b>{emailOrPhone}</b>. Enter it below.
          </p>
          <input
            type="text"
            placeholder="Enter code"
            value={code}
            onChange={(e) => setCode(e.target.value)}
            className="w-full p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring focus:ring-blue-200"
          />
          <button
            onClick={handleVerifyCode}
            disabled={loading}
            className={`w-full py-3 text-white font-bold rounded ${
              loading
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-green-500 hover:bg-green-600"
            }`}
          >
            {loading ? "Verifying..." : "Verify Code"}
          </button>
          <button
            onClick={() => setStep(1)}
            className="mt-4 w-full py-3 text-gray-700 font-bold rounded border border-gray-300 hover:bg-gray-100"
          >
            Back
          </button>
        </motion.div>
      )}
    </motion.div>
  );
};

export default MagicLinkForm;
