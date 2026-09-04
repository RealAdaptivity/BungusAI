"""Pytest configuration and fixtures"""

import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app


@pytest.fixture
def client():
    """Create a test client"""
    return TestClient(app)


@pytest.fixture
def sample_message():
    """Sample chat message for testing"""
    return {
        "message": "Hello, how are you?",
        "conversation_id": "test-conversation-123"
    }
