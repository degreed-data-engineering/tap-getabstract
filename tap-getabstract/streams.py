"""Stream class for tap-workday."""

import logging
from typing import cast, Dict, Optional, Any, Iterable
from pathlib import Path
from singer_sdk import typing as th
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import APIAuthenticatorBase, OAuthAuthenticator

logging.basicConfig(level=logging.INFO)

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class GetabstractOAuthAuthenticator(OAuthAuthenticator):
    @property
    def oauth_request_body(self) -> dict:
        return {
            "grant_type": "client_credentials",
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
        }


class TapGetabstractStream(RESTStream):
    """Getabstract stream class."""

    url_base = "https://www.getabstract.com/api"

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = super().get_url_params(context, next_page_token)
        params["psize"] = self.config["page_size"]
        params["activeOnly"] = self.config["active_only"]
        params["language"] = self.config["language"]
        return params

    @property
    def authenticator(self) -> APIAuthenticatorBase:
        return GetabstractOAuthAuthenticator(
            stream=self,
            auth_endpoint=f"https://www.getabstract.com/api/oauth/token",
        )


class Summaries(TapGetabstractStream):
    name = "summaries"  # Stream name
    path = "/library/v2/summaries"  # API endpoint after base_url
    primary_keys = ["id"]

    schema = th.PropertiesList().to_dict()
