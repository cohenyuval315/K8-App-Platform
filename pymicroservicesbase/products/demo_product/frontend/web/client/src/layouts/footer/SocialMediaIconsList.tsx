import SocialMediaIcon from './SocialMediaIcon';

interface SocialMediaLinks {
  name: string;
  href: string;
}

interface SocialMediaIconsListProps {
  socials: SocialMediaLinks[];
}

const SocialMediaIconsList: React.FC<SocialMediaIconsListProps> = ({ socials }) => {
  return (
    <div  style={{
      flex:1,
      flexDirection:"row",
      display:"flex",
      justifyContent:"end",
      paddingRight:10
    }}>
      {socials.map((social) => (
        <div key={social.name} style={{
          paddingLeft:10,
          paddingRight:10
        }}>
          <SocialMediaIcon  name={social.name} href={social.href} />
        </div>
      ))}
    </div>
  );
};

export default SocialMediaIconsList;
