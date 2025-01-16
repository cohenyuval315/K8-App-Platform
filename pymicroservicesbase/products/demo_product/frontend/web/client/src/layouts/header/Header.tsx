"use client"

import { motion } from 'framer-motion';
const Header = ({children}:{children:any}) => {
  return (
    <motion.header
      className='AppHeader'
      role='banner'
      style={{
        display:"block",
        wordWrap:"break-word",
      }}

      // className="bg-gray-800 text-white p-4 shadow-md"
      // initial={{ y: -50 }}
      // animate={{ y: 0 }}
      // transition={{ type: 'spring', stiffness: 120 }}
    >
        {children}
    </motion.header>
  );
};

export default Header;
