"""getabstract tap class."""

from typing import List
from singer_sdk import Tap, Stream
from singer_sdk import typing as th

from tap_getabstract.streams import (
    Summaries,
)

PLUGIN_NAME = "tap-getabstract"

STREAM_TYPES = [
    Summaries,
]


class TapGetabstract(Tap):
    """getabstract tap class."""

    name = "tap-getabstract"
    config_jsonschema = th.PropertiesList(
        th.Property("client_id", th.StringType, required=True, description="Client ID"),
        th.Property(
            "client_secret", th.StringType, required=True, description="Client Secret"
        ),
        th.Property("language", th.StringType, required=True, description="Language"),
        th.Property(
            "active_only",
            th.StringType,
            required=True,
            description="Only active records",
        ),
        th.Property("page_size", th.StringType, required=True, description="Page size"),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        streams = [stream_class(tap=self) for stream_class in STREAM_TYPES]

        return streams


# CLI Execution:
cli = TapGetabstract.cli
