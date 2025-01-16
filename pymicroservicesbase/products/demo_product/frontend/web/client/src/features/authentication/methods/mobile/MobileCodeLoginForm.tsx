import React, { useState } from 'react';

interface PhoneLoginProps {
  onSubmit: (phone: string, code: string) => void;
}

const PhoneLogin: React.FC<PhoneLoginProps> = ({ onSubmit }) => {
  const [phone, setPhone] = useState('');
  const [code, setCode] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(phone, code);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input
        type="text"
        placeholder="Phone Number"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
        className="w-full px-4 py-2 border rounded-lg"
      />
      <input
        type="text"
        placeholder="One-Time Code"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        className="w-full px-4 py-2 border rounded-lg"
      />
      <button
        type="submit"
        className="px-4 py-2 w-full text-white bg-purple-500 rounded-lg hover:bg-purple-600 transition"
      >
        Login
      </button>
    </form>
  );
};

export default PhoneLogin;
