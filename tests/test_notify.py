"""Unit test for module."""

from unittest.mock import patch

from notifier import notify


@patch("os.system")
def test_notify(mock_system):
    """Run unit test on notify."""
    notify(title="Test title", message="Test message")
    mock_system.assert_called()
