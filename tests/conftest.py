"""
Shared pytest fixtures for the YoloGemma test suite.
"""
import tempfile
import shutil
from pathlib import Path
from typing import Generator, Dict, Any
from unittest.mock import MagicMock

import pytest
import torch
import numpy as np
from PIL import Image


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for testing."""
    temp_path = Path(tempfile.mkdtemp())
    try:
        yield temp_path
    finally:
        shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def sample_image() -> Image.Image:
    """Create a sample PIL image for testing."""
    return Image.new('RGB', (224, 224), color='red')


@pytest.fixture
def sample_tensor() -> torch.Tensor:
    """Create a sample torch tensor for testing."""
    return torch.randn(1, 3, 224, 224)


@pytest.fixture
def sample_numpy_array() -> np.ndarray:
    """Create a sample numpy array for testing."""
    return np.random.rand(224, 224, 3).astype(np.float32)


@pytest.fixture
def mock_model_config() -> Dict[str, Any]:
    """Create a mock model configuration."""
    return {
        "model_name": "test_model",
        "hidden_size": 768,
        "num_attention_heads": 12,
        "num_hidden_layers": 12,
        "vocab_size": 30522,
        "max_position_embeddings": 512,
        "image_size": 224,
        "patch_size": 16
    }


@pytest.fixture
def mock_tokenizer():
    """Create a mock tokenizer."""
    tokenizer = MagicMock()
    tokenizer.encode.return_value = [1, 2, 3, 4, 5]
    tokenizer.decode.return_value = "test output"
    tokenizer.pad_token_id = 0
    tokenizer.eos_token_id = 2
    tokenizer.vocab_size = 30522
    return tokenizer


@pytest.fixture
def mock_model():
    """Create a mock model."""
    model = MagicMock()
    model.eval.return_value = model
    model.to.return_value = model
    model.forward.return_value = torch.randn(1, 10, 30522)
    return model


@pytest.fixture
def sample_text() -> str:
    """Provide sample text for testing."""
    return "This is a test sentence for the YoloGemma model."


@pytest.fixture
def sample_detection_result() -> Dict[str, Any]:
    """Create a sample detection result."""
    return {
        "boxes": [[10, 10, 100, 100], [150, 150, 200, 200]],
        "labels": ["person", "car"],
        "scores": [0.95, 0.87],
        "masks": None
    }


@pytest.fixture(scope="session")
def test_data_dir(tmp_path_factory) -> Path:
    """Create a session-scoped temporary directory for test data."""
    return tmp_path_factory.mktemp("test_data")


@pytest.fixture
def mock_device():
    """Mock device configuration."""
    return "cpu" if not torch.cuda.is_available() else "cuda"


@pytest.fixture(autouse=True)
def set_torch_seed():
    """Set torch random seed for reproducible tests."""
    torch.manual_seed(42)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(42)
        torch.cuda.manual_seed_all(42)


@pytest.fixture(autouse=True)
def set_numpy_seed():
    """Set numpy random seed for reproducible tests."""
    np.random.seed(42)


@pytest.fixture
def mock_gradio_interface():
    """Create a mock Gradio interface."""
    interface = MagicMock()
    interface.launch.return_value = None
    interface.close.return_value = None
    return interface


@pytest.fixture
def sample_video_path(temp_dir: Path) -> Path:
    """Create a sample video file path for testing."""
    video_path = temp_dir / "test_video.mp4"
    video_path.touch()  # Create empty file
    return video_path


@pytest.fixture
def cleanup_files():
    """Fixture to clean up any files created during testing."""
    files_to_cleanup = []
    
    def add_file(filepath: Path):
        files_to_cleanup.append(filepath)
    
    yield add_file
    
    # Cleanup
    for file_path in files_to_cleanup:
        if file_path.exists():
            if file_path.is_dir():
                shutil.rmtree(file_path, ignore_errors=True)
            else:
                file_path.unlink(missing_ok=True)