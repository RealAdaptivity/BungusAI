"""Tests for vision endpoints"""

import pytest


def test_analyze_image(client):
    """Test image analysis"""
    response = client.post(
        "/api/v1/vision/analyze",
        json={
            "image_url": "https://example.com/image.jpg",
            "analysis_type": "general"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "analysis" in data


def test_detect_objects(client):
    """Test object detection"""
    response = client.post(
        "/api/v1/vision/detect",
        json={
            "image_url": "https://example.com/image.jpg",
            "confidence_threshold": 0.5
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "detections" in data


def test_extract_text_ocr(client):
    """Test OCR text extraction"""
    response = client.post(
        "/api/v1/vision/ocr",
        json={"image_url": "https://example.com/image.jpg"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "text" in data
