# Example: High-Level System Architecture (C4 Context)

This example shows a C4 Context diagram for a simple online store.

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