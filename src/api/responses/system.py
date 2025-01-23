"""File contains responses for the system endpoint router"""
from fastapi import status
from fastapi.responses import HTMLResponse

from .generic import GenericResponses


class SystemResponses:
    """Class contains system responses"""

    index = {
        status.HTTP_200_OK: {
            "description": "HTML resource successfully served by the system",
            "headers": {
                "content-length": {
                    "description": "Content Length",
                    "type": "int",
                },
                "date": {"description": "Response Date", "type": "Datetime"},
                "server": {"description": "API Server", "type": "string"},
            },
        },
        **GenericResponses.not_found,
        **GenericResponses.server_error,
        **GenericResponses.unauthorized,
    }
