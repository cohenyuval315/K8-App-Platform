class IdentityService:
    async def whoami(self, command):
        user_session = await self.verify_active_session(command.request)
        user_response = await self.user_service.get_user(user_session.user_id)
        if user_response.status_code != 200:
            raise WebServiceError(
                error_code=500,
                error_message="user does not exists ,but does exists in active session",
            )

        content = user_response.json()
        return JSONResponse(status_code=200, content=content)

    async def get_user_identity(self, command):
        pass
