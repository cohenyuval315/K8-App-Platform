import Link from "next/link";

export default function Page() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 text-gray-800">
      <h1 className="text-3xl font-bold mb-4">Cookies Are Disabled</h1>
      <p className="text-lg mb-4">
        It seems that cookies are disabled in your browser. Cookies are
        essential for this website to function properly.
      </p>
      <p className="text-gray-600 mb-6">
        Please enable cookies in your browser settings and refresh the page.
      </p>
      <Link
        href="/"
        className="inline-block px-6 py-2 text-white bg-blue-600 hover:bg-blue-700 rounded-lg text-lg transition"
      >
        Go Back to Homepage
      </Link>
    </div>
  );
}
