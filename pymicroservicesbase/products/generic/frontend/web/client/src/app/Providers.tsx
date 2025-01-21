import StoreProvider from "./StoreProvider"


export default function AppProviders({
  children
}: {
  children: React.ReactNode
}) {

  return (
    <>
        <StoreProvider>
            {children}
        </StoreProvider>
    </>
  )
}
