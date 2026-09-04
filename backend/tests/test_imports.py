"""Test that all modules can be imported"""

import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_config_imports():
    """Test config module imports"""
    from config.settings import settings
    assert settings.APP_NAME == "BungusAI"


def test_ai_modules_import():
    """Test all AI modules can be imported"""
    from ai_core.conversation.chat_manager import ChatManager
    from ai_core.vision.vision_processor import VisionProcessor
    from ai_core.nlp.nlp_engine import NLPEngine
    from ai_core.prediction.prediction_engine import PredictionEngine
    from ai_core.gaming.game_engine import GameEngine

    assert ChatManager is not None
    assert VisionProcessor is not None
    assert NLPEngine is not None
    assert PredictionEngine is not None
    assert GameEngine is not None
