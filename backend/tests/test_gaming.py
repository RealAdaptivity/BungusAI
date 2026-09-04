"""Tests for gaming endpoints"""

import pytest


def test_start_game(client):
    """Test starting a game"""
    response = client.post(
        "/api/v1/game/start",
        json={
            "game_type": "chess",
            "difficulty": "medium"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "game" in data
    assert "game_id" in data["game"]


def test_start_game_invalid_type(client):
    """Test starting game with invalid type"""
    response = client.post(
        "/api/v1/game/start",
        json={
            "game_type": "invalid_game",
            "difficulty": "easy"
        }
    )
    assert response.status_code == 500


def test_make_game_move(client):
    """Test making a game move"""
    # First start a game
    start_response = client.post(
        "/api/v1/game/start",
        json={"game_type": "tic_tac_toe", "difficulty": "easy"}
    )
    game_id = start_response.json()["game"]["game_id"]

    # Then make a move
    response = client.post(
        f"/api/v1/game/{game_id}/move",
        json={"move": {"x": 0, "y": 0}}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "result" in data


def test_get_game_state(client):
    """Test getting game state"""
    # First start a game
    start_response = client.post(
        "/api/v1/game/start",
        json={"game_type": "chess", "difficulty": "medium"}
    )
    game_id = start_response.json()["game"]["game_id"]

    # Then get state
    response = client.get(f"/api/v1/game/{game_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "state" in data
