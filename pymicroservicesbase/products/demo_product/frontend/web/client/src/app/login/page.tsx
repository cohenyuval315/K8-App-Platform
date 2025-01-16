import LoginForm from "@/features/authentication/LoginForm";
import BackgroundImage from "@/components/BackgroundImage";
import Link from 'next/link'
import Motion from "@/components/motions/Motion";
import PasswordForm from "@/features/authentication/PasswordForm";
import MagicLinkForm from "@/features/authentication/MagicLinkForm";
import { LoginWithPassword } from "./actions";

// is used to pre-render pages at build time. we will use it for login configurations

// export async function getStaticProps() {
//   const res = await fetch('https://jsonplaceholder.typicode.com/posts');
//   const data = await res.json();

//   return {
//     props: { data },
//     revalidate: 10, // Revalidate every 10 seconds
//   };
// }




const loginConfig = {
  login_methods:[
    {
      id: "password",
      title: "Use Password",
      formComponent: PasswordForm,// onLoginPasswordSubmit={LoginWithPassword}/> ,//</PasswordForm>, //() => <PasswordForm LoginWithPassword={LoginWithPassword}/>,
      method: "password",
      twoFactor:false
    },
    {
      id: "magiclink",
      title: "Use Magic Link",
      formComponent: MagicLinkForm,
      method: "magiclink",
      twoFactor:true
    },
  ]
}


const containerVariants = {
  hidden: { opacity: 0, scale: 0.95 },
  visible: { opacity: 1, scale: 1, transition: { duration: 0.5 } },
};

export default async function LoginPage() {
  return (
    <div className="flex min-h-screen">
      <div className="flex w-full max-w bg-white shadow-lg rounded-lg overflow-hidden" >

        {/* Left Side - Image (flexible) */}
        <div className="flex-grow bg-cover bg-center"  style={{
          // backgroundColor:"rgba(30,18,80,255)"
          backgroundColor:"rgba(6,5,90,255)"
      }}>

          {/* Optional: Add overlay for text contrast */}
            <div className="relative flex-1">

            <div className="flex items-center justify-center h-full">
                <BackgroundImage />
              </div>
            </div>
              <div className="flex text-white text-3xl font-bold justify-center " style={{
              }}>

                    <h1 className="text-white text-5xl font-bold"
                    style={{
                      padding:100,
                      userSelect:"none",
                      pointerEvents:"none",
                      fontFamily:"monospace",
                    }}
                    >Welcome to YC Platform</h1>
              </div>
        </div>
        <div className="w-1/3 p-8">
          <LoginForm
            loginConfig={loginConfig}
          />

        <Motion
            initial="hidden"
            animate="visible"
          className="flex items-center justify-center mb-4 relative flex py-5 items-center"
          variants={containerVariants}
        >
          <div className="flex-grow border-t border-gray-500"></div>
          <span className="flex-shrink mx-4 text-gray-500">YOU DON'T HAVE AN ACCOUNT?</span>
          <div className="flex-grow border-t border-gray-500"></div>
        </Motion>

          <Motion
            className="flex items-center justify-between"
            variants={containerVariants}
            initial="hidden"
            animate="visible"
          >
            <Link
              className="text-center bg-gray-800 hover:bg-gray-900 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full"
              href={{
                pathname: '/register',
                // target: "_blank",
              }}
            >
              Register
            </Link>
          </Motion>
        </div>
      </div>
    </div>

  );
}
