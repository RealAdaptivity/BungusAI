# BungusAI - Omnipotent AI Platform

A comprehensive, full-featured AI system capable of handling **everything**: conversational AI, vision/image processing, natural language processing, data analysis/prediction, gaming AI, and much more.

## 🎯 Features

### Core Capabilities
- **Conversational AI** - Context-aware chatbot with Claude API
- **Vision & Image Processing** - Image analysis, OCR, object detection
- **Natural Language Processing** - Text analysis, sentiment analysis, entity extraction
- **Data Analysis & Prediction** - Statistical analysis, ML predictions, forecasting
- **Gaming AI** - Game intelligence, strategy, NPC behavior
- **Extensible Plugin System** - Easy to add new AI capabilities

### Infrastructure
- **Full-stack Application** - Python backend + React frontend
- **Microservices Architecture** - Modular, scalable design
- **API-First Design** - RESTful APIs + WebSocket support
- **Database Integration** - PostgreSQL + Vector DB for embeddings
- **Docker & Kubernetes Ready** - Cloud-native deployment
- **CI/CD Pipeline** - Automated testing and deployment

## 📋 Project Structure

```
BungusAI/
├── backend/
│   ├── ai_core/              # Core AI modules
│   │   ├── conversation/     # Chatbot & dialogue
│   │   ├── vision/          # Image processing
│   │   ├── nlp/             # Text processing
│   │   ├── prediction/      # ML predictions
│   │   └── gaming/          # Game AI
│   ├── services/             # Business logic services
│   ├── models/               # ML models & data models
│   ├── utils/                # Utility functions
│   ├── config/               # Configuration
│   └── tests/                # Testing suite
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API services
│   │   └── utils/           # Utilities
│   └── tests/               # Frontend tests
├── infrastructure/
│   ├── docker/              # Docker configurations
│   ├── k8s/                 # Kubernetes configs
│   └── scripts/             # Setup scripts
├── docs/                     # Documentation
└── .github/workflows/        # CI/CD pipelines
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL 14+

### Installation

1. **Clone and Setup**
   ```bash
   git clone https://github.com/RealAdaptivity/BungusAI.git
   cd BungusAI
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

5. **Start Development**
   ```bash
   # Terminal 1: Backend
   cd backend
   python app.py
   
   # Terminal 2: Frontend
   cd frontend
   npm start
   ```

## 📚 API Endpoints

### Conversation
- `POST /api/chat` - Send message to chatbot
- `GET /api/conversation/:id` - Get conversation history
- `DELETE /api/conversation/:id` - Clear conversation

### Vision
- `POST /api/vision/analyze` - Analyze image
- `POST /api/vision/detect` - Object detection
- `POST /api/vision/ocr` - Extract text from image

### NLP
- `POST /api/nlp/analyze` - Text analysis
- `POST /api/nlp/sentiment` - Sentiment analysis
- `POST /api/nlp/entities` - Extract entities

### Prediction
- `POST /api/predict` - Make predictions
- `POST /api/predict/train` - Train model
- `GET /api/predict/models` - List available models

### Gaming
- `POST /api/game/start` - Start game
- `POST /api/game/move` - AI move
- `GET /api/game/:id` - Game state

## 🔧 Configuration

See `docs/setup/configuration.md` for detailed configuration guide.

### Environment Variables
```
CLAUDE_API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@localhost/bungusai
REDIS_URL=redis://localhost:6379
OPENAI_API_KEY=optional_for_vision
ENVIRONMENT=development
DEBUG=true
```

## 🧪 Testing

```bash
# Run all tests
pytest backend/tests -v

# Run frontend tests
npm test

# Run integration tests
pytest backend/tests/integration -v
```

## 📖 Documentation

- [Architecture Guide](docs/architecture/ARCHITECTURE.md)
- [API Documentation](docs/api/API.md)
- [Setup Guide](docs/setup/SETUP.md)
- [Contributing Guide](CONTRIBUTING.md)

## 🚢 Deployment

### Docker
```bash
docker-compose up -d
```

### Kubernetes
```bash
kubectl apply -f infrastructure/k8s/
```

See `docs/deployment/DEPLOYMENT.md` for detailed instructions.

## 📦 Core Technologies

- **Backend**: Python, FastAPI/Flask, SQLAlchemy
- **Frontend**: React, TypeScript, Tailwind CSS
- **AI/ML**: Claude API, TensorFlow, scikit-learn, YOLO
- **Database**: PostgreSQL, Redis, Pinecone (vector DB)
- **DevOps**: Docker, Kubernetes, GitHub Actions
- **Testing**: pytest, Jest, Cypress

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - See LICENSE file for details

## 🔗 Resources

- [Claude API Docs](https://docs.anthropic.com)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [React Docs](https://react.dev)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/RealAdaptivity/BungusAI/issues)
- **Discussions**: [GitHub Discussions](https://github.com/RealAdaptivity/BungusAI/discussions)
- **Email**: support@bungusai.dev

---

**Built with ❤️ by BungusAI Team**
