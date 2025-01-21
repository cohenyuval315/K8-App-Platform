class SessionKeyManager:

    @classmethod
    def get_user_sessions_key(cls, user_id: str) -> str:
        return f"{user_id}:sessions"

    @classmethod
    def get_product_sessions_key(cls, product_id: str) -> str:
        return f"{product_id}:sessions"
