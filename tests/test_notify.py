"""Unit test for module."""
import logging
from unittest.mock import patch

from pynotification import builtin_notifier


@patch("os.system")
def test_builtin_notifier(mock_system):
    """Run unit test on builtin_notifier."""
    builtin_notifier(title="Test title", message="Test message")
    mock_system.assert_called()


@patch("os.system")
def test_builtin_notifier_debug(mock_system):
    """Run unit test on builtin_notifier with debug enabled."""
    builtin_notifier(title="Test title", message="Test message", debug=True)
    mock_system.assert_called()


@patch("os.system")
def test_builtin_notifier_logger(mock_system):
    """Run unit test on builtin_notifier with debug enabled."""
    logger = logging.getLogger(__name__)
    builtin_notifier(title="Test title", message="Test message", debug=True, logger=logger)
    mock_system.assert_called()
