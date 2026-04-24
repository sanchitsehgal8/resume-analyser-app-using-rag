"""
Configuration module for Resume Optimizer
Centralized configuration management for models, paths, and settings
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ============== MODEL CONFIGURATION ==============

# Embedding Models
EMBEDDING_MODELS = {
    "all-MiniLM-L6-v2": {
        "model_id": "sentence-transformers/all-MiniLM-L6-v2",
        "size": "22MB",
        "description": "Fast, lightweight embedding model"
    },
    "all-mpnet-base-v2": {
        "model_id": "sentence-transformers/all-mpnet-base-v2",
        "size": "438MB",
        "description": "More accurate, slightly slower"
    },
    "paraphrase-MiniLM-L6-v2": {
        "model_id": "sentence-transformers/paraphrase-MiniLM-L6-v2",
        "size": "22MB",
        "description": "Optimized for paraphrase detection"
    }
}

DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Generative Models
GENERATIVE_MODELS = {
    "Mistral 7B Instruct": {
        "model_id": "mistralai/Mistral-7B-Instruct-v0.2",
        "size": "15GB",
        "description": "Balanced performance, recommended"
    },
    "Llama 2 7B Chat": {
        "model_id": "meta-llama/Llama-2-7b-chat-hf",
        "size": "14GB",
        "description": "Good general performance"
    },
    "Flan-T5 Base": {
        "model_id": "google/flan-t5-base",
        "size": "1GB",
        "description": "Lightweight, CPU-friendly"
    },
    "Mistral 7B": {
        "model_id": "mistralai/Mistral-7B-v0.1",
        "size": "15GB",
        "description": "Base Mistral model"
    }
}

DEFAULT_GENERATIVE_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

# ============== DEVICE CONFIGURATION ==============

import torch

DEVICE = os.getenv("TORCH_DEVICE", "cuda" if torch.cuda.is_available() else "cpu")
DEVICE_INFO = f"Running on: {'GPU (CUDA)' if DEVICE == 'cuda' else 'CPU'}"

# ============== LLM GENERATION PARAMETERS ==============

GENERATION_KWARGS = {
    "temperature": 0.7,
    "top_p": 0.9,
    "max_new_tokens": 1024,
    "do_sample": True,
    "num_beams": 1
}

# ============== RAG CONFIGURATION ==============

SIMILARITY_TOP_K = 5  # Number of top similar chunks to retrieve

# ============== OPTIMIZATION PROMPTS ==============

OPTIMIZATION_PROMPTS = {
    "ATS Keyword Optimizer": "Identify and optimize ATS keywords. Focus on exact matches and semantic variations from the job description.",
    "Experience Section Enhancer": "Enhance experience section to align with job requirements. Focus on quantifiable achievements.",
    "Skills Hierarchy Creator": "Organize skills based on job requirements. Identify gaps and development opportunities.",
    "Professional Summary Crafter": "Create a targeted professional summary highlighting relevant experience and skills.",
    "Education Optimizer": "Optimize education section to emphasize relevant qualifications for this position.",
    "Technical Skills Showcase": "Organize technical skills based on job requirements. Highlight key competencies.",
    "Career Gap Framing": "Address career gaps professionally. Focus on growth and relevant experience."
}

RESUME_ANALYSIS_PROMPT = """Analyze this resume in detail. Focus on:
1. Key skills and expertise
2. Professional experience and achievements
3. Education and certifications
4. Notable projects or accomplishments
5. Career progression and gaps

Provide a concise analysis in bullet points."""

# ============== OUTPUT FORMATTING ==============

OPTIMIZATION_OUTPUT_FORMAT = """Provide a direct, structured response in this exact format:

## Key Findings
• [2-3 bullet points highlighting main alignment and gaps]

## Specific Improvements
• [3-5 bullet points with concrete suggestions]
• Each bullet should start with a strong action verb
• Include specific examples where possible

## Action Items
• [2-3 specific, immediate steps to take]
• Each item should be clear and implementable

Keep all points concise and actionable."""

# ============== PATHS ==============

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.expanduser("~/.cache/huggingface/")

# ============== ENVIRONMENT VARIABLES ==============

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN", None)

# ============== VALIDATION ==============

def validate_config():
    """Validate the configuration"""
    if DEVICE == "cuda" and not torch.cuda.is_available():
        print("Warning: CUDA not available, falling back to CPU")
        return False
    return True
