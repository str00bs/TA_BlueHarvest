"""File contains generic and shared responses"""
from typing import List

from fastapi import status

from api.schema import MessageSchema


class GenericResponses:
    """Class contains generic and shared responses"""

    # ? 200s
    ok = {
        status.HTTP_200_OK: {
            "model": List[MessageSchema],
            "description": "Successfully processed operation",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        }
    }

    # ? 300s
    redirect = {
        status.HTTP_308_PERMANENT_REDIRECT: {
            "description": "Redirects from index to /docs",
            "headers": {
                "Location": {"description": "Content Length", "type": "int"},
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        }
    }

    # ? 400s
    unauthorized = {
        status.HTTP_401_UNAUTHORIZED: {
            "model": List[MessageSchema],
            "description": "Unauthorized to view requested resource",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        }
    }

    not_found = {
        status.HTTP_404_NOT_FOUND: {
            "model": List[MessageSchema],
            "description": "Could not find requested resource",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
    }

    conflict = {
        status.HTTP_409_CONFLICT: {
            "model": List[MessageSchema],
            "descriptions": "The requested resource already exists!",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        }
    }

    unprocessable = {
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "model": List[MessageSchema],
            "descriptions": "Server could not process entity",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        }
    }

    # ? 500s
    server_error = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": List[MessageSchema],
            "description": "Server could not process request",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
    }
