const mockSessions = [
  {
    userId: "U123",
    sessionId: "S456",
    tokenExpiry: "2024-01-01 12:00:00",
    lastActive: "2023-12-31 18:45:00",
    ip: "192.168.1.10",
  },
  {
    userId: "U789",
    sessionId: "S101",
    tokenExpiry: "2024-01-02 14:30:00",
    lastActive: "2023-12-31 19:00:00",
    ip: "203.0.113.45",
  },
];

export default function ServicesPage() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      {/* Header Section */}
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Services</h1>
        <p className="text-gray-600">Monitor and manage all services.</p>
      </div>

      {/* Sessions Table */}
      <div className="bg-white shadow rounded-lg p-6">
        <table className="w-full border-collapse">
          <thead>
            <tr className="bg-gray-200">
              <th className="p-3 text-left text-gray-700">User ID</th>
              <th className="p-3 text-left text-gray-700">Session ID</th>
              <th className="p-3 text-left text-gray-700">Token Expiry</th>
              <th className="p-3 text-left text-gray-700">Last Active</th>
              <th className="p-3 text-left text-gray-700">IP Address</th>
              <th className="p-3 text-left text-gray-700">Actions</th>
            </tr>
          </thead>
          <tbody>
            {mockSessions.map((session, index) => (
              <tr
                key={index}
                className="hover:bg-gray-100 border-b"
              >
                <td className="p-3">{session.userId}</td>
                <td className="p-3">{session.sessionId}</td>
                <td className="p-3">{session.tokenExpiry}</td>
                <td className="p-3">{session.lastActive}</td>
                <td className="p-3">{session.ip}</td>
                <td className="p-3">
                  <button className="bg-blue-500 text-white px-3 py-1 rounded shadow hover:bg-blue-600 mr-2">
                    View
                  </button>
                  <button className="bg-red-500 text-white px-3 py-1 rounded shadow hover:bg-red-600">
                    Revoke
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
