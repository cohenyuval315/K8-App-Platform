const GlobalBarEnd = ({children}:{children:any}) => {
    return (
        <div
        className="AppHeader-globalBar-end"
            style={{
                flex:"0 1 auto",
                display:"flex",
                justifyContent:"flex-end",
                // gap
                // maxHeight calc(var(--base-size-32, 32px));
            }}
            >
                {children}
        </div>
    )
}

export default GlobalBarEnd;
