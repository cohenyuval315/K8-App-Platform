import App, { AppContext, AppInitialProps, AppProps } from 'next/app'

type AppOwnProps = {
    arg: string
}

export default function MyApp({
  Component,
  pageProps,
  arg,
}: AppProps & AppOwnProps) {
  return (
    <>
      <Component {...pageProps} />
    </>
  )
}

MyApp.getInitialProps = async (
  context: AppContext
): Promise<AppOwnProps & AppInitialProps> => {
  const ctx = await App.getInitialProps(context)

  return { ...ctx, arg: 'data' }
}
