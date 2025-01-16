from pymicroservicesbase.shared.errors.base_error import BaseError

# from sqlalchemy.exc import


class BaseDatabaseError(BaseError):
    pass


class DatabaseError(BaseDatabaseError):
    pass


class SessionAlreadyExistsInAsyncContextError(BaseDatabaseError):
    pass


class NotConfiguratedSQLDelegatorError(BaseDatabaseError):
    pass


class AlreadyConfiguredSQLDelegatorError(BaseDatabaseError):
    pass
