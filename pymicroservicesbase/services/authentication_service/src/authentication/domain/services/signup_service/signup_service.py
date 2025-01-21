from pymicroservicesbase.sdk.web_api.core_api.errors.web_service_error import (
    WebServiceError,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.commands.register.register_command import (
    RegisterCommand,
)
from pymicroservicesbase.services.authentication_service.src.authentication.application.responses.register_responses import (
    RegisterResponseModel,
)
from pymicroservicesbase.services.authentication_service.logger import logger


class SignupService:
    def __init__(self, user_service):
        self.user_service = user_service
        self.register_method_handlers = {
            "instant": self.register_user,
        }

    async def signup(self, command: RegisterCommand):
        try:

            handler = self.register_method_handlers[command.register_method]
            response = await handler(command=command)
            return response
        except KeyError:
            raise WebServiceError(
                error_message=f"invalid register method = {command.register_method}",
                error_code=400,
            )

    async def register_user(
        self, command: RegisterCommand
    ) -> RegisterResponseModel:
        params = {
            "view_type": "admin",
        }
        if len(command.username) == 0:
            command.username = command.email
        register_data = command.model_dump(
            exclude=["response", "request", "register_method"]  # type: ignore
        )

        response = await self.user_service.create_user(
            data=register_data, params=params
        )
        result = response.json()
        try:
            response.raise_for_status()
        except Exception as e:
            logger.error(e)
            raise WebServiceError(
                error_code=response.status_code,
                error=e,
                errors=WebServiceError.unpack(result),
            ) from e
        else:
            data = result["data"]
            logger.debug(data)

        return RegisterResponseModel(message="User successfuly registered")
