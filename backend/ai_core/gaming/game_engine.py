"""
Game Engine - Handles game AI and game logic
"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime
import uuid
import random

logger = logging.getLogger(__name__)


class GameEngine:
    """Manages games and AI game play"""

    def __init__(self):
        """Initialize game engine"""
        self.active_games: Dict[str, Dict] = {}
        self.game_types = ["chess", "tic_tac_toe", "checkers", "20_questions", "word_game"]
        logger.info("Game Engine initialized")

    async def start_game(
        self,
        game_type: str = "chess",
        difficulty: str = "medium"
    ) -> Dict[str, Any]:
        """
        Start a new game

        Args:
            game_type: Type of game (chess, tic_tac_toe, etc.)
            difficulty: Difficulty level (easy, medium, hard)

        Returns:
            Game session information
        """
        try:
            logger.info(f"Starting game: {game_type} (difficulty: {difficulty})")

            if game_type not in self.game_types:
                raise ValueError(f"Unknown game type: {game_type}")

            game_id = str(uuid.uuid4())

            game_session = {
                "game_id": game_id,
                "game_type": game_type,
                "difficulty": difficulty,
                "status": "active",
                "player": "human",
                "ai_opponent": "BungusAI",
                "turn": "human",
                "created_at": datetime.now().isoformat(),
                "board": self._initialize_board(game_type),
                "moves": [],
                "score": {"human": 0, "ai": 0}
            }

            self.active_games[game_id] = game_session
            logger.info(f"Game {game_id} started")

            return game_session

        except Exception as e:
            logger.error(f"Error starting game: {e}")
            raise

    async def make_move(
        self,
        game_id: str,
        move: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Process a player move and generate AI response

        Args:
            game_id: ID of the game
            move: Player's move

        Returns:
            Game state after move
        """
        try:
            logger.info(f"Processing move in game {game_id}")

            if game_id not in self.active_games:
                raise ValueError(f"Game {game_id} not found")

            game = self.active_games[game_id]

            # Validate it's the player's turn
            if game["turn"] != "human":
                raise ValueError("It's not the player's turn")

            # Record player move
            game["moves"].append({
                "player": "human",
                "move": move,
                "timestamp": datetime.now().isoformat()
            })

            # Generate AI move
            ai_move = await self._generate_ai_move(game)

            game["moves"].append({
                "player": "ai",
                "move": ai_move,
                "timestamp": datetime.now().isoformat()
            })

            # Update turn
            game["turn"] = "human"

            # Check game status
            game_status = await self._check_game_status(game)
            if game_status["finished"]:
                game["status"] = "finished"
                game["winner"] = game_status.get("winner")
                game["score"] = game_status.get("score", game["score"])

            return {
                "game_id": game_id,
                "player_move": move,
                "ai_move": ai_move,
                "game_status": game["status"],
                "turn": game["turn"],
                "score": game["score"]
            }

        except Exception as e:
            logger.error(f"Error making move: {e}")
            raise

    async def get_game_state(self, game_id: str) -> Dict[str, Any]:
        """
        Get current game state

        Args:
            game_id: ID of the game

        Returns:
            Game state
        """
        try:
            if game_id not in self.active_games:
                raise ValueError(f"Game {game_id} not found")

            game = self.active_games[game_id]
            return {
                "game_id": game_id,
                "game_type": game["game_type"],
                "status": game["status"],
                "turn": game["turn"],
                "board": game["board"],
                "score": game["score"],
                "moves_count": len(game["moves"])
            }

        except Exception as e:
            logger.error(f"Error getting game state: {e}")
            raise

    async def resign_game(self, game_id: str) -> Dict[str, Any]:
        """
        Resign from a game

        Args:
            game_id: ID of the game

        Returns:
            Game result
        """
        try:
            if game_id not in self.active_games:
                raise ValueError(f"Game {game_id} not found")

            game = self.active_games[game_id]
            game["status"] = "finished"
            game["winner"] = "ai"

            return {
                "game_id": game_id,
                "status": "resigned",
                "winner": "ai"
            }

        except Exception as e:
            logger.error(f"Error resigning game: {e}")
            raise

    def _initialize_board(self, game_type: str) -> Dict[str, Any]:
        """Initialize game board based on game type"""
        if game_type == "tic_tac_toe":
            return {
                "size": 3,
                "board": [[None, None, None], [None, None, None], [None, None, None]]
            }
        elif game_type == "chess":
            return {
                "size": 8,
                "pieces": "standard_setup"
            }
        else:
            return {"type": game_type, "initialized": True}

    async def _generate_ai_move(self, game: Dict) -> Dict[str, Any]:
        """Generate AI move based on game type and difficulty"""
        game_type = game["game_type"]
        difficulty = game["difficulty"]

        # Simulate AI move generation
        ai_move = {
            "type": "move",
            "position": [random.randint(0, 7), random.randint(0, 7)],
            "reasoning": f"AI move generated with {difficulty} difficulty"
        }

        return ai_move

    async def _check_game_status(self, game: Dict) -> Dict[str, Any]:
        """Check if game is finished and determine winner"""
        # Simulate game status check
        finished = len(game["moves"]) >= 10  # Example condition
        winner = "ai" if finished and random.random() > 0.5 else None

        return {
            "finished": finished,
            "winner": winner,
            "score": game["score"]
        }

    async def list_active_games(self) -> Dict[str, Any]:
        """Get list of all active games"""
        try:
            games_list = [
                {
                    "game_id": game_id,
                    "game_type": game["game_type"],
                    "status": game["status"],
                    "player": game["player"],
                    "created_at": game["created_at"]
                }
                for game_id, game in self.active_games.items()
            ]

            return {
                "active_games": games_list,
                "total_games": len(self.active_games)
            }

        except Exception as e:
            logger.error(f"Error listing games: {e}")
            raise

    async def get_game_statistics(self, game_id: str) -> Dict[str, Any]:
        """Get statistics for a specific game"""
        try:
            if game_id not in self.active_games:
                raise ValueError(f"Game {game_id} not found")

            game = self.active_games[game_id]

            return {
                "game_id": game_id,
                "total_moves": len(game["moves"]),
                "player_moves": len([m for m in game["moves"] if m["player"] == "human"]),
                "ai_moves": len([m for m in game["moves"] if m["player"] == "ai"]),
                "duration_seconds": 0,  # Calculate from created_at
                "score": game["score"],
                "status": game["status"]
            }

        except Exception as e:
            logger.error(f"Error getting game statistics: {e}")
            raise
