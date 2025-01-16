# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)


# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)


import bcrypt


def hash_password(password: str, salt: bytes, encoding="utf-8") -> bytes:
    """_summary_

    Args:
        password (str): _description_
        encoding (str, optional): _description_. Defaults to "utf-8".

    Returns:
        bytes: _description_
    """
    pwd_bytes = password.encode(encoding)
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password


def verify_password(
    plain_password: str, hashed_password: str, encoding="utf-8"
) -> bool:
    """_summary_

    Args:
        plain_password (str): _description_
        hashed_password (bytes): _description_
        encoding (str, optional): _description_. Defaults to "utf-8".

    Returns:
        bool: _description_
    """
    password_byte_enc = plain_password.encode(encoding)
    hashed_password_byte_enc = hashed_password.encode(encoding)
    return bcrypt.checkpw(
        password=password_byte_enc, hashed_password=hashed_password_byte_enc
    )
    # return pwd_context.verify(plain_password, hashed_password)


# Minimum eight characters, at least one letter and one number:
PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

# Minimum eight characters, at least one letter, one number and one special character:
PASSWORD_REGEX = (
    r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
)

# Minimum eight characters, at least one uppercase letter, one lowercase letter and one number:
PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

# Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character:
PASSWORD_REGEX = (
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
)

# Minimum eight and maximum 10 characters, at least one uppercase letter, one lowercase letter, one number and one special character:
PASSWORD_REGEX = (
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,10}$"
)
