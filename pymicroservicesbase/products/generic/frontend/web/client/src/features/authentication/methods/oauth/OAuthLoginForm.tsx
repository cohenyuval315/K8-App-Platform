import React from 'react';
import NextAuth from "next-auth"
import GoogleProvider from "next-auth/providers/google"
import OAuthButton from './OAuthLoginButton';



const OAuthLoginForm = ({onSubmit}) => {
    return (
        <div>
            <OAuthButton
                onClick={onSubmit}
                provider='google'

            />
        </div>
    )
}

export default OAuthLoginForm;
