# Quick Start Guide - Resume Optimizer with HuggingFace

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Python 3.10+
- 8GB RAM (16GB+ recommended)
- Optional: NVIDIA GPU for faster processing

### Step 1: Clone & Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd resume-analyser-app-using-rag

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
# Option A: Using pip (standard)
pip install -r requirements.txt

# Option B: Using uv (faster)
uv sync
```

### Step 3: Configure (Optional)
```bash
# Copy .env.example to .env (optional)
cp .env.example .env
```

### Step 4: Run the App
```bash
streamlit run main.py
```

The app will open at http://localhost:8501

---

## 📝 How to Use

1. **Upload Resume**: Click "Upload Resume" in the sidebar and select your PDF
2. **Configure Models**: Choose embedding and generative models (defaults are recommended)
3. **Enter Job Details**: 
   - Add the job title
   - Paste the full job description
4. **Select Optimization Type**: Choose what you want to optimize:
   - ATS Keyword Optimizer
   - Experience Section Enhancer
   - Skills Hierarchy Creator
   - Professional Summary Crafter
   - Education Optimizer
   - Technical Skills Showcase
   - Career Gap Framing
5. **Click Optimize**: Wait for AI analysis and suggestions
6. **Review Results**: See structured recommendations in the right panel

---

## 🎯 Optimization Types Explained

### 1. **ATS Keyword Optimizer**
Enhances your resume with keywords that pass Applicant Tracking Systems
- Perfect for: Large companies using automated screening
- Result: Better keyword alignment with job requirements

### 2. **Experience Section Enhancer**
Improves work experience descriptions
- Perfect for: Emphasizing achievements and impact
- Result: More compelling and quantifiable descriptions

### 3. **Skills Hierarchy Creator**
Organizes skills based on job relevance
- Perfect for: Showing relevant skills first
- Result: Clear prioritization of key skills

### 4. **Professional Summary Crafter**
Creates targeted professional summaries
- Perfect for: Creating impactful opening statements
- Result: Tailored summary highlighting relevant experience

### 5. **Education Optimizer**
Emphasizes relevant education and certifications
- Perfect for: Junior candidates or career changers
- Result: Better highlighting of educational achievements

### 6. **Technical Skills Showcase**
Organizes technical skills effectively
- Perfect for: Engineering and tech roles
- Result: Clear, organized technical competencies

### 7. **Career Gap Framing**
Addresses employment gaps professionally
- Perfect for: Explaining career transitions
- Result: Positive framing of gaps with growth context

---

## 🔧 Configuration Options

### Model Selection

**Generative Models** (for analysis):
- **Mistral 7B Instruct** (⭐ Recommended)
  - Best overall performance and speed
  - ~15GB downloads on first run
  
- **Llama 2 7B Chat**
  - Good alternative with similar performance
  
- **Flan-T5 Base**
  - Lightweight, CPU-friendly option
  - Better for limited resources

**Embedding Models** (for text understanding):
- **All-MiniLM-L6-v2** (⭐ Recommended)
  - Fast and lightweight
  - Perfect for most use cases

---

## ⚡ Performance Tips

### First Run
- Models download on first use (5-30GB depending on selection)
- Subsequent runs will be much faster

### GPU Acceleration
- If you have an NVIDIA GPU: Automatically detected and used (10-100x faster!)
- Check the sidebar - it shows GPU/CPU status

### For Slower Machines
- Use smaller models: Flan-T5 Base
- Use smaller embeddings: All-MiniLM-L6-v2
- Add more RAM or use cloud GPU options

---

## 🐛 Troubleshooting

### Problem: PDF won't upload
**Solution**: 
- Ensure it's a standard PDF (not encrypted)
- Try opening it in a PDF viewer first
- Max file size: 200MB

### Problem: Out of Memory (OOM)
**Solution**:
- Use smaller models (Flan-T5 Base)
- Reduce number of instances running
- Add more RAM to your system

### Problem: Very slow analysis
**Solution**:
- Check if GPU is available (look in sidebar)
- Use smaller models
- Close other applications

### Problem: Models won't download
**Solution**:
- Check internet connection
- Ensure enough disk space (~30GB)
- Try setting HF token in .env file

---

## 📊 System Requirements

| Aspect | Minimum | Recommended |
|--------|---------|-------------|
| RAM | 8GB | 16GB+ |
| Disk Space | 20GB | 30GB+ |
| Processor | Multi-core CPU | Recent CPU |
| GPU | Optional | NVIDIA RTX 2080+ |
| Internet | Required | High speed for first run |

---

## 🔌 Advanced Usage

### Using Different Models
Edit `config.py` to change default models:
```python
DEFAULT_GENERATIVE_MODEL = "google/flan-t5-base"
DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
```

### Adjusting Generation Parameters
Modify `GENERATION_KWARGS` in `config.py`:
```python
GENERATION_KWARGS = {
    "temperature": 0.7,  # Lower = more consistent
    "top_p": 0.9,        # Higher = more creative
    "max_new_tokens": 1024,  # Max output length
}
```

---

## 📚 Resources

- **HuggingFace Models**: https://huggingface.co/models
- **LlamaIndex Docs**: https://docs.llamaindex.ai/
- **Streamlit Docs**: https://docs.streamlit.io/
- **PyTorch Docs**: https://pytorch.org/docs/stable/index.html

---

## ✨ Tips for Best Results

1. **Detailed Job Descriptions**: Paste entire job description, not just title
2. **Clean PDFs**: Use readable, well-formatted resumes
3. **Multiple Optimizations**: Try different types to find best fit
4. **Review Results**: Always review AI suggestions before using them
5. **Iterate**: Run multiple times with different optimizations
6. **Customize**: Adapt suggestions to your specific situation

---

## 🤝 Support

Having issues? 
1. Check the FAQ above
2. Review the main README.md
3. Check HuggingFace documentation
4. Open an issue in the repository

---

**Happy optimizing! 🎉**
