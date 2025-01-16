"use client"
import { motion } from 'framer-motion';
import SocialMediaIconsList from './SocialMediaIconsList';
import FooterColumn from './FooterColumn';
import Copyright from './Copyright';
import { useEffect, useRef, useState } from 'react';
import LogoWithName from '@/components/common/logo/LogoWithName';
import FooterColumns from './FooterColumns';
import useVisibilityTrigger from '@/hooks/useVisibilityTrigger';
import { layoutConfig,LayoutConfigInterface } from '@/config';

const Footer: React.FC = () => {
  const [footerRef, isVisible] = useVisibilityTrigger({
    root: null,
    rootMargin: '0px',
    threshold: 0.1,
  });


  return (
    <motion.footer
      ref={footerRef}
      className="container"
      initial={{ opacity: 0, y: 50 }}
      animate={isVisible ? { opacity: 1, y: 0 } : { opacity: 0, y: 50 }}
      transition={{ duration: 0.5, ease: 'easeOut' }}
      style={{
        display:"flex",
        backgroundColor:"red",
        justifyContent:"center",
        alignItems:"center",
      }}
    >
      <div style={{
        backgroundColor:"blue",
        justifyContent:"center",
        alignItems:"center",
        userSelect:"none" ,
        flexGrow:1,
      }}>


        {/* Top Section with Logo Placeholder */}

        <div style={{
          flex:1,
          display:"flex",
          flexDirection:"row",

        }}>

          <div className="flex-shrink-0" style={{
            padding:30,
          }}>
            <LogoWithName />

          </div>

          <div className="">
            <FooterColumns
              // navLinks={layoutConfig.navigation}
              navLinks={[]}
            />
          </div>
        </div>

        <div className="flex justify-between items-center mt-auto">
          <div style={{flex:1}}/>
          <div style={{flex:1}}>
              <Copyright text={layoutConfig.copyright} />
          </div>
          <div style={{flex:1}}>
              <SocialMediaIconsList socials={[]} />
              {/* <SocialMediaIconsList socials={layoutConfig.socialLinks} /> */}
          </div>

        </div>


      </div>
    </motion.footer>
  );
};

export default Footer;
