import { CSRF_TOKEN_COOKIE_KEY, CSRF_TOKEN_HEADER_KEY, PRODUCT_HEADER_KEY, SERVICE_HEADER_KEY } from '@/constants';
import { Heartbeat } from './heart-beat';
import { cookies } from "next/headers";

type HTTPMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';

interface RequestParams {
    [key: string]: string | number | object | Date;
}

async function parseAndStoreCookies(setCookies: string[]) {
    const cookiesStore = await cookies();
    console.log("Set-Cookie Header:", setCookies);
    setCookies.forEach(cookieString => {
        // Trim the cookie string and log it
        const cookie = cookieString.trim();
        console.log("Parsing Cookie String:", cookie);

        // Split the cookie string into key-value and attributes
        const [keyValue, ...attributes] = cookie.split(';');

        // Log the key-value part and attributes
        console.log("Key-Value Part:", keyValue);
        console.log("Attributes:", attributes);

        // Extract the key and value from the key-value part
        const [key, value] = keyValue.split('=');
        const trimmedKey = key.trim();
        const trimmedValue = value ? value.trim() : null;

        // Log the extracted key and value
        console.log("Extracted Key:", trimmedKey);
        console.log("Extracted Value:", trimmedValue);

        // Prepare an object for cookie attributes
        const cookieAttributes = {};

        // Parse the cookie attributes and log each one
        attributes.forEach(attr => {
            const trimmedAttr = attr.trim().toLowerCase();
            console.log("Parsing Attribute:", trimmedAttr);

            if (trimmedAttr.startsWith('expires=')) {
                cookieAttributes.expires = new Date(trimmedAttr.split('=')[1].trim());
                console.log("Expires:", cookieAttributes.expires);
            } else if (trimmedAttr.startsWith('max-age=')) {
                cookieAttributes.maxAge = parseInt(trimmedAttr.split('=')[1].trim());
                console.log("Max-Age:", cookieAttributes.maxAge);
            } else if (trimmedAttr === 'secure') {
                cookieAttributes.secure = true;
                console.log("Secure:", cookieAttributes.secure);
            } else if (trimmedAttr === 'httponly') {
                cookieAttributes.httpOnly = true;
                console.log("HttpOnly:", cookieAttributes.httpOnly);
            } else if (trimmedAttr.startsWith('path=')) {
                cookieAttributes.path = trimmedAttr.split('=')[1].trim();
                console.log("Path:", cookieAttributes.path);
            } else if (trimmedAttr.startsWith('samesite=')) {
                cookieAttributes.sameSite = trimmedAttr.split('=')[1].trim();
                console.log("SameSite:", cookieAttributes.sameSite);
            }
        });

        // Log the final cookie attributes
        console.log("Final Cookie Attributes:", cookieAttributes);

        // Now, use the set method to store the cookie with its attributes
        cookiesStore.set(trimmedKey, trimmedValue, cookieAttributes);
        console.log(`Stored Cookie: ${trimmedKey} = ${trimmedValue}`);
    });
}


type TokenKey = "accessToken" | "refreshToken";

type Tokens = {
    [key in TokenKey]: string | null;
}

type Logger = {
    log: (message: string, ...args: any[]) => void;
    error: (message: string, ...args: any[]) => void;
    warn?: (message: string, ...args: any[]) => void;
    info?: (message: string, ...args: any[]) => void;
};

type Callbacks = {
    onRequestError?: (error: any, config?: RequestInit) => void;
    onResponseError?: (error: any, response?: Response) => void;
    onTimeout?: (error: any) => void;
    onCancel?: (error: any) => void;
};

export interface ApiClientConfig {
    baseUrl?: string;
    defaultTimeout?: number;
    defaultHeaders?: Headers;
    logger?: Logger;
    callbacks?: Callbacks;
    productId?: string;
    serviceId?: string;
    heartBeatIntervalTime?: number
    refreshOnUnAuth?:boolean,
    heartBeatCallback?: () => {}
}

class ApiClient {
    private static instance: ApiClient;
    private heartbeat: Heartbeat;
    private baseUrl: string;
    private languagePreference: string;
    private defaultHeaders: Headers;
    private defaultTimeout: number
    private logger: Logger;
    private callbacks: Callbacks;
    private isNavigator: boolean;
    private tokens: Tokens
    private refreshOnUnAuth: boolean;
    private tokensKeys: string[];
    private abortController: AbortController;

    private constructor(config: ApiClientConfig | null = null) {

        this.defaultTimeout = 60000;
        this.refreshOnUnAuth = false;

        this.heartbeat = Heartbeat.getInstance({ intervalTime: 99999999 || 5000 });

        this.baseUrl = "http://gateway:8000";

        this.isNavigator = typeof navigator !== "undefined";

        this.languagePreference = this.mapLanguage(this.isNavigator && navigator.language || "en;q=1, he;q=0.9, en-gb;q=0.8, ");
        const headers = new Headers();
        headers.append(
            'Content-Type','application/json'
        )
        headers.append('Accept-Language', this.languagePreference)
        // headers.append('X-Content-Type-Options', 'nosniff')
        // headers.append('Referrer-Policy', 'no-referrer-when-downgrade')
        headers.append("credentials", "include")

        this.defaultHeaders = headers;
        this.tokens = this._createTokens();
        this.tokensKeys = Object.keys(this.tokens);
        this.logger =  console;
        this.callbacks = {};
        this.abortController = new AbortController();
        ApiClient.instance = this;
        return ApiClient.instance;
    }


    public static getInstance(): ApiClient {
        if (!ApiClient.instance) {
            ApiClient.instance = new ApiClient();
        }
        return ApiClient.instance;
    }

    public configureInstance(config: ApiClientConfig | null = null): ApiClient {
        if (!config){
            return ApiClient.instance;
        }

        this.baseUrl = config.baseUrl || this.baseUrl;
        this.defaultTimeout = config.defaultTimeout || this.defaultTimeout;
        this.defaultHeaders = config.defaultHeaders || this.defaultHeaders;
        this.logger = config.logger || this.logger;
        this.callbacks = config.callbacks || this.callbacks;
        if (config.productId){
            if (this.defaultHeaders.has(PRODUCT_HEADER_KEY)){
                this.defaultHeaders.delete(PRODUCT_HEADER_KEY);
            }
            this.defaultHeaders.append(PRODUCT_HEADER_KEY, config.productId)
        }
        if (config.serviceId){
            if (this.defaultHeaders.has(SERVICE_HEADER_KEY)){
                this.defaultHeaders.delete(SERVICE_HEADER_KEY);
            }
            this.defaultHeaders.append(SERVICE_HEADER_KEY, config.serviceId)
        }
        this.refreshOnUnAuth = config.refreshOnUnAuth || false;
        return ApiClient.instance;
    }

    public getToken(key: TokenKey): string | null {
        return this.tokens[key];
    }

    public getTokens(): Tokens {
        return this.tokens;
    }

    public setToken(key: TokenKey, value: string) {
        this.tokens[key] = value;
    }

    public setTokens(tokens: Tokens): Tokens {
        Object.keys(tokens).forEach((key) => {
            this.tokens[key as TokenKey] = tokens[key as TokenKey];
        });
        return this.tokens;
    }

    private _createTokens(){
        const tokens = Object.fromEntries(
            (Object.keys({} as Tokens) as TokenKey[]).map((key) => [key, null])
        ) as Tokens;
        return tokens;
    }

    public resetTokens(){
        this.tokens = this._createTokens();
    }


    handleApiError(error:any){
        console.error(error);
        // this.logger.error('API Error:', error.response || error.message);
        this.callbacks.onResponseError?.(error, error.response);
    }

    handleRequestCancel(error:any){
        this.logger.warn?.('Request canceled:');
        this.callbacks.onCancel?.(error);
    }

    handleTimeout(error:any){
        this.logger.error('Request timeout:');
        this.callbacks.onTimeout?.(error);
    }


    /**
     * Aborts all ongoing requests.
     */
    public abortRequests(reason?:any): void {
        this.abortController.abort(reason)
    }

    /**
     * Aborts requests after a specified time length.
     * @param timeLength Time in milliseconds after which to abort the requests.
     */
    public abortRequestsByTimeLength(timeLength: number): void {
        setTimeout(() => {
            this.abortRequests();
        }, timeLength);
    }

    /**
     * Gets the current language preference.
     */
    public getLanguagePreference(): string {
        return this.languagePreference;
    }

    /**
     * Maps the browser language to the application's language settings.
     * @param language The browser's language string.
     */
    private mapLanguage(language: string): string {
        return language;
    }

    /**
     * Sets the language preference for the client.
     * @param language The language code to set.
     */
    public setLanguagePreference(language: string): void {
        this.languagePreference = language;
        this.defaultHeaders.delete('Accept-Language')
        this.defaultHeaders.append('Accept-Language', language);
    }



    /**
   * Generic request method using axios.
   * @param path The API endpoint path.
   * @param method The HTTP method.
   * @param data The request payload.
   * @param headers Additional headers.
   * @param params Query parameters.
   * @param accessToken Bearer token for authorization.
   * @param timeout Request timeout in milliseconds.
   */
    private async _request<T>(
        path: string,
        method: HTTPMethod,
        data: any = null,
        headers: Headers | null = null,
        params: RequestParams | null = null,
        timeout: number = this.defaultTimeout,
        useDefaultHeaders: boolean = true,
        next?: {
            revalidate?: number | false | undefined
            tags?: string[] | undefined
        }

    ): Promise<Response> {
        const cookieHeaderKey = "Cookie";
        const cookiesStore = await cookies()
        let baseUrl = this.baseUrl;
        const url = new URL(path, baseUrl);
        this.appendParamsToUrl(url,params);
        const finalHeaders = this.buildHeaders(headers,useDefaultHeaders)
        const csrf = cookiesStore.get(CSRF_TOKEN_COOKIE_KEY);
        finalHeaders.append(CSRF_TOKEN_HEADER_KEY,csrf ? csrf.value : "");
        finalHeaders.append(cookieHeaderKey ,cookiesStore.toString())
        const options: RequestInit = {
            method,
            headers: finalHeaders,
            body: method === 'GET' || method === 'DELETE' ? null : data ? JSON.stringify(data) : "",
            signal: this.abortController.signal,
            credentials:"include",
            next:next,

            redirect:"follow",
            // priority:"high",
            // // window:null,
            // cache:"no-store",
            // mode:"cors",

            // integrity:undefined,
            // referrerPolicy:"strict-origin-when-cross-origin"// defaut,
        };

        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), timeout);
        const fetchUrl = url.toString()


        try {
            console.log(fetchUrl, options);
            const response = await fetch(fetchUrl, options);
            const setCookies = response.headers.getSetCookie()
            await parseAndStoreCookies(setCookies);
            // setCookies.forEach((setCookie) => {
            //     console.log(setCookie);
            //     const [key, value] = setCookie.split('=');
            //     const trimmedKey = key.trim();
            //     const trimmedValue = value ? value.trim() : null;
            //     cookiesStore.set(trimmedKey, trimmedValue);
            // })

            if (this.refreshOnUnAuth && response.status == 401 && path != " /auth/login"){
                console.log("calling refresh endpoint...")
                const refreshUrl = new URL("/auth/refresh", baseUrl);
                const refreshFetchUrl = url.toString()
                const refresh = await fetch(
                    refreshFetchUrl,
                    {
                        ...options,
                        method:"POST",
                    }
                );
                const setCookies = refresh.headers.getSetCookie()
                await parseAndStoreCookies(setCookies);
                console.log(refresh,refresh.status);
                if (refresh.ok){
                    const _response = await fetch(fetchUrl, options);
                    console.log("after refresh",response.status,response.statusText);
                    return _response;
                }else{
                    return response;
                }
            }
            console.log(response.status,response.statusText);
            return response;

        } catch (error) {
            if (controller.signal.aborted) {
                this.handleTimeout(error);
                throw new Error('Request timed out');
            }
            this.handleApiError(error);
            throw error;
        } finally {
            clearTimeout(timeoutId);
        }
    }

    private appendParamsToUrl(url: URL, params: RequestParams | null) {
        if (params) {
            Object.keys(params).forEach((key) => {
                const value = params[key];

                // Check if the value is an object or a Date
                if (typeof value === 'object') {
                    // Stringify and encode the object or Date value
                    url.searchParams.append(key, encodeURIComponent(JSON.stringify(value)));
                } else {
                    // For strings and numbers, directly append
                    url.searchParams.append(key, String(value));  // Ensure number is converted to string
                }
            });
        }
    }

    private buildHeaders(
        newHeaders: Headers | null = null,
        useDefaultHeaders: boolean = true
    ): Headers {
        const finalHeaders = new Headers();
        if (useDefaultHeaders){
            this.defaultHeaders.forEach((value,key,p) => {
                finalHeaders.append(key,value)
            })
        }
        if (newHeaders){
            newHeaders.forEach((value,key,p) => {
                finalHeaders.append(key,value)
            })
        }
        return finalHeaders;
      }


    async get<T>(
        path: string,
        data: any = null,
        headers: Headers | null = null,
        params: RequestParams | null = null,
        timeout: number = this.defaultTimeout,
        useDefaultHeaders: boolean = true,
        next?: {
            revalidate?: number | false | undefined
            tags?: string[] | undefined
        }
    ): Promise<Response> {
        return await this._request(path,'GET',data,headers,params,timeout,useDefaultHeaders,next);
    }

    async put<T>(
        path: string,
        data: any = null,
        headers: Headers | null = null,
        params: RequestParams | null = null,
        timeout: number = this.defaultTimeout,
        useDefaultHeaders: boolean = true,
        next?: {
            revalidate?: number | false | undefined
            tags?: string[] | undefined
        }
    ): Promise<Response> {
        return await this._request(path,'PUT',data,headers,params,timeout,useDefaultHeaders,next);
    }


    async post<T>(
        path: string,
        data: any = null,
        headers: Headers | null = null,
        params: RequestParams | null = null,
        timeout: number = this.defaultTimeout,
        useDefaultHeaders: boolean = true,
        next?: {
            revalidate?: number | false | undefined
            tags?: string[] | undefined
        }
    ): Promise<Response> {
        return await this._request(path,'POST',data,headers,params,timeout,useDefaultHeaders,next);
    }

    async delete<T>(
        path: string,
        data: any = null,
        headers: Headers | null = null,
        params: RequestParams | null = null,
        timeout: number = this.defaultTimeout,
        useDefaultHeaders: boolean = true,
        next?: {
            revalidate?: number | false | undefined
            tags?: string[] | undefined
        }
    ): Promise<Response> {
        return await this._request(path,'DELETE',data,headers,params,timeout,useDefaultHeaders,next);
    }

    async patch<T>(
        path: string,
        data: any = null,
        headers: Headers | null = null,
        params: RequestParams | null = null,
        timeout: number = this.defaultTimeout,
        useDefaultHeaders: boolean = true,
        next?: {
            revalidate?: number | false | undefined
            tags?: string[] | undefined
        }
    ): Promise<Response> {
        return await this._request(path,'PATCH',data,headers,params,timeout,useDefaultHeaders,next);
    }




















    async ping(){
        return await this.get("/status/ping");
    }


    async login(data:any){
        return await this.post("/auth/login", data)
    }

    async register(data:any){
        const response = await this.post(
            "/auth/register",
            data,
        );
        return response;
    }

    async getUser(){
        const response = await this.get(
            "/users/me",
            // undefined,
            // undefined,
            // undefined,
            // undefined,
            // undefined,
            // false
        );
        return response;
    }

    async logout(){
        const response = await this.post("/auth/logout");
        return response;
    }
    async logoutSession(sessionId:string){
        const response = await this.post(
            "/auth/logout",
            {sessionId: sessionId}
        );
        return response;
    }



    // private async paginate(params:object, page:number, pageSize:number){
    //     return {
    //         ...params,
    //         page:page,
    //         pageSize:pageSize
    //     }
    // }

    // private async filters(params:object, filters: Record<string, any> | null = null){
    //     const formattedFilters: Record<string, any> = this.formatFilters(filters);
    //     return {
    //         ...params,
    //         ...formattedFilters
    //     }
    // }

    // private async sorts(params:object, sorts){

    //     return {
    //         ...params,
    //     }
    // }



    // private formatFilters(filters:Record<string, any> | null){
    //     const formattedFilters: Record<string, any> = {
    //         ...filters,
    //     };
    //     return formattedFilters;
    // }

    // private async _Many(
    //     path: string,
    //     method: HTTPMethod,
    //     data?: any,
    //     headers?: RequestHeaders | null,
    //     params?: RequestParams | null,
    //     auth?: Auth | null,
    //     timeout?: number,

    //     page: number | null = null,
    //     pageSize: number | null = null,
    //     filters: Record<string, any> | null = null,
    //     searchQuery: string | null = null,
    //     sortBy: string | null = null,
    //     sortOrder: number | null = null,

    // ): Promise<AxiosResponse<any>> {
    //     const formattedFilters: Record<string, any> = this.formatFilters(filters);
    //     const allParams = {
    //         page,
    //         page_size: pageSize,
    //         search_query: searchQuery,
    //         sort_by: sortBy,
    //         sort_order: sortOrder,
    //         ...formattedFilters,
    //         ...params,
    //     };
    //     return this._request<any>(path, method, data, headers, allParams, auth,timeout);
    // }

    // private async deleteMany(
    //     path: string,
    //     data?: any,
    //     headers?: RequestHeaders | null,
    //     params?: RequestParams | null,
    //     auth?: Auth | null,
    //     timeout?: number,
    //     page: number | null = null,
    //     pageSize: number | null = null,
    //     filters: Record<string, any> | null = null,
    //     searchQuery: string | null = null,
    //     sortBy: string | null = null,
    //     sortOrder: number | null = null,

    // ): Promise<AxiosResponse<any>> {
    //     return this._Many(path, "DELETE", data, headers, params, auth,timeout,page,pageSize,filters,searchQuery,sortBy,sortOrder);
    // }

    // private async getMany(
    //     path: string,
    //     data?: any,
    //     headers?: RequestHeaders | null,
    //     params?: RequestParams | null,
    //     auth?: Auth | null,
    //     timeout?: number,
    //     page: number | null = null,
    //     pageSize: number | null = null,
    //     filters: Record<string, any> | null = null,
    //     searchQuery: string | null = null,
    //     sortBy: string | null = null,
    //     sortOrder: number | null = null,

    // ): Promise<AxiosResponse<any>> {
    //     return this._Many(path, "GET", data, headers, params, auth,timeout,page,pageSize,filters,searchQuery,sortBy,sortOrder);
    // }


    // public async ping(): Promise<AxiosResponse<any>> {
    //     return this._request<any>('/api/ping', 'GET');
    // }

    public startHeartbeat() {
        this.heartbeat.start();
      }

      public pauseHeartbeat() {
        this.heartbeat.pause();
      }

      public resumeHeartbeat() {
        this.heartbeat.resume();
      }

      public stopHeartbeat() {
        this.heartbeat.stop();
      }
      public setHeartbeatCallback(callback: Function) {
        this.heartbeat.setCallback(callback);
      }
}



const baseApiClient = ApiClient.getInstance();

export {
    baseApiClient,
    ApiClient,
}
