
import {baseApiClient, ApiClient,ApiClientConfig} from "./api-client";
import {config} from "@/config";

const productKey = "something_wierd_demo_key"

class Client  {
    private baseApiClient:ApiClient
    constructor() {
        const apiConfig:ApiClientConfig = {
            baseUrl:"http://gateway:8000",
            productId: productKey,
            logger: console,
            refreshOnUnAuth: true
        }

        this.baseApiClient = baseApiClient.configureInstance(
            apiConfig
        );
        // this.data = config.accessToken || null;
    }
    // async setData(){

    // }

    async ping(){

        return await this.baseApiClient.ping();
    }
    async loginPassword(data:any){
        const response = await this.baseApiClient.login({
            ...data,
            login_method:"password"
        });
        return response;
    }
    async loginTokens(){
        const response = await this.baseApiClient.login({
            login_method:"tokens"
        });
        return response;
    }

    async register(data){
        const response = await this.baseApiClient.register(data);
        return response;
    }
    async logout(){
        const response = await this.baseApiClient.logout()
        return response;
    }

    async logoutSession(sessionId:string){
        const response = await this.baseApiClient.post(
            "/auth/logout",
            {sessionId: sessionId}
        );
        return response;
    }

    async loadApplicationConfig(){
        return await this.baseApiClient.get("/config")
    }
    async getOAuthProviders(){

    }



    async getProduct(){
        return await this.baseApiClient.get("/api/product")
    }

    async getUser( next?: { revalidate?: number | false | undefined; tags?: string[] | undefined; }){
        return await this.baseApiClient.get(
            "/auth/whoami",
            undefined,
            undefined,
            undefined,
            undefined,
            true,
            next
        );
    }

    async refreshUser(){
        return await this.baseApiClient.get(
            "/auth/refresh",
            undefined,
            undefined,
            undefined,
            undefined,
            true,
        );
    }

    async getUserSessions(user_id:string){
        return await this.baseApiClient.get(
            `/auth/sessions/users/${user_id}`,
            undefined,
            undefined,
            undefined,
            undefined,
            true,
        );
    }
    async updateUserProfile(data:object,user_id:string){
        return await this.baseApiClient.put(
            `/users/${user_id}`,
            data
        );
    }

    async getProductSessions(user_id:string){
        return await this.baseApiClient.get(
            `/auth/sessions/users/${user_id}`,
            undefined,
            undefined,
            undefined,
            undefined,
            true,
        );
    }

}


const apiClient = new Client();

export default apiClient;
