import logging
from typing import Dict, Any
import redis

class KnowledgeBaseConnector:
    def __init__(self, host: str = 'localhost', port: int = 6379):
        self.redis_instance = redis.Redis(host=host, port=port)
        
    def update(self, data: Dict[str, Any]) -> None:
        """Store processed data in the knowledge base."""
        try:
            logging.info("Storing data in knowledge base.")
            for key, value in data.items():
                self.redis_instance.hset('semantic_data', key, str(value))
        except Exception as e:
            logging.error(f"Redis error: {str(e)}")
            raise

    def get_semantic_models(self) -> Dict[str, Any]:
        """Retrieve semantic models from the knowledge base."""
        try:
            return self.redis_instance.hgetall('semantic_data')
        except Exception as e:
            logging.error(f"Failed to retrieve data: {str(e)}")
            raise

    def update_semantics(self, updates: Dict[str, Any]) -> None:
        """Update specific semantic models."""
        try:
            for key, value in updates.items():
                self.redis_instance.hset('semantic_data', key, str(value))
        except Exception as e:
            logging.error(f"Failed to update data: {str(e)}")
            raise