import { layoutConfig } from '@/config';
import Image from 'next/image';


interface LogoWithNameProps {
//   src: string;
//   alt: string;
//   name: string;
  width?: number;
  height?: number;
}

// const LogoWithName: React.FC<LogoWithNameProps> = ({ width = 40, height = 40 }) => {
//   return (
//     <div className="flex items-center">
//       <Image src={layoutConfig.brand.logo} alt={layoutConfig.brand.name} width={width} height={height}  style={{
//       }} />
//       <span className="ml-2 text-lg font-bold">{layoutConfig.brand.name}</span>
//     </div>
//   );
// };
const LogoWithName: React.FC<LogoWithNameProps> = ({ width = 40, height = 40 }) => {
  return (
    <div className="flex items-center">
      <Image src={""} alt={""} width={width} height={height}  style={{
      }} />
      <span className="ml-2 text-lg font-bold">{""}</span>
    </div>
  );
};


export default LogoWithName;
