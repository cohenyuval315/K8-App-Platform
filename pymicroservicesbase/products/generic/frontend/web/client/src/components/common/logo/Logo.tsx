import Image from 'next/image';
import siteConfig from '@config';


interface LogoProps {
  src: string;
  alt: string;
  width?: number;
  height?: number;
}

const Logo: React.FC<LogoProps> = ({  width = 40, height = 40 }) => {
  return (
    <div className="flex items-center">
      <Image src={siteConfig.brand.logo} alt={siteConfig.brand.name} width={width} height={height} />
    </div>
  );
};

export default Logo;
