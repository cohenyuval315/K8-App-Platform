import { layoutConfig } from '@/config';
import Image from 'next/image';


interface LogoWithNameProps {
  width?: number;
  height?: number;
  title?: string;
  src?:string
}

const LogoWithName: React.FC<LogoWithNameProps> = ({ width = 40, height = 40, title ="Logo", src="/assets/logo.png" }) => {
  return (
    <div className="flex items-center" style={{
      userSelect:"none",
      pointerEvents:"none"
    }} >
      <Image src={src} alt={title} width={width} height={height}  style={{
        userSelect:"none",
        pointerEvents:"none"
      }} />
      <span className="ml-2 text-lg font-bold">{title}</span>
    </div>
  );
};


export default LogoWithName;
