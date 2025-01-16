from pymicroservicesbase.sdk.web_api.core_api.web_service_container import (
    WebServiceContainer,
)


class WebContext:
    web_service_container: WebServiceContainer | None = None

    @classmethod
    def set_web_context(cls, web_service_container: WebServiceContainer):
        if cls.web_service_container is None:
            cls.web_service_container = web_service_container
        else:
            raise Exception("web service container already exists")

    @classmethod
    def get_web_context(cls) -> WebServiceContainer:
        if cls.web_service_container is None:
            raise Exception("web service container was not defined")
        return cls.web_service_container
