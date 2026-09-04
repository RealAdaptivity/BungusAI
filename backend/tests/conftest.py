"""Pytest configuration and fixtures"""

import pytest
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture
def app():
    """Lazy load app to avoid import issues during test discovery"""
    from app import app as fastapi_app
    return fastapi_app


@pytest.fixture
def client(app):
    """Create a test client"""
    from fastapi.testclient import TestClient
    return TestClient(app)


@pytest.fixture
def sample_message():
    """Sample chat message for testing"""
    return {
        "message": "Hello, how are you?",
        "conversation_id": "test-conversation-123"
    }
