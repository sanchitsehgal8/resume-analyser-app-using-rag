"""
Utility functions for Resume Optimizer
Handles PDF processing, document management, and UI helpers
"""

import streamlit as st
import base64
from PyPDF2 import PdfReader
import io
import os
from typing import List, Optional


def display_pdf_preview(pdf_file) -> bool:
    """
    Display PDF preview in the sidebar.
    
    Args:
        pdf_file: Uploaded PDF file object
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        st.sidebar.subheader("📄 Resume Preview")
        base64_pdf = base64.b64encode(pdf_file.getvalue()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500" type="application/pdf"></iframe>'
        st.sidebar.markdown(pdf_display, unsafe_allow_html=True)
        return True
    except Exception as e:
        st.sidebar.error(f"❌ Error previewing PDF: {str(e)}")
        return False


def extract_text_from_pdf(pdf_bytes: bytes) -> Optional[str]:
    """
    Extract text from PDF bytes.
    
    Args:
        pdf_bytes: PDF file content as bytes
        
    Returns:
        Optional[str]: Extracted text or None if failed
    """
    try:
        pdf_reader = PdfReader(io.BytesIO(pdf_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return None


def format_optimization_response(response: str) -> str:
    """
    Format the optimization response for better display.
    
    Args:
        response: Raw response from the model
        
    Returns:
        str: Formatted response
    """
    # Remove common model artifacts
    response = response.replace("<think>", "").replace("</think>", "")
    response = response.replace("[END]", "").strip()
    return response


def validate_inputs(job_title: str, job_description: str, docs_loaded: bool) -> tuple[bool, str]:
    """
    Validate user inputs.
    
    Args:
        job_title: Job title input
        job_description: Job description input
        docs_loaded: Whether documents are loaded
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not docs_loaded:
        return False, "❌ Please upload your resume first"
    if not job_title.strip():
        return False, "❌ Please provide a job title"
    if not job_description.strip():
        return False, "❌ Please provide a job description"
    if len(job_description.strip()) < 50:
        return False, "❌ Job description seems too short. Please provide more details."
    return True, ""


def initialize_session_states():
    """Initialize all required Streamlit session states."""
    defaults = {
        "messages": [],
        "docs_loaded": False,
        "temp_dir": None,
        "current_pdf": None,
        "documents": None,
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value


def get_device_info_emoji(device: str) -> str:
    """
    Get emoji for device type.
    
    Args:
        device: Device type (cuda, cpu, mps)
        
    Returns:
        str: Device info with emoji
    """
    device_map = {
        "cuda": "🟢 GPU (CUDA)",
        "cpu": "🔵 CPU",
        "mps": "🟣 GPU (Metal Performance Shaders)"
    }
    return device_map.get(device, "⚙️ Unknown Device")
