# Example Diagrams

This file contains examples of well-structured Mermaid diagrams relevant to this project, illustrating the use of the `diagram-style-guide.md`.

## Example 1: High-Level System Architecture (C4 Context)

```mermaid
C4Context
  title System Context for Online Store

  Person(customer, "Customer", "Uses the website to buy products")
  System(webApp, "Web Application", "Allows customers to browse and purchase products")
  System_Ext(paymentGateway, "Payment Gateway", "Processes credit card payments")
  System_Ext(emailService, "Email Service", "Sends order confirmations")
  SystemDb(productDb, "Product Database", "Stores product catalog and inventory")
  SystemDb(orderDb, "Order Database", "Stores customer orders")

  Rel(customer, webApp, "Browses products and places orders using")
  Rel_R(webApp, customer, "Shows product info and order status to")
  Rel(webApp, paymentGateway, "Processes payments using")
  Rel(webApp, emailService, "Sends order confirmation emails via")
  Rel(webApp, productDb, "Reads product information from")
  Rel(webApp, orderDb, "Writes order details to")
```

## Example 2: User Login Sequence

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
```

*(Add more relevant examples for different diagram types used in the project.)*