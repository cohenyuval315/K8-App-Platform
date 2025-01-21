// /components/auth/OAuthButton.tsx
import React from 'react';
import { OAuthProviders,OAuthProviderKey } from './OAuthProviders';

interface OAuthButtonProps {
  provider: OAuthProviderKey;
  text: string;
  onClick: () => void;
}

const OAuthButton: React.FC<OAuthButtonProps> = ({ provider, text, onClick }) => {

  if (!Object.keys(OAuthProviders).includes(provider.toLowerCase() as any)) {
    return null;
  }

  const providerData = OAuthProviders[provider.toLowerCase() as OAuthProviderKey];
  const providerCapitalized = `${provider.charAt(0).toUpperCase()}${provider.slice(1).toLowerCase()}`;


  return (
    <button
      onClick={onClick}
      className="flex items-center space-x-3 bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 focus:outline-none"
    >
      <div className="w-6 h-6">
        <providerData.icon />
      </div>
      <span className="font-medium">{text} {providerCapitalized}</span>
    </button>
  );
};

export default OAuthButton;
