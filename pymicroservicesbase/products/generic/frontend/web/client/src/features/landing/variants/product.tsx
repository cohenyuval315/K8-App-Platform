import Motion from '@/components/motions/Motion';
import Link from 'next/link';

const TITLE = "Product Dashboard";
const TITLE_HEADER = `Welcome to ${TITLE}`;
const DESCRIPTION = `The ${TITLE} gives you a comprehensive overview of your products, user sessions, and service health. Log in to unlock all the features and manage your business effectively.`;
const AUTHOR_DESCRIPTION = `
Hi! I'm Yuval Cohen, the creator of this product dashboard.
I'm passionate about building tools that help users manage their products and services efficiently.
With a background in [your background],
I’ve worked on building and scaling various tech products.`;
const SUPPORTING_COMPANIES = [
  "Yuval Cohen"
];
const WEBSITE_LINK = "https://www.linkedin.com/in/yc315/";
const WEBSITE_LINK_TITLE = "Visit my LinkedIn";
const FOOTER_TEXT = `2025 Yuval Cohen. All rights reserved.`;


export default async function Home() {
  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-r from-blue-100 via-indigo-200 to-pink-200">
      {/* Navbar */}
      <header className="bg-gray-800 text-white p-4 sticky top-0 z-50">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-3xl font-bold text-white">{TITLE}</h1>

            <Link
            href={"/login"}
            className="bg-blue-600 text-white py-2 px-6 rounded-lg text-lg hover:bg-blue-500 transition-all duration-300 transform hover:scale-105"
            >
            Login
            </Link>

        </div>
      </header>

      <Motion
        type='div'
        className="container mx-auto p-8 flex-grow"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
      >
        <section className="text-center mb-16">
          <Motion
            type='h2'
            className="text-5xl font-extrabold text-gray-800 mb-6"
            initial={{ y: -50 }}
            animate={{ y: 0 }}
            transition={{ duration: 0.6 }}
          >
            {TITLE_HEADER}
          </Motion>
          <Motion
            type='p'
            className="text-xl text-gray-600 mb-6 max-w-3xl mx-auto"
            initial={{ x: -100 }}
            animate={{ x: 0 }}
            transition={{ duration: 0.8 }}
          >
            {DESCRIPTION}
          </Motion>

          <Motion
            type='img'
            // @ts-ignore
            src="/images/dashboard-hero.jpg"
            alt="Product Dashboard"
            className="mx-auto rounded-lg shadow-xl mb-8 max-w-3xl"
            initial={{ scale: 0.8 }}
            animate={{ scale: 1 }}
            transition={{ duration: 0.8 }}
          />
          <section className="my-16">
          <Motion
              type='h3'
              className="text-3xl font-semibold text-gray-700 mb-6"
              initial={{ y: -50 }}
              animate={{ y: 0 }}
              transition={{ duration: 0.6 }}
          >
            Trusted by
          </Motion>
          <Motion
              type='div'
              className="flex justify-center overflow-hidden whitespace-nowrap"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.5, duration: 1 }}
          >
              <div className="flex space-x-8 animate-marquee">
                {SUPPORTING_COMPANIES.map((company, index) => (
                  <div key={index} className="text-xl text-gray-600">{company}</div>
                ))}
              </div>
          </Motion>
          </section>


          <section className="text-center py-16 bg-gray-50 shadow-lg rounded-lg my-16">
            <Motion
              type='h3'
              className="text-4xl font-bold text-gray-800 mb-6"
              initial={{ y: -50 }}
              animate={{ y: 0 }}
              transition={{ duration: 0.6 }}
            >
              About the Author
            </Motion>

            <Motion
              type='div'
              className="flex justify-center mb-8"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.5, duration: 1 }}
            >
              <img
                src="assets/author.jpeg" // Replace with your photo
                alt="Author"
                className="rounded-full w-40 h-40 object-cover shadow-lg border-4 border-blue-600"
              />
            </Motion>

            <Motion
              type='p'
              className="text-xl text-gray-700 max-w-3xl mx-auto mb-6"
              initial={{ x: 100 }}
              animate={{ x: 0 }}
              transition={{ duration: 0.8 }}
            >
              {AUTHOR_DESCRIPTION}
            </Motion>

            <Motion
              type='a'
              // @ts-ignore
              href={WEBSITE_LINK}
              target="_blank"
              className="text-blue-600 text-lg underline hover:text-blue-500"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              {WEBSITE_LINK_TITLE}
            </Motion>
          </section>
        </section>

      </Motion>

      <footer className="bg-gray-800 text-white py-6 mt-auto">
        <div className="container mx-auto text-center">
          <p>&copy; {FOOTER_TEXT}</p>
        </div>
      </footer>
    </div>
  );
}
