"""
llamamlx-embeddings: High-performance embeddings with MLX.

This package provides a unified interface for generating text embeddings
using Apple's MLX framework. It supports a variety of models,
efficient batch processing, quantization, seamless integration with vector
databases, and easy deployment as a FastAPI service.
"""

# Integration clients
from .client import LlamamlxEmbeddingsClient  # For API client

# Core embedding functionality
from .core.embeddings import (  # For direct use
    BaseEmbedding,
    Embeddings,
    LateInteractionTextEmbedding,
    SparseTextEmbedding,
    TextCrossEncoder,
    TextEmbedding,
)

# Mock embeddings for testing
from .core.mock_embeddings import MockEmbedding

# Model management
from .core.models import (
    get_model_info,
    list_supported_models,
    load_mlx_model,
)
from .core.models import register_custom_model as add_custom_model

# Quantization utilities
from .core.quantization import dequantize, get_quantization_status, quantize

# Import sparse embedding utilities
from .core.sparse import (
    SparseEmbedding,
    convert_to_sparse_embedding,
    sparse_dot_product,
    sparse_normalize,
)
from .integrations.base import VectorDBClient  # Abstract base class

# Get logger
from .logging import get_logger

# Processing utilities
from .processing.text import (
    chunk_text,
    preprocess_text,
)

# Import utility functions for better error handling
from .utils.error_handling import (
    DependencyError,
    ModelNotFoundError,
    check_dependency,
    configure_logging,
    handle_fatal_error,
    require_dependency,
    safe_import,
    with_fallback,
)

# Import version
from .version import __version__

# Try to import integration clients, but don't fail if dependencies are missing
qdrant_client = safe_import("qdrant_client", extra_name="qdrant")
if qdrant_client:
    from .integrations.qdrant import QdrantClient  # Qdrant convenience class
else:

    class QdrantClient(VectorDBClient):
        """Placeholder for QdrantClient when qdrant-client is not installed."""

        def __init__(self, *args, **kwargs):
            raise ImportError(
                "Qdrant integration requires qdrant-client package. Install with 'pip install llamamlx-embeddings[qdrant]'"
            )


# Try with new package name
pinecone = safe_import("pinecone", extra_name="pinecone")
if pinecone:
    from .integrations.pinecone import PineconeClient  # Pinecone client
else:

    class PineconeClient(VectorDBClient):
        """Placeholder for PineconeClient when pinecone package is not installed."""

        def __init__(self, *args, **kwargs):
            raise ImportError(
                "Pinecone integration requires pinecone package. Install with 'pip install llamamlx-embeddings[pinecone]'. "
                "Note the package was renamed from pinecone-client to pinecone."
            )


# Expose logging configuration for users
__all__ = [
    # Version
    "__version__",
    # Logging and error handling
    "configure_logging",
    "get_logger",
    "safe_import",
    "check_dependency",
    "require_dependency",
    "with_fallback",
    "handle_fatal_error",
    "DependencyError",
    "ModelNotFoundError",
    # Core embeddings
    "BaseEmbedding",
    "TextEmbedding",
    "SparseTextEmbedding",
    "LateInteractionTextEmbedding",
    "TextCrossEncoder",
    "Embeddings",
    "MockEmbedding",
    # Sparse embedding utilities
    "SparseEmbedding",
    "sparse_normalize",
    "sparse_dot_product",
    "convert_to_sparse_embedding",
    # Text processing
    "preprocess_text",
    "chunk_text",
    # Model management
    "list_supported_models",
    "add_custom_model",
    "load_mlx_model",
    "get_model_info",
    # Quantization
    "quantize",
    "dequantize",
    "get_quantization_status",
    # Integration clients
    "LlamamlxEmbeddingsClient",
    "QdrantClient",
    "PineconeClient",
    "VectorDBClient",
]

# Initialize logging with default configuration
logger = get_logger("init")
logger.debug(f"llamamlx-embeddings v{__version__} initialized")
