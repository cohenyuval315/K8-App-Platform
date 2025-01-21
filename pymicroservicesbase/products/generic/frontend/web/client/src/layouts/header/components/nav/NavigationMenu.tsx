"use client"
import React, { useState } from 'react';
import Motion from '@/components/motions/Motion';

interface SubOption {
  label: string;
  link: string;
  description?: string;
  rows:boolean;
  subOptions?: SubOption[];
}

interface NavigationItem {
  label: string;
  link?: string;
  rows:boolean;
  subOptions?: SubOption[];
}

interface NavigationMenuProps {
  menuItems: NavigationItem[];
}

interface NavigationMenuLink {
  label:string;
  link?:string;
}

const NavigationMenuLink:React.FC<NavigationMenuLink>  = ({label, link}) => {
  return (

    <Motion
      className="relative" // Wrapper div to position text and background properly
      // whileHover={{ scale: 1.05 }}
      transition={{ duration: 0.3 }}
    >
      <Motion
        className="absolute inset-0 bg-gray-800 opacity-0 rounded-md" // Background div (initial opacity 0)
        whileHover={{ opacity: 0.5 }} // On hover, background opacity will change to 0.5
        transition={{ opacity: { duration: 0.5 } }} // Smooth transition of opacity
      />
      <Motion
        type='a'
        href={link ? link : "/"}
        className="text-white text-lg font-semibold hover:text-blue-500 transition-all relative z-10"
        // whileHover={{ scale: 1.1 }}
        // transition={{ duration: 0.5 }}
      >
        {label}
      </Motion>
    </Motion>

  )
}

const NavigationMenu: React.FC<NavigationMenuProps> = ({ menuItems }) => {
  const [activeIndex, setActiveIndex] = useState<number | null>(null);

  const handleMouseEnter = (index: number) => {
    setActiveIndex(index);
  };

  const handleMouseLeave = () => {
    setActiveIndex(null);
  };

  const renderMenuItems = (items: SubOption[], rows:boolean) => {
    const className = rows ? `space-x-1` : `flex space-x-${items.length}`
    return (
      <ul className={className}>
        {items.map((item, index) => (
          <li key={index}>
            {item.link ? (
              <NavigationMenuLink
                label={item.label}
                link={item.link}
              />
            ): (
              <div className='text-sm text-gray-400'>
                {item.label}
              </div>
            )}
            {item.description && <p className="text-sm text-gray-400">{item.description}</p>}

            {item.subOptions && (
              <div className="">
                {renderMenuItems(item.subOptions, item.rows)}
              </div>
            )}
          </li>
        ))}
      </ul>
    );
  };



  return (
    <nav className="w-full flex justify-center">
      <ul className="flex gap-12">
        {menuItems.map((item, index) => (
          <li
            key={index}
            className="relative group"
            onMouseEnter={() => handleMouseEnter(index)}
            onMouseLeave={handleMouseLeave}
          >

            <NavigationMenuLink
              label={item.label}
              link={item.link}
            />

            {item.subOptions && activeIndex === index && (
              <Motion
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: 10 }}
                transition={{ duration: 0.3 }}
                className="absolute top-full left-0"
              >
                {renderMenuItems(item.subOptions, item.rows)}
              </Motion>
            )}

          </li>
        ))}
      </ul>
    </nav>
  );
};

export default NavigationMenu;
