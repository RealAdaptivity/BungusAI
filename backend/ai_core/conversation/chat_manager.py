"""
Chat Manager - Handles conversational AI using Claude API
"""

import logging
from typing import Optional, Dict, Any
from datetime import datetime
import uuid
from anthropic import Anthropic
from config.settings import settings

logger = logging.getLogger(__name__)


class ChatManager:
    """Manages conversations using Claude API"""

    def __init__(self):
        """Initialize the chat manager"""
        self.client = Anthropic(api_key=settings.CLAUDE_API_KEY)
        self.conversations: Dict[str, list] = {}
        self.system_prompt = """You are BungusAI, an omnipotent AI assistant capable of doing everything.
You can help with:
- Casual conversations and chitchat
- Problem-solving and analysis
- Creative writing and storytelling
- Technical explanations and coding help
- Data analysis and predictions
- Game playing and strategy
- Image analysis and vision tasks
- Natural language processing
- And much more!

Be helpful, creative, and engaging. Always try to understand the user's intent and provide the most useful response."""

    async def process_message(
        self,
        message: str,
        conversation_id: Optional[str] = None,
        context: Optional[Dict] = None
    ) -> str:
        """
        Process a user message and generate a response

        Args:
            message: User's message
            conversation_id: Unique conversation identifier
            context: Optional context information

        Returns:
            AI response
        """
        try:
            # Generate conversation ID if not provided
            if not conversation_id:
                conversation_id = str(uuid.uuid4())

            # Initialize conversation history if needed
            if conversation_id not in self.conversations:
                self.conversations[conversation_id] = []

            # Add user message to history
            self.conversations[conversation_id].append({
                "role": "user",
                "content": message,
                "timestamp": datetime.now().isoformat()
            })

            # Build messages for API
            messages = [
                {"role": msg["role"], "content": msg["content"]}
                for msg in self.conversations[conversation_id][-settings.MAX_CONVERSATION_HISTORY:]
            ]

            # Call Claude API
            response = self.client.messages.create(
                model=settings.CLAUDE_MODEL,
                max_tokens=settings.CLAUDE_MAX_TOKENS,
                temperature=settings.CLAUDE_TEMPERATURE,
                system=self.system_prompt,
                messages=messages
            )

            # Extract response text
            assistant_message = response.content[0].text

            # Add assistant response to history
            self.conversations[conversation_id].append({
                "role": "assistant",
                "content": assistant_message,
                "timestamp": datetime.now().isoformat()
            })

            logger.info(f"Processed message in conversation {conversation_id}")
            return assistant_message

        except Exception as e:
            logger.error(f"Error in process_message: {e}")
            raise

    async def get_history(self, conversation_id: str) -> list:
        """
        Get conversation history

        Args:
            conversation_id: Conversation ID

        Returns:
            List of messages in the conversation
        """
        return self.conversations.get(conversation_id, [])

    async def clear_conversation(self, conversation_id: str) -> bool:
        """
        Clear a conversation

        Args:
            conversation_id: Conversation ID to clear

        Returns:
            True if successful
        """
        if conversation_id in self.conversations:
            del self.conversations[conversation_id]
            logger.info(f"Cleared conversation {conversation_id}")
            return True
        return False

    async def create_conversation(self) -> str:
        """
        Create a new conversation

        Returns:
            Conversation ID
        """
        conversation_id = str(uuid.uuid4())
        self.conversations[conversation_id] = []
        logger.info(f"Created conversation {conversation_id}")
        return conversation_id
