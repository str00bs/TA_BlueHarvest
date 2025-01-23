# TA BlueHarvest
Implementation for the technical assignment from BlueHarvest

## Notes
A few notable things have been omitted as it's not specified by the assignment:
- Wallet <-> Transaction logic (i.e. Transfer of funds, no-overdrafting, is funds available?)
- Polymorphic relationships (i.e. so you can do account.wallets.transactions)
  - Eager-loading of account.wallets and account.transactions
- A bunch of error details, though some have been added for display purposes.
- Regression (unit) tests for all endpoints (Pytest fixtures are not necessary for this)

## Setup
Run:
1. Copy ENV: `cp dist.env .env`
2. Run docker: `docker-compose up -d`
3. Open `0.0.0.0:80` in a web-browser


## Default Endpoints
The following default endpoints are provided by FastAPI and exposed by the template
- Front-End: `/`
- Swagger UI: `/docs`
- ReDoc Documentation: `/redoc`
- OpenAPI 3.0: `/openapi.json`


## Resources
Resources provided for the repository and application.

### General
General resources already provided for/with the application & repository.
- IDE Configurations: [VSCode](resources/vscode)
- Debugging & Testing:
  - [Static Analysis Requirements](resources/requirements/analysis.txt)
  - [Unit Testing Requirements](resources/requirements/testing.txt)
  - [Security Scanning Requirements](resources/requirements/security.txt)
- Deployment Tools:
  - Dockerfile: [Dockerfile](Dockerfile)

### SDK Docs
- API Framework: [FastAPI](https://fastapi.tiangolo.com/)
  - Parent: [Starlette](https://www.starlette.io/)
  - Auth: [FastAPI Azure Auth](https://github.com/Intility/fastapi-azure-auth)
  - Schema: [Pydantic](https://pydantic-docs.helpmanual.io/)
- Testing:
  - Runner: [Pytest](https://docs.pytest.org/en/6.2.x/)
  - Async: [aiounittest](https://pypi.org/project/aiounittest/)
- Database
  - ORM: [Masonite ORM](https://orm.masoniteproject.com/)
  - _Formerly known as/continuation of: [Orator](https://orator-orm.com/)_
- Validation & Settings
  - [Pydantic Settings](https://pydantic-docs.helpmanual.io/usage/settings/)
