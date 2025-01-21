// "use client"


export default async function GlobalBar({
    children,
  }: Readonly<{
    children: React.ReactNode;
  }>) {
    return (
        <div
            className="app-header-global-bar"
            style={{
                display:"flex",
                justifyContent: 'space-between',
                alignItems: "center",
                padding:10,
                color: "white",
                position: "sticky",
                top: "0",
                zIndex: "1000",
            }}>
            <div className="w-full p-1"
                style={{
                    display:"flex",
                    alignItems:"center",
                    borderRadius:5,
                }}
            >
                {children}
            </div>
        </div>
    );
  }



