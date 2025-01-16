import { Suspense } from "react";
import UserSession from "./UserSession";

const handleLogoutSession = (sessionId) => {
  alert(`Logging out session: ${sessionId}`);
};

export default function CurrentSessionPage() {
  // Fetch session data (could be from an API or database)
  const currentSession = {
    sessionId: "S456",
    userId: "U123",
    token: "abc123xyz",
    ip: "192.168.1.10",
    device: "Chrome - Windows",
    loginTime: "2023-12-31 18:00:00",
  };

  const mockSessions = [
    {
      sessionId: "S456",
      ip: "192.168.1.10",
      device: "Chrome - Windows",
      lastActive: "2023-12-31 18:45:00",
    },
    {
      sessionId: "S101",
      ip: "203.0.113.45",
      device: "Safari - macOS",
      lastActive: "2023-12-31 19:00:00",
    },
  ];

  const tableHeaders = Object.keys(currentSession);


  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-gray-800 mb-4">Current Session</h1>
      <div className="bg-white p-6 rounded-lg shadow mb-6">
        <h2 className="text-xl font-semibold mb-3">Session Details</h2>
        <Suspense>
        <div className="bg-white p-6 rounded-lg shadow mb-6">
            <h2 className="text-xl font-semibold mb-3">Session Details</h2>
            <UserSession userSessionData={currentSession}/>
        </div>

        </Suspense>
      </div>

      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-semibold mb-3">All Sessions</h2>
        <table className="w-full border-collapse">
          <thead>
            <tr className="bg-gray-200">
              <th className="p-3 text-left text-gray-700">Session ID</th>
              <th className="p-3 text-left text-gray-700">IP Address</th>
              <th className="p-3 text-left text-gray-700">Device</th>
              <th className="p-3 text-left text-gray-700">Last Active</th>
              <th className="p-3 text-left text-gray-700">Actions</th>
            </tr>
          </thead>
          <tbody>
            <Suspense>
              {mockSessions.map((session, index) => (
              <tr
                key={index}
                className="hover:bg-gray-100 border-b"
              >
                <td className="p-3">{session.sessionId}</td>
                <td className="p-3">{session.ip}</td>
                <td className="p-3">{session.device}</td>
                <td className="p-3">{session.lastActive}</td>
                <td className="p-3">
                  <button
                    // onClick={() => handleLogoutSession(session.sessionId)}
                    className="bg-red-500 text-white px-3 py-1 rounded shadow hover:bg-red-600"
                  >
                    Logout
                  </button>
                </td>
              </tr>
              ))}
            </Suspense>
          </tbody>
        </table>
      </div>
    </div>
  );
}
