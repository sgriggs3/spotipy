# -*- coding: utf-8 -*-

""" Shows a user's playlists (need to be authenticated via oauth) """

__all__ = ["CLIENT_CREDS_ENV_VARS"]

import logging

LOGGER = logging.getLogger(__name__)

CLIENT_CREDS_ENV_VARS = {
    "client_id": "SPOTIPY_CLIENT_ID",
    "client_secret": "SPOTIPY_CLIENT_SECRET",
    "client_username": "SPOTIPY_CLIENT_USERNAME",
    "redirect_uri": "SPOTIPY_REDIRECT_URI",
}


def get_host_port(netloc):
    if ":" in netloc:
        host, port = netloc.split(":", 1)
        port = int(port)
    else:
        host = netloc
        port = None

    return host, port


def normalize_scope(scope):
    if scope:
        if isinstance(scope, str):
            scopes = scope.split(',')
        elif isinstance(scope, list) or isinstance(scope, tuple):
            scopes = scope
        else:
            raise Exception(
                "Unsupported scope value, please either provide a list of scopes, "
                "or a string of scopes separated by commas"
            )
        return " ".join(sorted(scopes))
    else:
        return None