from pydantic_settings import BaseSettings


class BaseAppConfig(BaseSettings):
    APP_NAME: str
    APP_DESCRIPTION: str
    VERSION: str
    SUMMARY: str


# from pydantic import BaseSettings, Field

# class BaseAppConfig(BaseSettings):
#     APP_NAME: str = Field(
#         default=...,
#         alias="app_name",
#         title="Application Name",
#         description="The name of the application."
#     )
#     APP_DESCRIPTION: str = Field(
#         default=...,
#         alias="app_description",
#         title="Application Description",
#         description="A brief description of the application's purpose or functionality."
#     )
#     VERSION: str = Field(
#         default=...,
#         alias="version",
#         title="Application Version",
#         description="The version of the application, typically following semantic versioning."
#     )
#     SUMMARY: str = Field(
#         default=...,
#         alias="summary",
#         title="Application Summary",
#         description="A short summary providing an overview of the application."
#     )
