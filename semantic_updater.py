import logging
from typing import Dict, Any
from knowledge_base_connector import KnowledgeBaseConnector

class SemanticUpdater:
    def __init__(self):
        self.knowledge_base = KnowledgeBaseConnector()
        
    def update_semantic_models(self, updates: Dict[str, Any]) -> None:
        """Update semantic models in the knowledge base."""
        try:
            logging.info("Updating semantic models.")
            self.knowledge_base.update_semantics(updates)
        except Exception as e:
            logging.error(f"Failed to update semantic models: {str(e)}")
            raise

    def retrieve_models(self) -> Dict[str, Any]:
        """Retrieve current semantic models."""
        try:
            return self.knowledge_base.get_semantic_models()
        except Exception as e:
            logging.error(f"Failed to retrieve semantic models: {str(e)}")
            raise