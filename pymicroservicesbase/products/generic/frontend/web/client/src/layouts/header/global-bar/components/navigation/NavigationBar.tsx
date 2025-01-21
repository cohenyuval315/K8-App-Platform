"use client"
import LogoWithName from '@/components/common/logo/LogoWithName';
import { useState } from 'react';
import UserNavigationMenu from '../user/UserNavigationMenu';

const NavigationBar = ({ links }:{ links:[{href:string,label:string}]}) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="navbar">
      <LogoWithName/>
      <div className={`menu-toggle ${isOpen ? 'open' : ''}`} onClick={toggleMenu}>
        <span className="bar"></span>
        <span className="bar"></span>
        <span className="bar"></span>
      </div>
      {/* <NavigationMenu />*/}
      <UserNavigationMenu />
    </nav>
  );
};

export default NavigationBar;
