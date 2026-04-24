# Resume Optimizer with HuggingFace & LlamaIndex

![GIf](./demo.gif)

A powerful AI-powered resume optimization tool that helps job seekers enhance their resumes based on specific job requirements. Built with Streamlit and powered by open-source HuggingFace models, this application provides targeted suggestions to improve your resume's effectiveness.

## Features

- **PDF Resume Processing**: Upload and analyze your resume in PDF format
- **Job-Specific Optimization**: Get tailored suggestions based on job title and description
- **Multiple Optimization Types**:
  - ATS Keyword Optimizer
  - Experience Section Enhancer
  - Skills Hierarchy Creator
  - Professional Summary Crafter
  - Education Optimizer
  - Technical Skills Showcase
  - Career Gap Framing
- **Real-time Preview**: View your resume while making changes
- **AI-Powered Analysis**: Leverages open-source HuggingFace models for intelligent suggestions
- **GPU Support**: Automatic CUDA detection for faster processing
- **Local Processing**: Run completely offline with HuggingFace models

## Prerequisites

- Python 3.10 or higher
- PDF resume file
- 8GB RAM minimum (16GB+ recommended for faster inference)
- Optional: NVIDIA GPU with CUDA support for faster processing

## Installation

### Option 1: Standard pip installation

```bash
# Clone the repository
git clone <your-repository-url>
cd resume-analyser-app-using-rag

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Using uv (recommended for faster installation)

```bash
# Clone the repository
git clone <your-repository-url>
cd resume-analyser-app-using-rag

# Install with uv
uv sync
```

## Environment Setup

Create a `.env` file in the project root (optional, for HuggingFace token if using gated models):

```env
# Optional: HuggingFace API token for accessing gated models
HUGGINGFACE_API_TOKEN=your_token_here
```

To get a HuggingFace token:
1. Create a free account at [HuggingFace](https://huggingface.co)
2. Go to Settings → Access Tokens → Create New Token
3. Copy your token and add it to `.env`

## Usage

### 1. Start the application:

```bash
streamlit run main.py
```

### 2. Open your browser:
Navigate to http://localhost:8501

### 3. In the application:
- **Choose Models** (optional): Select embedding and generative models from the sidebar
- **Upload Resume**: Upload your resume in PDF format
- **Enter Job Details**: Provide the job title and complete job description
- **Select Optimization Type**: Choose what aspect of your resume to optimize
- **Click Optimize**: Let AI analyze and generate suggestions
- **Review Results**: Read the optimization suggestions in the right panel

## How It Works

### Architecture

```
User Input (PDF, Job Info)
        ↓
   PDF Processing (PyPDF2)
        ↓
Document Indexing (LlamaIndex)
        ↓
Embedding Generation (HuggingFace)
        ↓
Vector Store Creation
        ↓
RAG Query Processing
        ↓
LLM Response Generation (HuggingFace)
        ↓
Structured Output Display
```

### Process Flow

1. **Resume Upload**: The application processes your PDF resume and extracts its content using PyPDF2
2. **Document Indexing**: Content is indexed using LlamaIndex for efficient retrieval
3. **Embedding Generation**: Uses HuggingFace embeddings to convert text to vectors
4. **Job Analysis**: Analyzes the provided job title and description
5. **RAG Processing**: Uses Retrieval-Augmented Generation to find relevant resume sections
6. **AI Processing**: Uses open-source HuggingFace LLMs to:
   - Analyze your resume content
   - Compare it with job requirements
   - Generate targeted improvement suggestions
7. **Optimization**: Provides specific, actionable recommendations based on your selected optimization type

## Available Models

### Generative Models

- **Mistral 7B Instruct** (recommended for most users)
  - Model: `mistralai/Mistral-7B-Instruct-v0.2`
  - Size: ~15GB
  - Speed: Good, balanced performance

- **Llama 2 7B Chat**
  - Model: `meta-llama/Llama-2-7b-chat-hf`
  - Size: ~14GB
  - Speed: Good

- **Google Flan-T5 Base**
  - Model: `google/flan-t5-base`
  - Size: ~1GB
  - Speed: Fast, good for CPU-only systems

- **Mistral 7B**
  - Model: `mistralai/Mistral-7B-v0.1`
  - Size: ~15GB
  - Speed: Good

### Embedding Models

- **All-MiniLM-L6-v2** (recommended)
  - Model: `sentence-transformers/all-MiniLM-L6-v2`
  - Size: ~22MB
  - Speed: Very fast

- **All-MPNet-Base-v2**
  - Model: `sentence-transformers/all-mpnet-base-v2`
  - Size: ~438MB
  - Speed: Slightly slower but more accurate

- **Paraphrase-MiniLM-L6-v2**
  - Model: `sentence-transformers/paraphrase-MiniLM-L6-v2`
  - Size: ~22MB
  - Speed: Very fast

## Optimization Types Explained

- **ATS Keyword Optimizer**: Enhances your resume with relevant keywords that pass Applicant Tracking Systems
- **Experience Section Enhancer**: Improves the presentation of your work experience with quantifiable achievements
- **Skills Hierarchy Creator**: Organizes your skills based on job requirements and identifies gaps
- **Professional Summary Crafter**: Creates a compelling professional summary highlighting relevant experience
- **Education Optimizer**: Optimizes education section to emphasize relevant qualifications
- **Technical Skills Showcase**: Highlights your technical competencies in an organized manner
- **Career Gap Framing**: Helps address career gaps professionally with growth context

## System Requirements

### Minimum (CPU-only, slower)
- RAM: 8GB
- Storage: 10GB for models and dependencies
- Processor: Multi-core CPU

### Recommended (with GPU)
- RAM: 16GB+
- VRAM: 6GB+ (NVIDIA GPU with CUDA)
- Storage: 20GB for models
- GPU: NVIDIA GPU (RTX 3060 or better)

### Installation Tips for Different Systems

#### macOS
```bash
# Ensure you have Python 3.10+
python --version

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install PyTorch for macOS (CPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install other dependencies
pip install -r requirements.txt
```

#### Linux with GPU
```bash
# Install CUDA toolkit (if not already installed)
# Follow: https://developer.nvidia.com/cuda-downloads

# Install dependencies
pip install -r requirements.txt
```

#### Windows
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Troubleshooting

### Issue: Out of Memory (OOM) Error
**Solution**: 
- Use a smaller model: Switch to `google/flan-t5-base`
- Use CPU: Remove CUDA to force CPU usage
- Reduce batch size in the code

### Issue: Models downloading very slowly
**Solution**:
- Check your internet connection
- Models cache in `~/.cache/huggingface/` - ensure you have space
- Use offline mode if models are already cached

### Issue: CUDA not detected on Windows
**Solution**:
- Ensure NVIDIA GPU drivers are up to date
- Reinstall PyTorch: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`

### Issue: PDF not loading
**Solution**:
- Ensure PDF is not encrypted
- Try opening the PDF with a standard PDF viewer first
- Check file permissions

### Issue: Slow inference on CPU
**Solution**:
- Use GPU if available
- Switch to smaller model like Flan-T5
- Increase timeout in Streamlit settings

## Performance Tips

1. **First Run**: Models will be downloaded (~5-30GB depending on selection). This happens only once.
2. **GPU Usage**: If CUDA is available, it will be used automatically for 10-100x faster inference
3. **Model Selection**: Choose smaller models for faster processing on limited hardware
4. **Concurrent Running**: Avoid running multiple instances simultaneously to prevent memory issues

## Configuration

You can customize the application behavior by editing `main.py`:

- Change default models in the sidebar selectbox
- Adjust temperature/top_p in `run_rag_completion()` for varied responses
- Modify prompts for different optimization strategies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Areas for contribution:
- Additional optimization types
- Support for more resume formats (DOCX, etc.)
- Enhanced UI/UX
- Performance optimizations
- Bug fixes and improvements

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is designed to assist with resume optimization. While it provides AI-powered suggestions, please review all changes carefully before submitting your resume to employers.

## Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Review HuggingFace documentation: https://huggingface.co/docs
3. Check LlamaIndex documentation: https://docs.llamaindex.ai/
4. Open an issue in the repository

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [HuggingFace](https://huggingface.co/)
- RAG implementation using [LlamaIndex](https://www.llamaindex.ai/)
- PDF processing with [PyPDF2](https://github.com/py-pdf/PyPDF2)