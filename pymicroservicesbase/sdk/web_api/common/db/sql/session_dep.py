from pymicroservicesbase.sdk.sql.sql_delegator import SQLDelegator

# def _get_sync_session():
#     with create_session(scoped=False) as session:
#         yield session


# async def _get_async_session():
#     async with create_session() as session:
#         yield session


# SyncSessionDep = Annotated[Session, Depends(_get_sync_session)]

# AsyncSessionDep = Annotated[AsyncSession, Depends(_get_async_session)]

# def _get_session_dep(is_async:bool = True):
#     return AsyncSessionDep

# SessionDep = _get_session_dep()


def SessionDep(sql_delegator: SQLDelegator, is_async: bool = True):
    # def _get_sync_session():
    #     with sql_delegator.session(scoped=False) as session:
    #         yield session

    async def _get_async_session():
        async with sql_delegator.session() as session:
            yield session

    if is_async:
        return _get_async_session
