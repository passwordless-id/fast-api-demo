from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OpenIdConnect
import requests

app = FastAPI()

openid = OpenIdConnect(openIdConnectUrl="https://api.passwordless.id/.well-known/openid-configuration")

@app.get("/userinfo")
async def userinfo(authHeader: Annotated[str, Depends(openid)]):
    # The token in `authHeader` is short lived and will expire after a short while
    # Therefore, you should cache the user information and establish a normal user session
    # This also avoids uselessly repating the request each time and is more snappy
    res = requests.get('https://api.passwordless.id/openid/userinfo', headers = {"Authorization":authHeader})
    return res.json()

