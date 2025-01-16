export default async function Page() {
    return (
      <div className="h-screen flex flex-col items-center justify-center bg-gray-100 text-gray-800">
        <div className="text-center">
          <h1 className="text-3xl font-bold mb-4">Welcome to Your Dashboard</h1>
          <p className="text-lg mb-6">
            Start exploring by using the navigation drawer on the left. You'll find options to access all your tools and settings.
          </p>
          <div className="bg-white p-6 rounded-lg shadow-md inline-block">
            <h2 className="text-xl font-semibold mb-2">Product Demo</h2>
            <p className="text-sm text-gray-600 mb-4">
              Dive into our product demo to see what this platform can do for you. Click below to get started!
            </p>
            <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
              View Product Demo
            </button>
          </div>
        </div>
      </div>
    );
  }
