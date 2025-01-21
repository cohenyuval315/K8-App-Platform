// /components/auth/UsernamePasswordForm.tsx
import React, { useState } from 'react';

interface UsernamePasswordFormProps {
  onSubmit: (username: string, password: string) => void;
}

const UsernamePasswordForm: React.FC<UsernamePasswordFormProps> = ({ onSubmit }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(username, password);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input
        type="text"
        placeholder="Username or Email"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        className="w-full px-4 py-2 border rounded-lg"
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="w-full px-4 py-2 border rounded-lg"
      />
      <button
        type="submit"
        className="px-4 py-2 w-full text-white bg-green-500 rounded-lg hover:bg-green-600 transition"
      >
        Login
      </button>
    </form>
  );
};

export default UsernamePasswordForm;
