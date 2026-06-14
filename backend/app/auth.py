from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from keycloak import KeycloakOpenID

from app.config import settings

_bearer = HTTPBearer()

_keycloak = KeycloakOpenID(
    server_url=settings.keycloak_url,
    realm_name=settings.keycloak_realm,
    client_id=settings.keycloak_client_id,
    client_secret_key=settings.keycloak_client_secret,
)


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(_bearer)) -> dict:
    token = credentials.credentials
    try:
        user_info = _keycloak.introspect(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate token")

    if not user_info.get("active"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is inactive or expired")

    return user_info
