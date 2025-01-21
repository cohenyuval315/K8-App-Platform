import { FcGoogle } from "react-icons/fc";
import { FaGithub } from "react-icons/fa";
import { FaApple } from "react-icons/fa";
import { FaMicrosoft } from "react-icons/fa";
import { FaLinkedin } from "react-icons/fa";
import { FaFacebook } from "react-icons/fa";
import { FaInstagram } from "react-icons/fa";
import { FaAmazon } from "react-icons/fa";
import { FaSquareXTwitter } from "react-icons/fa6";
import { IconType } from "react-icons";

type OAuthProviderKey = 'google' | 'facebook' | 'github' | 'microsoft' | 'apple' | 'linkedin' | 'instagram' | 'amazon' | 'twitter';
interface OAuthProvider {
    icon: IconType
}
const OAuthProviders: Record<OAuthProviderKey, OAuthProvider> = {
    google: {
        icon: FcGoogle
    },
    microsoft:{
        icon:FaMicrosoft
    },
    github: {
        icon:FaGithub
    },
    facebook: {
        icon: FaFacebook
    },
    apple: {
        icon:FaApple
    },
    linkedin:{
        icon:FaLinkedin
    },
    instagram :{
        icon:FaInstagram
    },
    amazon: {
        icon:FaAmazon
    },
    twitter: {
        icon:FaSquareXTwitter
    }
}


export {
    OAuthProviders,
    type OAuthProviderKey
};
