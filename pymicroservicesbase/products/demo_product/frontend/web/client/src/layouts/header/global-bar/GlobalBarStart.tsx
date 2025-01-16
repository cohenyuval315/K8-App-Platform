const GlobalBarStart = ({children}:{children:any}) => {
    return (
        <div
        className="AppHeader-globalBar-start"
            style={{
                flex:"1 1 auto",
                display:"flex",
                // gap:""
            }}

            >
                {children}
        </div>
    )
}
export default GlobalBarStart;
