"""
BungusAI - Main Application Entry Point
Omnipotent AI platform with conversation, vision, NLP, prediction, and gaming capabilities
"""

from fastapi import FastAPI, HTTPException, WebSocket, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging
from typing import Dict
import json

from config.settings import settings
from ai_core.conversation.chat_manager import ChatManager
from ai_core.vision.vision_processor import VisionProcessor
from ai_core.nlp.nlp_engine import NLPEngine
from ai_core.prediction.prediction_engine import PredictionEngine
from ai_core.gaming.game_engine import GameEngine

# Configure logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format=settings.LOG_FORMAT
)
logger = logging.getLogger(__name__)


# Global instances
chat_manager: ChatManager = None
vision_processor: VisionProcessor = None
nlp_engine: NLPEngine = None
prediction_engine: PredictionEngine = None
game_engine: GameEngine = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle management"""
    # Startup
    logger.info("🚀 Starting BungusAI...")
    global chat_manager, vision_processor, nlp_engine, prediction_engine, game_engine

    try:
        chat_manager = ChatManager()
        vision_processor = VisionProcessor()
        nlp_engine = NLPEngine()
        prediction_engine = PredictionEngine()
        game_engine = GameEngine()
        logger.info("✅ All AI engines initialized successfully")
    except Exception as e:
        logger.error(f"❌ Failed to initialize engines: {e}")
        raise

    yield

    # Shutdown
    logger.info("🛑 Shutting down BungusAI...")


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Omnipotent AI Platform - Do Everything",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# Health & Status Endpoints
# ============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
    }


@app.get("/status")
async def status_endpoint():
    """Detailed status of all AI engines"""
    return {
        "status": "operational",
        "engines": {
            "conversation": "ready" if chat_manager else "initializing",
            "vision": "ready" if vision_processor else "initializing",
            "nlp": "ready" if nlp_engine else "initializing",
            "prediction": "ready" if prediction_engine else "initializing",
            "gaming": "ready" if game_engine else "initializing"
        },
        "timestamp": json.dumps({"message": "All systems operational"})
    }


# ============================================================================
# Conversation / Chat Endpoints
# ============================================================================

@app.post("/api/v1/chat")
async def send_message(request: dict):
    """
    Send a message to the AI chatbot

    Request body:
    {
        "conversation_id": "uuid",
        "message": "Your message here",
        "context": {}  # Optional context
    }
    """
    if not chat_manager:
        raise HTTPException(status_code=503, detail="Chat service not available")

    try:
        response = await chat_manager.process_message(
            message=request.get("message"),
            conversation_id=request.get("conversation_id"),
            context=request.get("context", {})
        )
        return {"status": "success", "response": response}
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/conversation/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Get conversation history"""
    if not chat_manager:
        raise HTTPException(status_code=503, detail="Chat service not available")

    try:
        history = await chat_manager.get_history(conversation_id)
        return {"status": "success", "history": history}
    except Exception as e:
        logger.error(f"Error retrieving conversation: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/v1/conversation/{conversation_id}")
async def clear_conversation(conversation_id: str):
    """Clear conversation history"""
    if not chat_manager:
        raise HTTPException(status_code=503, detail="Chat service not available")

    try:
        await chat_manager.clear_conversation(conversation_id)
        return {"status": "success", "message": "Conversation cleared"}
    except Exception as e:
        logger.error(f"Error clearing conversation: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Vision / Image Processing Endpoints
# ============================================================================

@app.post("/api/v1/vision/analyze")
async def analyze_image(request: dict):
    """
    Analyze an image

    Request body:
    {
        "image_url": "url_to_image",
        "analysis_type": "general|detailed|objects"
    }
    """
    if not vision_processor:
        raise HTTPException(status_code=503, detail="Vision service not available")

    try:
        result = await vision_processor.analyze_image(
            image_url=request.get("image_url"),
            analysis_type=request.get("analysis_type", "general")
        )
        return {"status": "success", "analysis": result}
    except Exception as e:
        logger.error(f"Vision analysis error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/v1/vision/detect")
async def detect_objects(request: dict):
    """
    Detect objects in an image

    Request body:
    {
        "image_url": "url_to_image",
        "confidence_threshold": 0.5
    }
    """
    if not vision_processor:
        raise HTTPException(status_code=503, detail="Vision service not available")

    try:
        detections = await vision_processor.detect_objects(
            image_url=request.get("image_url"),
            confidence=request.get("confidence_threshold", 0.5)
        )
        return {"status": "success", "detections": detections}
    except Exception as e:
        logger.error(f"Object detection error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/v1/vision/ocr")
async def extract_text(request: dict):
    """
    Extract text from image (OCR)

    Request body:
    {
        "image_url": "url_to_image"
    }
    """
    if not vision_processor:
        raise HTTPException(status_code=503, detail="Vision service not available")

    try:
        text = await vision_processor.extract_text(
            image_url=request.get("image_url")
        )
        return {"status": "success", "text": text}
    except Exception as e:
        logger.error(f"OCR error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# NLP Endpoints
# ============================================================================

@app.post("/api/v1/nlp/analyze")
async def analyze_text(request: dict):
    """Analyze text"""
    if not nlp_engine:
        raise HTTPException(status_code=503, detail="NLP service not available")

    try:
        analysis = await nlp_engine.analyze_text(request.get("text"))
        return {"status": "success", "analysis": analysis}
    except Exception as e:
        logger.error(f"NLP analysis error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/v1/nlp/sentiment")
async def sentiment_analysis(request: dict):
    """Analyze sentiment of text"""
    if not nlp_engine:
        raise HTTPException(status_code=503, detail="NLP service not available")

    try:
        sentiment = await nlp_engine.analyze_sentiment(request.get("text"))
        return {"status": "success", "sentiment": sentiment}
    except Exception as e:
        logger.error(f"Sentiment analysis error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/v1/nlp/entities")
async def extract_entities(request: dict):
    """Extract named entities from text"""
    if not nlp_engine:
        raise HTTPException(status_code=503, detail="NLP service not available")

    try:
        entities = await nlp_engine.extract_entities(request.get("text"))
        return {"status": "success", "entities": entities}
    except Exception as e:
        logger.error(f"Entity extraction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Prediction / ML Endpoints
# ============================================================================

@app.post("/api/v1/predict")
async def make_prediction(request: dict):
    """Make a prediction using ML models"""
    if not prediction_engine:
        raise HTTPException(status_code=503, detail="Prediction service not available")

    try:
        prediction = await prediction_engine.predict(
            model_name=request.get("model_name"),
            features=request.get("features")
        )
        return {"status": "success", "prediction": prediction}
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/v1/predict/train")
async def train_model(request: dict):
    """Train a new model"""
    if not prediction_engine:
        raise HTTPException(status_code=503, detail="Prediction service not available")

    try:
        result = await prediction_engine.train_model(
            model_name=request.get("model_name"),
            training_data=request.get("training_data")
        )
        return {"status": "success", "result": result}
    except Exception as e:
        logger.error(f"Model training error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/predict/models")
async def list_models():
    """List available prediction models"""
    if not prediction_engine:
        raise HTTPException(status_code=503, detail="Prediction service not available")

    try:
        models = await prediction_engine.list_models()
        return {"status": "success", "models": models}
    except Exception as e:
        logger.error(f"Error listing models: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Gaming Endpoints
# ============================================================================

@app.post("/api/v1/game/start")
async def start_game(request: dict):
    """Start a new game"""
    if not game_engine:
        raise HTTPException(status_code=503, detail="Gaming service not available")

    try:
        game_session = await game_engine.start_game(
            game_type=request.get("game_type"),
            difficulty=request.get("difficulty", "medium")
        )
        return {"status": "success", "game": game_session}
    except Exception as e:
        logger.error(f"Game start error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/v1/game/{game_id}/move")
async def make_game_move(game_id: str, request: dict):
    """Make a move in the game"""
    if not game_engine:
        raise HTTPException(status_code=503, detail="Gaming service not available")

    try:
        result = await game_engine.make_move(
            game_id=game_id,
            move=request.get("move")
        )
        return {"status": "success", "result": result}
    except Exception as e:
        logger.error(f"Game move error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/game/{game_id}")
async def get_game_state(game_id: str):
    """Get current game state"""
    if not game_engine:
        raise HTTPException(status_code=503, detail="Gaming service not available")

    try:
        state = await game_engine.get_game_state(game_id)
        return {"status": "success", "state": state}
    except Exception as e:
        logger.error(f"Error getting game state: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# WebSocket Endpoints (Real-time)
# ============================================================================

@app.websocket("/ws/chat/{conversation_id}")
async def websocket_chat(websocket: WebSocket, conversation_id: str):
    """WebSocket for real-time chat"""
    await websocket.accept()

    if not chat_manager:
        await websocket.close(code=status.WS_1011_SERVER_ERROR)
        return

    try:
        while True:
            data = await websocket.receive_text()
            response = await chat_manager.process_message(
                message=data,
                conversation_id=conversation_id
            )
            await websocket.send_text(json.dumps({
                "type": "response",
                "data": response
            }))
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        await websocket.close(code=status.WS_1011_SERVER_ERROR)


# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Handle general exceptions"""
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


# ============================================================================
# Root Endpoint
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "operational",
        "endpoints": {
            "health": "/health",
            "status": "/status",
            "chat": "/api/v1/chat",
            "vision": "/api/v1/vision",
            "nlp": "/api/v1/nlp",
            "prediction": "/api/v1/predict",
            "gaming": "/api/v1/game"
        }
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
