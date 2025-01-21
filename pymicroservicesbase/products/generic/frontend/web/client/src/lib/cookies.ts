import 'server-only'
import { cookies } from 'next/headers'

const defaultCookiesOptions = [
    "sessionId",
    "sessionToken",
    "csrfToken",
    "accessToken",
    "idToken",
    "refreshToken",
];

export async function getCookieStore(){
    const cookieStore = await cookies()
    return cookieStore;
}

export async function deleteCookie(cookie:string){
    const cookieStore = await getCookieStore();
    cookieStore.delete(cookie);
}

export async function parseResponseCookie(cookieHeader:string){
    const cookieParts = cookieHeader.split(';');
    const [cookie] = cookieParts;
    const [cookieName, cookieValue] = cookie.split('=');
    return {
        cookieName: cookieName,
        cookieValue: cookieValue
    }
}

export async function setCookies(cookies:{cookieName:string, cookieValue:string}[]){
    cookies.forEach(cookie => {
        const {cookieName, cookieValue} = cookie;
        setCookie(cookieName,cookieValue);
    });
}


export async function setCookie(cookieName:string, cookieValue:string){
    const cookieStore = await getCookieStore();
    cookieStore.set(cookieName, cookieValue);
}

export async function setCookieIfNotExists(cookieName:string, cookieValue:string){
    const cookieStore = await getCookieStore();
    if (!cookieStore.has(cookieName)){
        cookieStore.set(cookieName, cookieValue);
    }
}


export async function setResponseCookies(response: Response) {
    const cookieStore = await getCookieStore();
    const setCookieHeaders = response.headers.getSetCookie();
    if (setCookieHeaders) {
        setCookieHeaders.forEach(cookieHeader => {
            const cookieParts = cookieHeader.split(';');
            const [cookie] = cookieParts;
            const [cookieName, cookieValue] = cookie.split('=');
            if (cookieName && cookieValue) {
                cookieStore.set(cookieName, cookieValue);
            }
        });
    }
}

export async function getCookie(cookie:string){
    const cookieStore =  await getCookieStore();
    return cookieStore.get(cookie);
}

export async function getCookies(cookie:string){
    const cookieStore =  await getCookieStore();
    return cookieStore.getAll(cookie);
}

export async function deleteCookies(cookiesOptions:string[] = defaultCookiesOptions) {
    const cookieStore = await getCookieStore();
    cookiesOptions.forEach(cookieOption => {
        cookieStore.delete(cookieOption);
    });
}

export async function deleteAllCookies() {
    const cookieStore = await getCookieStore();

}
