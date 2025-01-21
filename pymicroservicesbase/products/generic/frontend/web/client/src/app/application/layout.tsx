import LogoWithName from "@/components/common/logo/LogoWithName";
import Footer from "@/layouts/footer/Footer";
import UserAuthMenu from "@/layouts/header/components/auth-menu/UserAuthMenu";
import NavigationMenu from "@/layouts/header/components/nav/NavigationMenu";
import GlobalBar from "@/layouts/header/global-bar/GlobalBar";
const menuConfig = [
    {
      label: 'Home',
      link: '/',
    },
    {
      label: 'Products',
      link: '/products',
      rows:false,
      subOptions: [
        {
          label: 'Web Solutions',
          link: '/products/web',
          description: 'All things web',
          rows:true,
          subOptions: [
            { label: 'Web Hosting', link: '/products/web/hosting' },
            { label: 'Web Design', link: '/products/web/design' },
          ],
        },
        {
          label: 'App Solutions',
          link: '/products/app',
          description: 'Everything for apps',
          rows:true,
          subOptions: [
            { label: 'App Hosting', link: '/products/app/hosting' },
            { label: 'App Design', link: '/products/app/design' },
          ],
        },
        {
          label: 'Cloud Solutions',
          link: '/products/cloud',
          description: 'Powerful cloud tools',
          subOptions: [
            { label: 'Cloud Hosting', link: '/products/cloud/hosting' },
            { label: 'Cloud Storage', link: '/products/cloud/storage' },
          ],
        },
      ],
    },
    {
      label: 'Services',
      link: '/services',
      rows:true,
      subOptions: [
        { label: 'Web Development', link: '/services/web' },
        { label: 'App Development', link: '/services/app' },
        { label: 'Cloud Computing', link: '/services/cloud' },
        { label: 'AI Solutions', link: '/services/ai' },
      ],
    },
    {
      label: 'Contact',
      link: '/contact',
    },
  ];



export default async function Layout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const isLoggedIn = false;

  return (
    <div  className="min-h-screen flex flex-col">
      <GlobalBar>
      <div className="flex items-center justify-between w-full">
          <div className="flex-shrink-0" style={{
            paddingRight:50,
          }}>
            <LogoWithName />
          </div>

          <div className="flex-grow" style={{

          }}>
            <div style={{
                // display:"flex",
                justifyContent:"center",
                display:"inline-block"
            }}>
              <NavigationMenu menuItems={menuConfig} />
            </div>
          </div>

          <div className="flex-shrink-0">
            <UserAuthMenu />
          </div>
          </div>
      </GlobalBar>

      <div className="flex-grow">
        {children}
      </div>

      <Footer/>
    </div>
  );
}
