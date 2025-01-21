from datetime import timedelta
from json import JSONEncoder
from typing import Dict, Iterable, List, Literal, Sequence

import jwt
from pydantic import ConfigDict, Field

from pymicroservicesbase.sdk.web_api.core_api.base_model import BaseModel
from pymicroservicesbase.utils.tokens.base_token_factory import (
    BaseTokenFactory,
)
from pymicroservicesbase.utils.datetime_utils.datetime import utcnow
from pymicroservicesbase.utils.id.generate_id import generate_id

JWTAlgorithmType = Literal[
    "HS256",  # HMAC with SHA-256, Required
    "HS384",  # HMAC with SHA-384, Optional
    "HS512",  # HMAC with SHA-512, Optional
    "RS256",  # RSASSA-PKCS1-v1_5 using SHA-256, Recommended
    "RS384",  # RSASSA-PKCS1-v1_5 using SHA-384, Optional
    "RS512",  # RSASSA-PKCS1-v1_5 using SHA-512, Optional
    "ES256",  # ECDSA using P-256 and SHA-256, Recommended+
    "ES384",  # ECDSA using P-384 and SHA-384, Optional
    "ES512",  # ECDSA with SHA-512, Optional
    "PS256",  # SASSA-PSS using SHA-256 and MGF1 with SHA-256, Optional
    "PS384",  # RSASSA-PSS using SHA-384 and MGF1 with SHA-384, Optional
    "PS512",  # RSASSA-PSS using SHA-512 and MGF1 with SHA-512 , Optional
    "none",  # No digital signature or MAC performed, Optional
]

JOSEType = Literal["JOSE", "JWT", "JWS", "JWE"]

JOSEContentType = JOSEType | Literal["Opaque"]


class JOSEHeader(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        arbitrary_types_allowed=False,
        extra="allow",
    )

    jose_type: JOSEType | None = Field(
        default=None,
        title="Type of the Token",
        description="Type of the token (e.g., 'JWT', 'JWS', 'JWE', etc.). usually JWT",
        alias="typ",
    )

    content_type: JOSEContentType | None = Field(
        default=None,
        title="Content type",
        description="Content type; used to indicate the payload is also a token type.",
        alias="cty",
    )

    algorithm: JWTAlgorithmType | None = Field(
        title="algorithm to use on the token",
        description="Algorithm used",
        alias="alg",
    )

    key_id: str | None = Field(
        default=None, title="Key ID", description="Key ID", alias="kid"
    )

    encoding: str | None = Field(
        default=None,
        title="encoding",
        description="encoding of the jose header",
        alias="enc",
    )


class JWTDecodeOptions(BaseModel):
    verify_signature: bool | None = Field(
        default=None,
        title="algos in decoding",
        description="Decoding Field, verify",
        alias="verify_signature",
    )
    verify_audience: bool | None = Field(
        default=None,
        title="verify audience",
        description="Decoding Field, verify",
        alias="verify_aud",
    )
    verify_issuer: bool | None = Field(
        title="verify issuer",
        description="Decoding Field, verify",
        alias="verify_iss",
    )
    verify_expire: bool | None = Field(
        default=None,
        title="verify expire",
        description="Decoding Field, verify",
        alias="verify_exp",
    )
    verify_issued_at: bool | None = Field(
        title="verify issued at",
        description="Decoding Field, verify",
        alias="verify_iat",
    )
    verify_not_before: bool | None = Field(
        default=None,
        title="verify not before",
        description="Decoding Field, verify if not before",
        alias="verify_nbf",
    )
    strict_audience: bool | None = Field(
        default=None,
        title="strict audience",
        description="Decoding Field, verify",
        alias="strict_aud",
    )
    required_fields: List[str] | None = Field(
        default=None,
        title="required fields",
        description="Decoding Field, require values to exists in payload",
        alias="require",
    )


class JWTConfig(BaseModel):
    secret_key: str | bytes | None = Field(
        default=None,
        title="secret key",
        description="kid in headers override this",
        alias="key",
    )
    subject: str | None = Field(
        default=None,
        title="subject",
        description="kid in headers override this",
        alias="sub",
    )
    issuer: str | Sequence[str] | None = Field(
        default=None,
        title="issuer",
        description="kid in headers override this",
        alias="iss",
    )
    audience: str | Iterable[str] | None = Field(
        default=None,
        title="audience",
        description="kid in headers override this",
        alias="aud",
    )
    headers: JOSEHeader | None = Field(
        default=None, title="jose headers", description="", alias="headers"
    )
    algorithm: JWTAlgorithmType | None = Field(
        default=None,
        title="alg in jose headers override this",
        description="",
        alias="algorithm",
    )
    algorithms: Sequence[JWTAlgorithmType] | None = Field(
        default=None,
        title="algos in decoding",
        description="Decoding Field",
        alias="algorithms",
    )

    verify: bool | None = Field(
        default=None,
        title="verify",
        description="Decoding Field, verify",
        alias="verify",
    )

    detached_payload: bytes | None = Field(
        default=None,
        title="algos in decoding",
        description="Decoding Field, verify",
        alias="detached_payload",
    )

    leeway: float | timedelta | None = Field(
        default=None,
        title="algos in decoding",
        description="Decoding Field, verify",
        alias="leeway",
    )

    json_encoder: type[JSONEncoder] | None = Field(
        default=None,
        title="algos in decoding",
        description="Decoding Field, verify",
        alias="json_encoder",
    )

    sort_headers: bool | None = Field(
        default=None,
        title="sort headers",
        description="Decoding Field, verify",
        alias="sort_headers",
    )

    decode_options: JWTDecodeOptions | None = Field(
        default=None,
        title="decode option in jwt",
        description="dict of options",
        alias="options",
    )

    verify_signature: bool | None = Field(
        default=None,
        title="algos in decoding",
        description="Decoding Field, verify",
        alias="verify_signature",
    )
    verify_audience: bool | None = Field(
        default=None,
        title="verify audience",
        description="Decoding Field, verify",
        alias="verify_aud",
    )
    verify_issuer: bool | None = Field(
        default=None,
        title="verify issuer",
        description="Decoding Field, verify",
        alias="verify_iss",
    )
    verify_expire: bool | None = Field(
        default=None,
        title="verify expire",
        description="Decoding Field, verify",
        alias="verify_exp",
    )
    verify_issued_at: bool | None = Field(
        default=None,
        title="verify issued at",
        description="Decoding Field, verify",
        alias="verify_iat",
    )
    verify_not_before: bool | None = Field(
        default=None,
        title="verify not before",
        description="Decoding Field, verify if not before",
        alias="verify_nbf",
    )
    strict_audience: bool | None = Field(
        default=None,
        title="strict audience",
        description="Decoding Field, verify",
        alias="strict_aud",
    )
    required_fields: List[str] | None = Field(
        default=None,
        title="require fields",
        description="Decoding Field, require values to exists in payload",
        alias="require",
    )


class JWTTokenFactory(BaseTokenFactory):
    token_type = "Bearer"
    JTI_ID_LENGTH = 36

    def _verify_token(self, token):
        try:
            options = (getattr(self, "options", None),)
            if not isinstance(options, dict):
                options = {}
            _options = {
                "verify_signature": getattr(self, "verify_signature"),
                "require": getattr(self, "require"),
                "verify_aud": getattr(self, "verify_aud", False),
                "verify_iss": getattr(self, "verify_iss", False),
                "verify_exp": getattr(self, "verify_exp"),
                "verify_iat": getattr(self, "verify_iat"),
                "verify_nbf": getattr(self, "verify_nbf"),
                "strict_aud": getattr(self, "strict_aud"),
            }
            options.update(_options)
            decoded = jwt.decode(
                jwt=token,
                key=getattr(self, "key"),
                algorithms=getattr(self, "algorithms"),
                options=options,
                verify=getattr(self, "verify", None),
                subject=getattr(self, "sub", None),
                audience=getattr(self, "aud", None),
                issuer=getattr(self, "iss", None),
                leeway=getattr(self, "leeway"),
            )
            # header = decoded["header"]
            # payload = decoded["payload"]
            # signature = decoded["signature"]
            # self.header = header
            # self.payload = payload
            # self.signature = signature
            return decoded
        except Exception as e:
            raise AttributeError(e)

    def _normalize_leeyway(self, leeyway: float | timedelta):
        if isinstance(leeyway, float):
            return timedelta(seconds=leeyway)
        if isinstance(leeyway, timedelta):
            return leeyway
        else:
            raise ValueError("leeyway must be float or timedelta")

    def _generate_jti(self):
        return generate_id(self.JTI_ID_LENGTH)

    def _normalize_headers(self, headers: JOSEHeader | None):
        if headers is None:
            return None
        _headers = headers.model_dump(
            exclude_none=True, by_alias=True, exclude_unset=True
        )
        return _headers

    def _generate_token(
        self,
        expiration_time_in_seconds: int,
        payload: Dict[str, str],
    ) -> str:
        try:
            jwt_dict = {
                "jti": self._generate_jti(),
                "iat": utcnow(),
                "nbf": utcnow(),
                "exp": utcnow()
                + timedelta(seconds=expiration_time_in_seconds),
            }
            jwt_dict.update(payload.copy())

            if getattr(self, "sub", None) is not None:
                jwt_dict["sub"] = getattr(self, "sub")
            if getattr(self, "iss", None) is not None:
                jwt_dict["iss"] = getattr(self, "iss")
            if getattr(self, "aud", None) is not None:
                jwt_dict["aud"] = getattr(self, "aud")

            token = jwt.encode(
                payload=jwt_dict,
                key=getattr(self, "key"),
                algorithm=getattr(self, "algorithm", None),
                headers=getattr(self, "headers", None),
                sort_headers=getattr(self, "sort_headers"),
                json_encoder=getattr(self, "json_encoder", None),
            )
            return token
        except AttributeError as e:
            raise AttributeError(f"Attribute Error: {e}")

    def _configure(self, jwt_config: JWTConfig | None = None):
        if jwt_config is not None:
            data = jwt_config.model_dump(
                exclude_unset=True,
                by_alias=True,
                exclude_none=False,
                exclude_defaults=False,
            )
            for k, v in data.items():
                if k == "leeway":
                    v = self._normalize_leeyway(v)
                elif k == "options":
                    v = v.model_dump(
                        exclude_unset=True,
                        by_alias=True,
                        exclude_none=False,
                        exclude_defaults=False,
                    )
                setattr(self, k, v)

    # def __configure(
    #     self,
    #     *,
    #     secret_key: str | bytes | None = None,
    #     subject: str | None = None,
    #     issuer: str | Sequence[str] | None = None,
    #     audience: str | Iterable[str] | None = None,
    #     headers: JOSEHeader | None = None,
    #     algorithm: JWTAlgorithmType | None = None,
    #     algorithms: Sequence[JWTAlgorithmType] | None = None,
    #     options: dict[str, Any] | None = None,
    #     verify: bool | None = None,
    #     detached_payload: bytes | None = None,
    #     leeway: float | timedelta = 0,
    #     json_encoder: type[JSONEncoder] | None = None,
    #     sort_headers: bool = True,
    #     verify_signature:bool =True,
    #     verify_aud:bool  = True,
    #     verify_iss:bool  = True,
    #     verify_exp:bool  = True,
    #     verify_iat:bool  = True,
    #     verify_nbf:bool  = True,
    #     strict_aud:bool  = False,
    #     require:List[str]  = ["exp", "iat", "nbf"],

    # ):
    #     self.secret_key = secret_key
    #     self.subject = subject
    #     self.issuer = issuer
    #     self.audience = audience
    #     self.headers = self._normalize_headers(headers)
    #     self.algorithm = algorithm
    #     self.algorithms = algorithms
    #     self.leeway = self._normalize_leeyway(leeway)
    #     self.options = options
    #     self.verify = verify
    #     self.detached_payload = detached_payload
    #     self.json_encoder = json_encoder
    #     self.sort_headers = sort_headers
    #     self.verify_signature = verify_signature
    #     self.verify_aud = verify_aud
    #     self.verify_iss = verify_iss
    #     self.verify_exp = verify_exp
    #     self.verify_iat = verify_iat
    #     self.verify_nbf = verify_nbf
    #     self.strict_aud = strict_aud
    #     self.require = require
