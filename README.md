# 🧠 NeuroControl AI 

Production-Ready AI Agent System built with:

- ✅ FastAPI
- ✅ NeuralNode
- ✅ Hybrid Memory (Short-term + Vector DB)
- ✅ ChromaDB (Long-Term Memory)
- ✅ JWT Authentication
- ✅ Tool Execution Framework
- ✅ Structured Logging
- ✅ Secure Session Ownership

---

# 🚀 Project Overview

NeuroControl AI is an advanced Agentic AI system capable of:

- Executing system tools (calculator, notepad, system info, etc.)
- Maintaining conversational short-term memory
- Retrieving long-term relevant memory using vector similarity
- Enforcing JWT-based authentication
- Validating session ownership
- Logging tool execution for security and observability

This project demonstrates:

> AI Systems Engineering  
> LLM Memory Architecture  
> Secure Agent Infrastructure  
> Production-level API Design  

---

# 🏗 Architecture

User → JWT Login → Secure Endpoint →  
Hybrid Memory → Context Builder →  
NeuralNode Agent → Tool Execution → Logging

---

# 🧠 Memory System

### 🔹 Short-Term Memory
- Stores last 5–6 messages per session
- Maintains conversational continuity

### 🔹 Long-Term Memory (Vector)
- Uses sentence-transformers
- Stored in ChromaDB
- Retrieves top-K relevant past messages

### 🔹 Context Builder
- Merges short + vector memory
- Builds structured prompt for LLM

---

# 🔐 Security Features

- JWT Authentication
- Password hashing (bcrypt)
- Session ownership validation
- Structured logging for audit trail
- Tool execution monitoring

---

# 🛠 Tech Stack

- Python 3.12
- FastAPI
- NeuralNode
- ChromaDB
- Sentence-Transformers
- python-jose (JWT)
- passlib (bcrypt)
- Docker

---

# 📈 Future Improvements
- SQLite / PostgreSQL integration
- Role-based tool access
- Rate limiting
- Token refresh system
- Redis caching layer
- Multi-agent architecture
- Web frontend dashboard
- Cloud deployment (AWS / GCP)

# 👨‍💻 Author
- Yassin sanad
- Ai Engineering & Machine learning engineering 
