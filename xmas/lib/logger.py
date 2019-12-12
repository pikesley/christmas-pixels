
import logging

LOGGER = logging.getLogger('christmas-pixels')
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(logging.StreamHandler())


def disable():
    """Switch logging off because it messes up the test output."""
    LOGGER.setLevel(logging.CRITICAL)
