import config from "./config";


const date = "2024"

export interface LayoutConfigInterface {
  brand:object,
  navigation:object,
  socialLinks:object,
  copyright: string
}

export interface NavLink {
  name: string;
  href: string;
  children: NavLink[];
}

export interface FooterColumnsProps {
  navLinks: NavLink[];
}

export const layoutConfig: LayoutConfigInterface = {
    brand: {
      name: "config.getAppName()",
      logo: '/assets/logo.ico',
    },
    navigation: [
      { name: 'Home', href: '/' ,children: [
          {name: 'Testddddddddddddddddddddd', href: '/test' ,children:[]}
      ]},
      { name: 'About', href: '/about' ,children: []},
      { name: 'Contact', href: '/contact' ,children: []},
      { name: 'Blog', href: '/blog' ,children: []},
      { name: 'About', href: '/about' ,children: []},

    ],
    socialLinks: [
      { name: 'Facebook', href: 'https://facebook.com'},
      { name: 'Twitter', href: 'https://twitter.com' },
      { name: 'Instagram', href: 'https://instagram.com'},
      { name: 'Github', href: 'https://github.com'},
    ],
    copyright: `© ${date} ${"config.getAppName()"}. All rights reserved.`,
  };
