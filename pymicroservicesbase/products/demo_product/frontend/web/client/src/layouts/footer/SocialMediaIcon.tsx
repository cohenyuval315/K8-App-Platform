import { FaFacebook, FaTwitter, FaInstagram, FaGithub } from 'react-icons/fa';
import { IconType } from 'react-icons';

const iconMap: Record<string, IconType> = {
  Facebook: FaFacebook,
  Twitter: FaTwitter,
  Instagram: FaInstagram,
  Github: FaGithub,
};

interface SocialMediaIconProps {
  name: string;
  href: string;
}

const SocialMediaIcon: React.FC<SocialMediaIconProps> = ({ name, href }) => {
  const IconComponent = iconMap[name];

  if (!IconComponent) return null;

  return (
    <div className="flex flex-col items-center">
      <a href={href} aria-label={name} className="text-xl">
        <IconComponent />
      </a>
    </div>
  );
};

export default SocialMediaIcon;
