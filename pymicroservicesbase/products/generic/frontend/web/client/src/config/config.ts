"use client"

class Config{
    private static instance: Config;
    private serverUrl: string;
    private env: string
    private productId: string


    private constructor() {
        this.serverUrl = "http://localhost:8000" //,this._getRequiredvariable("NEXT_PUBLIC_SERVER_URL");
        // this.env = this._getRequiredvariable("NEXT_PUBLIC_ENV");
        this.productId = "demo"//,this._getRequiredvariable("NEXT_PUBLIC_PRODUCT_ID");
        Config.instance = this;
    }

    public getEnvObject(){
        return Object(process.env);
    }

    public static getInstance(): Config {
        if (!Config.instance) {
            Config.instance = new Config();
        }
        return Config.instance;
    }

    _getRequiredvariable(varName: string): string {
        const value = process.env[varName];
        if (value === undefined) {
            throw new WebClientError(`Environment variable "${varName}" is required but not set.`);
        }
        return value;
    }

    public getServerUrl(){
        return this.serverUrl;
    }

    public getEnv(){
        return this.env
    }
    public getIsProduction(){
        return this.env == "production";
    }

}

const config = Config.getInstance();

export default config;
