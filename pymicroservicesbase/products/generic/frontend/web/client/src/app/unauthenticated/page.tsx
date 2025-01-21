import Link from 'next/link'

export default function UnauthenticatedPage() {
  return (
    <div className="bg-gray-50 text-gray-800 min-h-screen flex flex-col justify-center items-center">
      <div className="container mx-auto px-6 py-12 text-center">
        <h1 className="text-4xl font-bold text-red-600 mb-4">Unauthorized Access</h1>
        <p className="text-lg text-gray-700 mb-6">
          It looks like you’re trying to access a page that requires authentication. Please log in to continue.
        </p>
        <div className="flex justify-center space-x-4">
          <Link
          href="/login"
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow hover:bg-blue-700 transition"
          >
              Log In
          </Link>
          <Link
            href="/register"
            className="bg-green-600 text-white py-2 px-6 rounded-lg shadow hover:bg-green-700 transition"
            >
              Sign Up
          </Link>
        </div>
        <p className="text-gray-600 mt-6">
          If you think this is a mistake, please contact our support
        </p>
      </div>
    </div>
  )
}
