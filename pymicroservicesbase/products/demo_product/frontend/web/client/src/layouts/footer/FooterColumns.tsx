import React from 'react';
import FooterColumn from './FooterColumn';

interface NavLink {
  name: string;
  href: string;
  children: NavLink[];
}

interface FooterColumnsProps {
  navLinks: NavLink[];
}

const FooterColumns: React.FC<FooterColumnsProps> = ({ navLinks }) => (
    <div style={{
        flex:1,
        display:"flex",
        flexDirection:"row",
        flexWrap:"wrap",
        // justifyContent:"space-between",

    }}>
    {navLinks.map((nav) => (
      <div key={nav.href} style={{
            flex:1,
            display:"flex",
            flexShrink:1,
            flexDirection:"column",
      }}>
        <FooterColumn link={nav} />
      </div>
    ))}
  </div>
  );
export default FooterColumns;
