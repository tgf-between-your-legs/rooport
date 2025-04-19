# Example: User Login Sequence

This example shows a sequence diagram detailing the user login process.

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant WebServer
    participant AuthService
    participant UserDB

    User->>Browser: Enters credentials & Clicks Login
    activate Browser
    Browser->>WebServer: POST /login (username, password)
    activate WebServer
    WebServer->>AuthService: ValidateCredentials(username, password)
    activate AuthService
    AuthService->>UserDB: FindUser(username)
    activate UserDB
    UserDB-->>AuthService: UserRecord (hashedPassword)
    deactivate UserDB
    alt Credentials Valid
        AuthService-->>WebServer: Auth Token
    else Credentials Invalid
        AuthService-->>WebServer: Authentication Failure
    end
    deactivate AuthService
    alt Authentication Success
        WebServer-->>Browser: Set Cookie (Auth Token) & Redirect to Dashboard
    else Authentication Failure
        WebServer-->>Browser: Show Login Error
    end
    deactivate WebServer
    Browser-->>User: Display Dashboard / Error Message
    deactivate Browser