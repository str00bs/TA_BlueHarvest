"""File contains responses for the '/transactions' endpoint router"""

from fastapi import status

from api.schema.transactions import TransactionsList, TransactionsSchema

from .generic import GenericResponses


class TransactionsResponses:
    """Class contains transactions responses"""

    options = {
        status.HTTP_200_OK: {
            "content": None,
            "description": "Transactions router options successfully retrieved",
            "headers": {
                "allow": {
                    "description": "Allowed methods for the Transactions router",
                    "type": "List[string]",
                }
            },
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    # ? CRUD responses
    create = {
        status.HTTP_201_CREATED: {
            "model": TransactionsSchema,
            "description": "Transactions successfully created",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
        **GenericResponses.conflict,
    }

    retrieve = {
        status.HTTP_200_OK: {
            "model": TransactionsSchema,
            "description": "Transactions successfully retrieved",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    listed = {
        status.HTTP_200_OK: {
            "model": TransactionsList,
            "description": "TransactionsList successfully retrieved",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }
