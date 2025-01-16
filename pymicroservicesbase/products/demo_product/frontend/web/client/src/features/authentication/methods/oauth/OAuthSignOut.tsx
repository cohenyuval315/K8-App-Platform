import { signOut, SignOutParams } from "next-auth/react"

export function SignOut({options,...props}:{props: React.ComponentPropsWithRef<any>, options?:SignOutParams}) {
    return (
      <button
        onClick={() => signOut(options)}
        className="w-full p-0"
        {...props}
      >
        Sign Out
      </button>
    )
  }
