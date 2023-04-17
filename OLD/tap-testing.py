from singer_sdk.testing import get_tap_test_class

from tap import TapGetabstract

SAMPLE_CONFIG = {
    "client_id": "libraryapi-client-degreed-demo",
    "client_secret": "EBA4F7D7B76E2D864E9A",
    "language": "en",
    "active_only": "true",
    "page_size": "50",
}


# Run standard built-in tap tests from the SDK:
TestTapExample = get_tap_test_class(tap_class=TapGetabstract, config=SAMPLE_CONFIG)
