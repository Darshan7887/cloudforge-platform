from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import requests

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

AUTH_SERVICE_URL = "http://cloudforge-auth:8000/validate-token"

def get_current_email(token: str = Depends(oauth2_scheme)):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
	
	response = requests.get(
    		AUTH_SERVICE_URL,
    		headers=headers,
    		timeout=3
	)
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token validation failed"
            )

        return response.json()["email"]

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Auth service unavailable"
        )
