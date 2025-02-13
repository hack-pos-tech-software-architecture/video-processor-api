from flask_jwt_extended import create_access_token

from ports.access_token import AccessTokenInterface


class AccessTokenJWT(AccessTokenInterface):

    def generate_token(self, payload: any) -> str:
        return create_access_token(identity=payload)

    def refresh_token(self, payload: any) -> str:
        raise NotImplementedError
