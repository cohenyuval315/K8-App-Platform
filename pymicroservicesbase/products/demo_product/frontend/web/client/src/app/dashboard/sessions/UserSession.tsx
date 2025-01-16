
export default function UserSession({userSessionData}:{userSessionData:any}){
    return (
        <pre className="bg-gray-100 p-4 rounded-lg overflow-auto">
            {JSON.stringify(userSessionData, null, 2)}
        </pre>
    )
}
