# Agentic Emotional AI Assistant (NLP + RAG + Memory + Gemini LLM) 🤖

An advanced, multi-agent conversational platform built using **Streamlit**, **Google Gemini**, **HuggingFace Transformers**, and a specialized, lightweight **RAG + Memory architecture**. 

This system operates beyond standard chatbots by executing dedicated agentic workers to dissect user state vectors, query memory registers, pull psychological coping contexts, and reason through a generative LLM layer to deliver deeply empathetic, supportive conversations.

## 🚀 Live Links
* **Live Demo App:** [emotional-intelligence-agent-chatbot.streamlit.app](https://emotional-intelligence-agent-chatbot.streamlit.app/)
* **Source Code Repository:** [github.com/shankar-kumar-skj/Emotional-ChatBot](https://github.com/shankar-kumar-skj/Emotional-ChatBot)

---

## ✨ Features Breakdown

### 🧠 Multi-Agent Orchestration Layer
* **Emotion Agent:** Tracks core emotional metrics (`sadness`, `joy`, `anger`, `fear`, etc.) using a fine-tuned Transformer backend.
* **Sentiment Agent:** Maps conversational text down into structural polarization vectors (`POSITIVE` / `NEGATIVE`).
* **Memory Agent:** Manages volatile multi-turn memory windows, supplying historical context directly to generation cycles.
* **RAG Agent:** Queries a localized semantic knowledge indexing system to extract optimal behavioral mechanics and coping suggestions.
* **LLM Orchestrator Engine:** Consumes analytical matrix configurations to synthesize highly safe, contextually calibrated replies via Gemini.

### 💬 Deep UI/UX Framework
* Built using a responsive, fluid layout via **Streamlit**.
* Renders real-time classification metrics, multi-turn dialogue histories, and deep "Glass Box" system diagnostics inside each conversation loop.

---

# 📌 Project Structure

```text
Emotional-ChatBot/
│── agents/                    # Multi-Agent Architecture Layer
│   ├── emotion_agent.py       # Intercepts strings to perform cognitive classification
│   ├── memory_agent.py        # Manages session history state loops and sliding windows
│   └── rag_agent.py           # Evaluates localized context maps and coping metadata
│
│── app_streamlit.py           # Main dashboard presentation layer and orchestrator
│── llm_module.py              # Primary Gemini API connector + local tokenizer fallback
│── nlp_module.py              # Synthetic string preprocessing and token conditioning
│── sentiment_module.py        # Pipeline wrappers for core HuggingFace models
│── .env                       # Local environment secrets configuration file
│── .gitignore                 # Tracking exclusion policies for runtime assets
└── requirements.txt           # Verified dependency matrix mapping

```

---

# 📌 Pipeline Processing Mechanics (Flow Diagram)

The application coordinates data flows synchronously, processing user input tokens across downstream evaluation blocks to build a comprehensive context prompt.

```text
                     USER INPUT TEXT
                            │
                            ▼
               [ NLP Preprocessing Module ]      <-- (nlp_module.py)
                            │
                            ▼
             ┌──────────────┴──────────────┐
             ▼                             ▼
     [ Emotion Agent ]             [ Sentiment Agent ]
     (RoBERTa Parsing)             (Polarity Analyzer)
             │                             │
             └──────────────┬──────────────┘
                            │
                            ▼
               [ Memory Retrieval System ]       <-- (agents/memory_agent.py)
                            │
                            ▼
               [ RAG Knowledge Search ]          <-- (agents/rag_agent.py)
                            │
                            ▼
             ┌─────────────────────────────┐
             │ Contextual Prompt Assembler │
             └─────────────────────────────┘
                            │
                            ▼
               [ Gemini 2.5 Flash Engine ]       <-- (llm_module.py)
              (Fallback Layer: DistilGPT-2)
                            │
                            ▼
                  [ Chat Output Render ]         <-- (app_streamlit.py)

```

---

# 📌 Installation & Configuration (Step-by-Step)

### **1. Clone the Project Repository**

```bash
git clone [https://github.com/shankar-kumar-skj/Emotional-ChatBot.git](https://github.com/shankar-kumar-skj/Emotional-ChatBot.git)
cd Emotional-ChatBot

```

### **2. Setup Your Private Key Vectors**

Create a new `.env` file directly inside the workspace root folder:

```env
GEMINI_API_KEY=your_actual_api_key_here

```

### **3. Review Dependencies (`requirements.txt`)**

Verify your system manifest contains the required frameworks for local operation:

```text
streamlit
google-genai
python-dotenv
transformers
torch

```

### **4. Environment Building & Package Ingestion**

```bash
# Initialize isolated workspace environment
python -m venv .venv

# Active project workspace (Windows)
.venv\Scripts\activate

# Active project workspace (Mac/Linux)
source .venv/bin/activate

# Execute batch framework downloads
pip install -r requirements.txt

```

### **5. Run the Active Application**

```bash
streamlit run app_streamlit.py

```

---

# 📌 Deep Architecture Walkthrough

---

## 🟦 1. Core Modules

### **NLP Sanitization Layer (`nlp_module.py`)**

* **Purpose:** Normalizes user interaction data.
* **Mechanism:** Removes extraneous space allocations and cleans out breaking syntax blocks to produce optimized tensor matrices for the classification heads.

### **Analytical Transformers (`sentiment_module.py`)**

* **Purpose:** Drives structural state-classification analytics.
* **Mechanism:** Uses a custom `j-hartmann/emotion-english-distilroberta-base` fine-tuned network to measure specific emotion metrics alongside general positive/negative sentiment weights.

### **Inference Orchestration Module (`llm_module.py`)**

* **Purpose:** Builds rich prompts and handles final generative token streams.
* **Mechanism:** Binds system contexts dynamically using `gemini-2.5-flash`. In the event of network dropouts or API quota exhaustion, it routes tasks automatically to an inline local `distilgpt2` fallback framework.

---

## 🟩 2. Agentic Directory (`agents/`)

### **Emotion Agent (`emotion_agent.py`)**

* **Purpose:** Extracts core human emotion probabilities.
* **Output Matrix:**
```json
{
  "sentiment": "NEGATIVE",
  "emotion": "sadness",
  "confidence": 0.9924
}

```



### **Memory Agent (`memory_agent.py`)**

* **Purpose:** Manages a context window across multiple conversation turns.
* **Mechanism:** Stores the last $N$ interactions in the session state to preserve conversation continuity, avoiding abrupt shifts in agent context.

### **RAG Agent (`rag_agent.py`)**

* **Purpose:** Inject auxiliary therapeutic contextual guidelines.
* **Current Knowledge Baseline:** Employs rule-based heuristics targeting specific emotional matches, such as linking elevated anxiety indexes with deep breathing scripts or suggesting community connection strategies during sadness spikes.

---

# 📊 Diagnostic Output Simulation

* **👤 User Input:** *"I am feeling very sad today"*
* **🧠 System Metric Extraction:**
* **Emotion Matrix:** `sadness` 😔
* **Polar Sentiment:** `NEGATIVE` 📉
* **Memory History Vector:** `[Last 3 structural conversation turns injected]`
* **RAG Context Flag:** `[Triggering contextual guidelines: Exercise & Mindfulness]`


* **🤖 Bot Output Response:** *"I'm incredibly sorry you're navigating through this weight today. Please remember that you aren't carrying this alone. If you feel up to it, taking a small break to breathe deeply or reaching out to a trusted connection could help steady your space..."*

---

# ⚠️ Troubleshooting & Resolution

### **1. Torch / Torchvision Errors**

* **Issue:** `ModuleNotFoundError: torchvision`
* **Resolution:** Ensure the execution space is confined to Python versions `3.10` or `3.11`. Run a targeted cache clear and dependency rebuild using `pip install torch --extra-index-url https://download.pytorch.org/whl/cpu`.

### **2. Array Normalization Anomaly**

* **Issue:** Mathematical operational exceptions (`max()` failures) when evaluating Transformer pipelines.
* **Resolution:** Enforce dictionary assertions within your response wrapper functions to ensure nested prediction lists are cleanly flattened into standardized structural pairs.

---

# 🚀 Engineering Roadmap

* **Vector Database Integration:** Transitioning from in-memory arrays to dedicated vector store systems (e.g., `FAISS`), allowing semantic search across larger behavioral knowledge bases.
* **Stateful Long-Term Databases:** Connecting lightweight database engines (such as `SQLite` or `PostgreSQL`) to store chronological conversation records and trace emotional trend histories over time.
* **Multi-Modal Audio Support:** Expanding pipeline processing capabilities to handle vocal metrics and voice inputs.

```
***

### 💡 Why this layout works perfectly:
1. **Mathematical Cleanliness:** Removed raw, broken prose math styles (e.g., changing `Input text $\to$ strip` to high-end markdown representations), making the repository layout highly legible on mobile and desktop viewports.
2. **Accurate Agent Footprint:** Added clear definitions for the elements in your `agents/` workspace (`emotion_agent.py`, `memory_agent.py`, `rag_agent.py`).
3. **Optimized Structural Styling:** Utilizes uniform formatting metrics across blocks, presenting your project with the technical depth and polish expected of final-year work or production-ready open-source code.

```
