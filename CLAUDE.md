# BungusAI - Codebase Documentation

## 📋 Overview

**BungusAI** is a comprehensive, full-featured AI platform capable of handling **everything**: conversational AI, vision/image processing, natural language processing, data analysis/prediction, gaming AI, and much more.

This document provides essential context for AI assistants and developers working on the BungusAI codebase.

## 🏗️ Architecture Overview

### Technology Stack

- **Backend**: Python 3.11+ with FastAPI
- **Frontend**: React 18+ with TypeScript
- **Database**: PostgreSQL 15+ for relational data
- **Cache**: Redis 7+ for caching and sessions
- **AI/ML**: Claude API, TensorFlow, scikit-learn, PyTorch
- **DevOps**: Docker, Docker Compose, Kubernetes-ready
- **CI/CD**: GitHub Actions

### Project Structure

```
BungusAI/
├── backend/                 # Python FastAPI application
│   ├── app.py              # Main application entry point
│   ├── config/             # Configuration management
│   │   └── settings.py     # Centralized settings
│   ├── ai_core/            # Core AI modules
│   │   ├── conversation/   # Claude API-powered chatbot
│   │   ├── vision/         # Image processing & analysis
│   │   ├── nlp/            # Text processing & NLP
│   │   ├── prediction/     # ML model predictions
│   │   └── gaming/         # Game AI engine
│   ├── services/           # Business logic services
│   ├── models/             # Data models & ML models
│   ├── utils/              # Utility functions
│   ├── tests/              # Test suite
│   └── requirements.txt    # Python dependencies
├── frontend/               # React TypeScript application
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── services/      # API integration
│   │   └── utils/         # Utilities
│   ├── package.json       # Node dependencies
│   └── vite.config.ts     # Vite configuration
├── infrastructure/        # DevOps & deployment
│   ├── docker/           # Docker configurations
│   ├── k8s/              # Kubernetes manifests
│   └── scripts/          # Setup scripts
├── docs/                 # Documentation
│   ├── architecture/     # Architecture guides
│   ├── api/             # API documentation
│   ├── setup/           # Setup guides
│   └── tutorials/       # Tutorials
├── .github/workflows/    # GitHub Actions CI/CD
├── Dockerfile           # Multi-stage Docker build
├── docker-compose.yml   # Local development setup
├── .env.example         # Environment template
└── README.md            # Project README
```

## 🔑 Key Features

### 1. **Conversational AI**
- **Module**: `backend/ai_core/conversation/chat_manager.py`
- **Uses**: Claude API (Anthropic)
- **Capabilities**: Natural conversations with context awareness
- **API**: `POST /api/v1/chat`, `GET /api/v1/conversation/{id}`

### 2. **Vision & Image Processing**
- **Module**: `backend/ai_core/vision/vision_processor.py`
- **Capabilities**: 
  - Image analysis (general, detailed, object detection)
  - Object detection (YOLO)
  - OCR (text extraction)
  - Image classification
- **API**: `POST /api/v1/vision/analyze`, `/vision/detect`, `/vision/ocr`

### 3. **Natural Language Processing**
- **Module**: `backend/ai_core/nlp/nlp_engine.py`
- **Capabilities**:
  - Text analysis & statistics
  - Sentiment analysis
  - Named entity recognition
  - Text summarization
  - Keyword extraction
- **API**: `POST /api/v1/nlp/analyze`, `/nlp/sentiment`, `/nlp/entities`

### 4. **Machine Learning & Prediction**
- **Module**: `backend/ai_core/prediction/prediction_engine.py`
- **Capabilities**:
  - Model training & management
  - Predictions with multiple models
  - Model evaluation & metrics
- **API**: `POST /api/v1/predict`, `/predict/train`, `GET /predict/models`

### 5. **Gaming AI**
- **Module**: `backend/ai_core/gaming/game_engine.py`
- **Supported Games**: Chess, Tic-Tac-Toe, Checkers, 20 Questions, Word Games
- **Features**: AI opponent, multiple difficulty levels
- **API**: `POST /api/v1/game/start`, `POST /game/{id}/move`, `GET /game/{id}`

## 🔌 Core Configuration

### Settings Management
- **Location**: `backend/config/settings.py`
- **Method**: Pydantic BaseSettings with environment variables
- **Key Settings**:
  - `CLAUDE_API_KEY`: Claude API authentication
  - `DATABASE_URL`: PostgreSQL connection
  - `REDIS_URL`: Redis cache connection
  - `DEBUG`: Debug mode toggle
  - `ENVIRONMENT`: dev/staging/production

### Environment Variables
See `.env.example` for all available configuration options.

## 🚀 Development Workflow

### Local Setup

1. **Clone and enter directory**
   ```bash
   git clone https://github.com/RealAdaptivity/BungusAI.git
   cd BungusAI
   ```

2. **Backend setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cp ../.env.example ../.env
   ```

3. **Frontend setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Start services**
   ```bash
   # Option 1: Docker Compose (recommended)
   docker-compose up

   # Option 2: Manual (Terminal 1)
   cd backend && python app.py

   # Option 2: Manual (Terminal 2)
   cd frontend && npm run dev
   ```

### API Testing

- **Health Check**: `curl http://localhost:8000/health`
- **Status**: `curl http://localhost:8000/status`
- **Documentation**: `http://localhost:8000/docs` (Swagger UI)

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v
pytest tests/ --cov=. --cov-report=html
```

### Frontend Tests
```bash
cd frontend
npm test
npm run test:ui
```

## 📚 API Documentation

### Base URL
- Development: `http://localhost:8000/api/v1`
- Production: `https://api.bungusai.dev/api/v1`

### Authentication
Currently supports API key authentication via headers:
```
Authorization: Bearer YOUR_API_KEY
```

### Endpoints by Category

**Chat/Conversation**
- `POST /chat` - Send message
- `GET /conversation/:id` - Get history
- `DELETE /conversation/:id` - Clear chat

**Vision**
- `POST /vision/analyze` - Analyze image
- `POST /vision/detect` - Detect objects
- `POST /vision/ocr` - Extract text

**NLP**
- `POST /nlp/analyze` - Analyze text
- `POST /nlp/sentiment` - Sentiment analysis
- `POST /nlp/entities` - Extract entities

**Prediction**
- `POST /predict` - Make prediction
- `POST /predict/train` - Train model
- `GET /predict/models` - List models

**Gaming**
- `POST /game/start` - Start game
- `POST /game/:id/move` - Make move
- `GET /game/:id` - Get state

### WebSocket Endpoints
- `WS /ws/chat/:conversation_id` - Real-time chat

## 🔄 Database Schema

### Key Tables
- `conversations` - Chat history
- `users` - User accounts
- `models` - ML models metadata
- `games` - Game sessions
- `predictions` - Prediction history

### Migrations
Run with Alembic:
```bash
alembic upgrade head
alembic downgrade -1
alembic revision --autogenerate -m "Description"
```

## 🐳 Docker & Deployment

### Local Development
```bash
docker-compose up -d
docker-compose down
docker-compose logs -f backend
```

### Production Build
```bash
docker build -t bungusai:1.0.0 .
docker run -p 8000:8000 --env-file .env bungusai:1.0.0
```

### Kubernetes
```bash
kubectl apply -f infrastructure/k8s/
kubectl get pods
kubectl logs deployment/bungusai-backend
```

## 📖 Code Style & Standards

### Python
- **Style**: PEP 8, enforced with `black` and `flake8`
- **Type Hints**: Required, checked with `mypy`
- **Docstrings**: Google-style docstrings
- **Testing**: pytest with >80% coverage

### TypeScript/React
- **Linter**: ESLint with TypeScript support
- **Formatter**: Prettier
- **Components**: Functional components with hooks
- **Testing**: Vitest + React Testing Library

### Git Conventions
- **Branches**: `feature/name`, `fix/name`, `claude/**`
- **Commits**: Conventional commits format
- **PRs**: Require tests, linting, and documentation

## 🔐 Security Considerations

### API Security
- CORS properly configured
- HTTPS enforced in production
- JWT tokens for authentication
- Rate limiting on endpoints
- Input validation with Pydantic

### Data Protection
- Database passwords in environment
- API keys not committed to repo
- Sensitive logs redacted
- HTTPS for all external requests

## 🐛 Common Development Tasks

### Adding a New AI Capability
1. Create module in `backend/ai_core/new_capability/`
2. Implement class inheriting from base engine
3. Add endpoints in `backend/app.py`
4. Write tests in `backend/tests/`
5. Update documentation
6. Add to CI/CD pipeline

### Adding Frontend Components
1. Create component in `frontend/src/components/`
2. Create tests alongside
3. Export from index files
4. Use in pages/layouts
5. Update stories/documentation

### Database Changes
1. Create Alembic migration
2. Update `models/` definitions
3. Test migration up and down
4. Document schema changes

## 📞 Support & Troubleshooting

### Common Issues

**Claude API not connecting**
- Check `CLAUDE_API_KEY` in `.env`
- Verify API key is active on Anthropic dashboard

**Database connection errors**
- Ensure PostgreSQL is running
- Check `DATABASE_URL` connection string
- Verify database exists

**Frontend can't reach backend**
- Check backend is running on port 8000
- Verify CORS settings in `.env`
- Check browser console for errors

## 📝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Branch Naming
- Development: `claude/ai-creation-planning-322x2w`
- Features: `feature/description`
- Fixes: `fix/description`

### Pull Request Checklist
- [ ] Tests pass locally
- [ ] Code formatted with black/prettier
- [ ] Type checking passes
- [ ] Documentation updated
- [ ] No sensitive data committed
- [ ] PR description is clear

## 🔗 Useful Links

- [Claude API Docs](https://docs.anthropic.com)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [React Docs](https://react.dev)
- [PostgreSQL Docs](https://www.postgresql.org/docs)
- [Docker Docs](https://docs.docker.com)

## 📄 License

MIT License - See LICENSE file

---

**Last Updated**: 2024  
**Maintainers**: BungusAI Team
