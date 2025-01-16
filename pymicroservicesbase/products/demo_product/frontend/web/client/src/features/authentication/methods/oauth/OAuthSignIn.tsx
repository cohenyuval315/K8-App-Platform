import { signIn, SignInAuthorizationParams, SignInOptions } from "next-auth/react"
import { OAuthProviderKey } from "./OAuthProviders"

export function SignIn({
  provider,
  options,
  authorizationParams,
  ...props
}: { provider?: OAuthProviderKey, options?:SignInOptions, authorizationParams?: SignInAuthorizationParams } & React.ComponentPropsWithRef<any>) {
  return (
    <button onClick={() => signIn(provider, options, authorizationParams)} {...props}>
      Sign In
    </button>
  )
}
