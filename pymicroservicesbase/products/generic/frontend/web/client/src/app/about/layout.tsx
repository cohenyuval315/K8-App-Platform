import Link from "next/link";

const Layout = ({ children }: {children:React.ReactNode}) => {
  return (
    <div className="min-h-screen flex flex-col bg-gray-100">
      <header className="bg-blue-600 text-white py-4">
        <div className="container mx-auto px-6 flex justify-between items-center">
          <h1 className="text-2xl font-bold">Yuval Cohen</h1>
          <nav>
            <Link href="/" className="text-white hover:underline px-3">
              Home
            </Link>
            <Link href="/about" className="text-white hover:underline px-3">
              About
            </Link>
          </nav>
        </div>
      </header>
      <main className="flex-grow">{children}</main>
      <footer className="bg-gray-800 text-gray-300 py-6 text-center">
        <p>© 2025 Yuval Cohen. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Layout;
