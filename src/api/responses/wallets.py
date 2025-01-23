"""File contains responses for the '/wallets' endpoint router"""

from fastapi import status

from api.schema.wallets import WalletsList, WalletsSchema

from .generic import GenericResponses


class WalletsResponses:
    """Class contains wallets responses"""

    options = {
        status.HTTP_200_OK: {
            "content": None,
            "description": "Wallets router options successfully retrieved",
            "headers": {
                "allow": {
                    "description": "Allowed methods for the Wallets router",
                    "type": "List[string]",
                }
            },
        },
        **GenericResponses.unauthorized,
        **GenericResponses.not_found,
        **GenericResponses.server_error,
    }

    retrieve = {
        status.HTTP_200_OK: {
            "model": WalletsSchema,
            "description": "Wallets successfully retrieved",
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
            "model": WalletsList,
            "description": "WalletsList successfully retrieved",
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

    create = {
        status.HTTP_201_CREATED: {
            "model": WalletsSchema,
            "description": "Wallets successfully created",
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

    delete = {
        status.HTTP_204_NO_CONTENT: {
            "content": None,
            "description": "Wallets successfully deleted",
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
