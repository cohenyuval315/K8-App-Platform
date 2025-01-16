## Overview

Pymicroservicesbase is a modular and configurable microservices architecture that I’ve been building in my free time. It’s not perfect, and some parts are still a work-in-progress, but it’s a project I’ve enjoyed working on to learn, experiment, and improve my skills. This architecture is designed to be flexible, and while it’s functional, it’s primarily a demo and learning experience for now.

The project demonstrates the use of modular microservices, an API Gateway, and an SDK to handle various tasks. it’s a fun and ongoing exploration of building distributed systems.


## Table of Contents

- [Introduction](#introduction)
- [Services Overview](#services-overview)
  - [User Service](#user-service)
  - [Authentication Service](#authentication-service)
  - [API Gateway Service](#api-gateway-service)
- [SDKs](#sdk--web-api)
  - [web api]()
  - [sql]()
  - [cache]()
- [Demo product](#demo-product)
- [Installation & Setup](#installation--setup)


## Introduction

This microservices architecture provides a foundation for building highly decoupled, generic microservices that are flexible to integrate into any type of system, while maintaining a strict scope of responsibility per service. Built with Python for fast development, it uses a sdks to share common building blocks across services.


## Services Overview


### Service Structure: (Domain Driven Design):
```
  /{{service}}/                   # Root directory for the service
      /api/                       # Contains internal API definitions and configurations
          /controllers/           # Functions that handle API request processing with dependency injection
          /routes/                # All route definitions for the API

      /application/               # Contains interfaces and application-specific logic
          /commands/              # Defines actions to be performed with their respective interfaces
          ...

      /domain/                    # Contains core business logic for the service
          /{{service}}/           # Service-specific domain models and business logic
          ...                      # Other business-related components

  app.py                          # Main application entry point
  logger.py                       # Logging utility for the service
  README.md                       # Documentation for the service
```


### 🧑‍🤝‍🧑 **User Service**



The **User Service**  is designed to handle all user-related operations, providing endpoints for retrieving, creating, managing, and deleting users. For more details, refer to the [User Service Documentation](pymicroservicesbase/services/authentication_service/README.md).


---

### 🪪 **Authentication Service**

The Authentication Service is responsible for handling user authentication. It provides mechanisms for verifying user identity but does not manage access permissions. For more details, refer to the .
[Authentication Service Documentation](pymicroservicesbase/services/authentication_service/README.md)


### 🌐 **API Gateway Service**

The **API Gateway Service**  acts as an internal service that serves as a single entry point for all requests, routing traffic to the appropriate microservice, while it centralizing key functions. For more details, refer to the [API Gateway Service Documentation](pymicroservicesbase/services/api_gateway_service/README.md).


---

## SDKs:

### web api
The Web API is built using FastAPI and designed to be a unified service builder, offering easily extendable features and ready-to-use build variants. Adhering to the latest best practices, PEP standards, and utilizing a well-structured `pyproject.toml`, this setup streamlines the Web API build process with many configurable options for seamless integration.

### SQL:
The SQL Delegator handles the main database operations and provides a single entry point for these tasks. It is designed to follow best practices for reliable and efficient database interaction.
- Built in alignment with SQLAlchemy documentation and best practices.
- Ensures no race conditions during database operations.
-  Utilizes asynchronous session context variables for improved performance.
- Flexible design, making it suitable for use in various contexts.
- Robust transaction management for maintaining data consistency.


### Cache
A comprehensive structure for managing all caching operations, designed to decouple the caching logic from the specific cache service being used. Includes thorough test coverage to ensure reliability.


### Service Internal
A singleton connection pool using an httpx asynchronous client, designed to handle direct communication with other microservices. It also includes ready-to-use clients for common microservices.


# Demo Product
Essentially an admin dashboard, this project does not require a specialized backend. It is built with the latest technologies, including Next.js with the App Router and TypeScript. Features include user sessions, data management, and server-side rendering.

The UI is styled using Tailwind CSS, designed with the help of
ChatGPT  ¯\_(ツ)_/¯





## Installation & Setup
    Currently, the project only runs in development mode. Some files are experimental or meant for testing purposes, and the setup is not yet optimized for production.

### Prerequisites:
- Docker (for containerization)

To get started with this project, follow these simple steps to get the project up and running locally.


#### run demo nextjs:
```
./tools/scripts/products/ui/dev.sh demo_product/frontend/web/client
```

#### run demo microservices:
```
./tools/scripts/web_service/dev.sh user_service
./tools/scripts/web_service/dev.sh authentication_service
./tools/scripts/web_service/dev.sh api_gateway_service
./tools/scripts/services/redis.sh
./tools/scripts/services/postgres.sh

```


### Devtools:
  - `docker` and `docker compose`
  - `pre-commit` - via /tools/scripts/commit.sh
  - `.devcontainer` - via `vscode`
  - `ruff`
  - `black`
  - `isort`
  - `git`
  - etc
  - ...
