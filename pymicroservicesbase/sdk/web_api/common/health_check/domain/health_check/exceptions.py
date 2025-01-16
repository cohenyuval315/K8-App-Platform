from ...core_api.errors.web_service_error import WebServiceError


class HealthCheckDoesNotExistsError(WebServiceError):
    pass


class HealthCheckAlreadyRunningError(WebServiceError):
    pass
