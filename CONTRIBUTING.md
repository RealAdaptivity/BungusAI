# Contributing to BungusAI

Thank you for your interest in contributing to BungusAI! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/BungusAI.git`
3. Create a branch: `git checkout -b feature/your-feature`
4. Follow the development setup in [CLAUDE.md](CLAUDE.md)

## Development Process

### 1. Branch Naming Convention
- Feature: `feature/description-of-feature`
- Bug fix: `fix/description-of-fix`
- Documentation: `docs/description`
- Refactor: `refactor/description`
- Test: `test/description`
- Claude development: `claude/description-id`

### 2. Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

Examples:
```
feat(chat): add context memory to conversations
fix(vision): resolve image processing timeout
docs(api): update endpoint documentation
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

### 3. Before Pushing

#### Backend
```bash
cd backend

# Format code
black . --line-length=100

# Sort imports
isort .

# Lint
flake8 . --max-line-length=100

# Type check
mypy . --ignore-missing-imports

# Run tests
pytest tests/ -v
```

#### Frontend
```bash
cd frontend

# Format and lint
npm run lint
npm run format

# Type check
npm run type-check

# Run tests
npm test
```

### 4. Pull Request Process

1. **Update your branch** with latest main/develop
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Push your changes**
   ```bash
   git push origin feature/your-feature
   ```

3. **Create Pull Request** with:
   - Clear title describing the change
   - Description of what changed and why
   - Link to related issues (if any)
   - Before/after screenshots for UI changes
   - Test results showing what you tested

4. **PR Checklist**
   - [ ] Code follows style guidelines
   - [ ] Tests added/updated and passing
   - [ ] Documentation updated
   - [ ] No breaking changes (or documented)
   - [ ] Commit messages are clear
   - [ ] No sensitive data committed

5. **Review & Merge**
   - Address reviewer feedback
   - Keep commits clean (rebase if needed)
   - Squash commits if instructed
   - Get approval before merging

## Code Style Guide

### Python

**Format with Black**
```bash
black . --line-length=100
```

**Example**
```python
def process_message(
    message: str,
    conversation_id: Optional[str] = None,
    context: Optional[Dict] = None
) -> str:
    """
    Process a user message and generate a response.
    
    Args:
        message: User's message text
        conversation_id: Unique conversation identifier
        context: Optional context information
        
    Returns:
        AI-generated response
        
    Raises:
        ValueError: If message is empty
    """
    if not message:
        raise ValueError("Message cannot be empty")
    
    # Process message logic
    response = ai_engine.generate_response(message)
    return response
```

### TypeScript/React

**Example Component**
```typescript
import React, { useState } from 'react';

interface ChatMessageProps {
  message: string;
  sender: 'user' | 'ai';
  timestamp: Date;
}

export const ChatMessage: React.FC<ChatMessageProps> = ({
  message,
  sender,
  timestamp
}) => {
  return (
    <div className={`message message-${sender}`}>
      <p>{message}</p>
      <time>{timestamp.toLocaleTimeString()}</time>
    </div>
  );
};
```

## Testing Guidelines

### Backend Testing
```python
import pytest
from app import app
from config.settings import settings

@pytest.fixture
def client():
    return TestClient(app)

def test_chat_endpoint(client):
    """Test chat message processing"""
    response = client.post(
        "/api/v1/chat",
        json={
            "message": "Hello",
            "conversation_id": "test-123"
        }
    )
    assert response.status_code == 200
    assert "response" in response.json()
```

### Frontend Testing
```typescript
import { render, screen } from '@testing-library/react';
import { ChatMessage } from './ChatMessage';

describe('ChatMessage', () => {
  it('renders message with sender and timestamp', () => {
    const now = new Date();
    render(
      <ChatMessage
        message="Hello"
        sender="user"
        timestamp={now}
      />
    );
    
    expect(screen.getByText('Hello')).toBeInTheDocument();
  });
});
```

### Coverage Requirements
- Backend: Minimum 80% code coverage
- Frontend: Minimum 70% code coverage
- Critical paths: 100% coverage expected

## Documentation

### Code Documentation
- Docstrings for all functions/classes (Google style)
- Inline comments for complex logic
- Type hints on all functions
- Examples in module docstrings

### External Documentation
- Update README.md for major changes
- Update CLAUDE.md for architectural changes
- Add/update docs/ files for new features
- Keep API documentation current

## Performance Guidelines

### Backend
- Database queries should use indexes
- Cache frequently accessed data
- Avoid N+1 query problems
- Use async/await for I/O operations
- Profile code with large datasets

### Frontend
- Lazy load heavy components
- Memoize expensive computations
- Optimize bundle size
- Use production builds for testing
- Monitor performance metrics

## Security

### Do NOT
- Commit API keys or secrets
- Log sensitive information
- Store passwords in plain text
- Make database passwords public
- Hard-code credentials

### Do
- Use environment variables
- Validate all inputs
- Use HTTPS in production
- Keep dependencies updated
- Review security advisories
- Use prepared statements
- Implement rate limiting

## Reporting Issues

### Bug Reports
Include:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment (OS, Python/Node version)
- Error messages/logs
- Screenshots if applicable

### Feature Requests
Include:
- Clear description of feature
- Use case and benefits
- Possible implementation
- Priority level
- Any related issues

## Questions?

- Open a GitHub Discussion
- Check existing issues/PRs
- Read [CLAUDE.md](CLAUDE.md)
- Review API documentation

## Recognition

Contributors will be:
- Added to CONTRIBUTORS.md
- Mentioned in release notes
- Recognized in documentation

Thank you for contributing to BungusAI! 🚀
