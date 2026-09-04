"""Tests for prediction endpoints"""

import pytest


def test_list_models(client):
    """Test listing available models"""
    response = client.get("/api/v1/predict/models")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "models" in data


def test_make_prediction(client):
    """Test making a prediction"""
    response = client.post(
        "/api/v1/predict",
        json={
            "model_name": "linear_regression",
            "features": {"feature1": 1.0, "feature2": 2.0}
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "prediction" in data


def test_train_model(client):
    """Test model training"""
    response = client.post(
        "/api/v1/predict/train",
        json={
            "model_name": "test_model",
            "training_data": [
                {"feature1": 1.0, "feature2": 2.0, "label": 1},
                {"feature1": 2.0, "feature2": 4.0, "label": 2}
            ]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "result" in data
