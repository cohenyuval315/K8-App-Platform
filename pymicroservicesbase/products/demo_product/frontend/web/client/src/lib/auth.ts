import apiClient from "@/api/client";


// Function to get the session from the token (or return null if invalid)
export async function getAuthenticationUserSession() {
  const response = await apiClient.login()
  return response
}
