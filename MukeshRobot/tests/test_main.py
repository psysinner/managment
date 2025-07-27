import pytest
from unittest.mock import patch

@patch('telegram.ext.Updater')
@patch('telegram.Bot')
def test_example(mock_bot, mock_updater):
    import MukeshRobot
    assert 1 == 1
