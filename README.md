# Authentiraptor

Authentiraptor is a conceptual copy of OAuth2. This is made for understanding purposes, and is probably far from perfect.

To make a adequate prototype, I need the four main components present in OAuth2 operations.
- Client: The system that wants to access a protected resource 
- Authorization-server: The server that delivers token with user's consent
- Resource-owner: The user or system that owns the resource. We need it's consent to let their resource be accesed 
- Resource-server: The system that holds the protected resource


Access Token Example
```
{
  "iss": "https://my-domain.auth0.com/",
  "sub": "auth0|123456",
  "aud": [
    "https://example.com/health-api",
    "https://my-domain.auth0.com/userinfo"
  ],
  "azp": "my_client_id",
  "exp": 1311281970,
  "iat": 1311280970,
  "scope": "openid profile read:patients read:admin"
}
```

