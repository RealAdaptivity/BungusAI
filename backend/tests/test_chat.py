"""Tests for chat/conversation endpoints"""

import pytest


def test_send_message(client, sample_message):
    """Test sending a message"""
    response = client.post("/api/v1/chat", json=sample_message)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "response" in data


def test_send_message_empty(client):
    """Test sending empty message"""
    response = client.post(
        "/api/v1/chat",
        json={"message": "", "conversation_id": "test-123"}
    )
    # Should either succeed with empty response or fail with validation error
    assert response.status_code in [200, 422]


def test_get_conversation_history(client, sample_message):
    """Test getting conversation history"""
    # First send a message
    client.post("/api/v1/chat", json=sample_message)

    # Then get history
    conv_id = sample_message["conversation_id"]
    response = client.get(f"/api/v1/conversation/{conv_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "history" in data


def test_clear_conversation(client, sample_message):
    """Test clearing conversation"""
    # First send a message
    client.post("/api/v1/chat", json=sample_message)

    # Then clear it
    conv_id = sample_message["conversation_id"]
    response = client.delete(f"/api/v1/conversation/{conv_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
