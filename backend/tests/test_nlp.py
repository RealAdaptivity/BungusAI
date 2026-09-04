"""Tests for NLP endpoints"""

import pytest


def test_analyze_text(client):
    """Test text analysis"""
    response = client.post(
        "/api/v1/nlp/analyze",
        json={"text": "This is a sample text for analysis."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "analysis" in data


def test_sentiment_analysis(client):
    """Test sentiment analysis"""
    response = client.post(
        "/api/v1/nlp/sentiment",
        json={"text": "I love this product! It's amazing!"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "sentiment" in data


def test_extract_entities(client):
    """Test entity extraction"""
    response = client.post(
        "/api/v1/nlp/entities",
        json={"text": "John Smith works at Google in New York."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "entities" in data
