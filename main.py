import streamlit as st
import os
from llama_index.core import SimpleDirectoryReader, Settings, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
from dotenv import load_dotenv
import tempfile
import shutil
import base64
from PyPDF2 import PdfReader
import io
import torch

# Import configuration and utilities
from config import (
    DEVICE, DEFAULT_EMBEDDING_MODEL, DEFAULT_GENERATIVE_MODEL,
    GENERATION_KWARGS, SIMILARITY_TOP_K, OPTIMIZATION_PROMPTS,
    RESUME_ANALYSIS_PROMPT, OPTIMIZATION_OUTPUT_FORMAT, EMBEDDING_MODELS,
    GENERATIVE_MODELS, validate_config
)
from utils import (
    display_pdf_preview, format_optimization_response, validate_inputs,
    initialize_session_states, get_device_info_emoji
)

# Load environment variables
load_dotenv()

# Validate configuration
validate_config()

def run_rag_completion(
    documents,
    query_text: str,
    job_title: str,
    job_description: str,
    embedding_model: str = DEFAULT_EMBEDDING_MODEL,
    generative_model: str = DEFAULT_GENERATIVE_MODEL
) -> str:
    """Run RAG completion using HuggingFace models for resume optimization."""
    try:
        # Initialize HuggingFace LLM
        llm = HuggingFaceLLM(
            model_name=generative_model,
            tokenizer_name=generative_model,
            device_map=DEVICE,
            generate_kwargs=GENERATION_KWARGS
        )

        # Initialize HuggingFace Embeddings
        embed_model = HuggingFaceEmbedding(
            model_name=embedding_model,
            device=DEVICE
        )
        
        Settings.llm = llm
        Settings.embed_model = embed_model
        
        # Step 1: Analyze the resume
        index = VectorStoreIndex.from_documents(documents)
        resume_analysis = index.as_query_engine(
            similarity_top_k=SIMILARITY_TOP_K
        ).query(RESUME_ANALYSIS_PROMPT)
        
        # Step 2: Generate optimization suggestions
        optimization_prompt = f"""Based on the resume analysis and job requirements, provide specific, actionable improvements.

Resume Analysis:
{resume_analysis}

Job Title: {job_title}
Job Description: {job_description}

Optimization Request: {query_text}

{OPTIMIZATION_OUTPUT_FORMAT}"""
        
        optimization_suggestions = index.as_query_engine(
            similarity_top_k=SIMILARITY_TOP_K
        ).query(optimization_prompt)
        
        return str(optimization_suggestions)
    except Exception as e:
        raise

def display_pdf_preview(pdf_file):
    """Display PDF preview in the sidebar."""
    try:
        st.sidebar.subheader("Resume Preview")
        base64_pdf = base64.b64encode(pdf_file.getvalue()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500" type="application/pdf"></iframe>'
        st.sidebar.markdown(pdf_display, unsafe_allow_html=True)
        return True
    except Exception as e:
        st.sidebar.error(f"Error previewing PDF: {str(e)}")
        return False

def main():
    st.set_page_config(page_title="Resume Optimizer", layout="wide")
    
    # Initialize session states
    initialize_session_states()
    
    # Header
    st.title("📝 Resume Optimizer")
    st.caption("🚀 Powered by HuggingFace & LlamaIndex")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Model selection
        generative_model_name = st.selectbox(
            "Generative Model",
            list(GENERATIVE_MODELS.keys()),
            index=0,
            help="Select a HuggingFace model for resume analysis"
        )
        generative_model = GENERATIVE_MODELS[generative_model_name]["model_id"]
        
        embedding_model_name = st.selectbox(
            "Embedding Model",
            list(EMBEDDING_MODELS.keys()),
            index=0,
            help="Select a HuggingFace embedding model"
        )
        embedding_model = EMBEDDING_MODELS[embedding_model_name]["model_id"]
        
        st.divider()
        
        # Device info
        device_info = get_device_info_emoji(DEVICE)
        st.info(f"📊 {device_info}")
        
        st.divider()
        
        # Resume upload
        st.subheader("📄 Upload Resume")
        uploaded_file = st.file_uploader(
            "Choose your resume (PDF)",
            type="pdf",
            accept_multiple_files=False
        )
        
        # Handle PDF upload and processing
        if uploaded_file is not None:
            if uploaded_file != st.session_state.current_pdf:
                st.session_state.current_pdf = uploaded_file
                try:
                    # Create temporary directory for the PDF
                    if st.session_state.temp_dir:
                        shutil.rmtree(st.session_state.temp_dir)
                    st.session_state.temp_dir = tempfile.mkdtemp()
                    
                    # Save uploaded PDF to temp directory
                    file_path = os.path.join(st.session_state.temp_dir, uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    with st.spinner("📚 Loading and processing resume..."):
                        documents = SimpleDirectoryReader(st.session_state.temp_dir).load_data()
                        st.session_state.docs_loaded = True
                        st.session_state.documents = documents
                        st.success("✓ Resume loaded successfully")
                        display_pdf_preview(uploaded_file)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📋 Job Information")
        job_title = st.text_input("Job Title", placeholder="e.g., Senior Software Engineer")
        job_description = st.text_area(
            "Job Description", 
            height=200,
            placeholder="Paste the complete job description here..."
        )
        
        st.subheader("🎯 Optimization Options")
        optimization_type = st.selectbox(
            "Select Optimization Type",
            list(OPTIMIZATION_PROMPTS.keys())
        )
        
        if st.button("🚀 Optimize Resume", use_container_width=True):
            is_valid, error_msg = validate_inputs(
                job_title, 
                job_description, 
                st.session_state.docs_loaded
            )
            
            if not is_valid:
                st.error(error_msg)
                st.stop()
            
            with st.spinner("🔄 Analyzing resume and generating suggestions..."):
                try:
                    response = run_rag_completion(
                        st.session_state.documents,
                        OPTIMIZATION_PROMPTS[optimization_type],
                        job_title,
                        job_description,
                        embedding_model,
                        generative_model
                    )
                    response = format_optimization_response(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.success("✓ Analysis complete!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
            
            st.divider()
    
    with col2:
        st.subheader("💡 Optimization Results")
        if not st.session_state.messages:
            st.info("💬 Results will appear here after you click 'Optimize Resume'")
        else:
            for message in st.session_state.messages[-1:]:
                st.markdown(message["content"])

if __name__ == "__main__":
    main()