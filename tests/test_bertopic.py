# Basic tests for BERTopic
# This is a placeholder for the actual test_bertopic.py file

import pytest
from bertopic import BERTopic

def test_bertopic_init():
    """Test initializing BERTopic."""
    model = BERTopic()
    assert isinstance(model, BERTopic)