# 🤖 05 - RAG Foundation

A Retrieval-Augmented Generation (RAG) application built using **Python**, **FastAPI**, and **Ollama**.

This project demonstrates how modern AI assistants reduce hallucinations by retrieving relevant knowledge before generating answers. It implements a complete RAG pipeline from scratch, including document chunking, embedding generation, semantic retrieval, prompt construction, and grounded answer generation without relying on LangChain, LlamaIndex, or external vector databases.

---

## 🎯 Objectives

- Understand Retrieval-Augmented Generation (RAG)
- Learn Document Chunking
- Build a Knowledge Base
- Generate Embeddings for Documents
- Implement Semantic Retrieval
- Build a Prompt Builder
- Ground LLM responses using retrieved context
- Reduce AI Hallucinations
- Build a production-style RAG backend architecture

---

## 🚀 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | FastAPI |
| Validation | Pydantic |
| LLM | Ollama + Qwen3 |
| Embedding Model | Ollama + nomic-embed-text |
| HTTP Client | Requests |
| Math Library | NumPy |

---

## ✨ Features

- RESTful RAG APIs
- Interactive Swagger UI
- Knowledge Base Loader
- Document Chunking
- Embedding Generation
- In-Memory Knowledge Repository
- Semantic Retrieval
- Top-K Search
- Prompt Builder
- Grounded Answer Generation
- Repository Pattern
- Service Layer Architecture
- Layered Architecture

---

## 🏛️ Architecture

```text
                          Client
                             │
                             ▼
                  FastAPI REST Controller
                             │
                             ▼
                        RAG Service
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
Retrieval Service     Prompt Builder      LLM Service
        │                    │                    │
        ▼                    ▼                    ▼
Embedding Service     Build Context      Ollama Client
        │                                      │
        ▼                                      ▼
Knowledge Repository                  Qwen3 Language Model
        │
        ▼
Chunk Repository
```

---

## 📂 Project Structure

```text
05-rag-foundation
│
├── clients/
├── config/
├── controllers/
├── knowledge/
├── models/
├── repository/
├── schemas/
├── services/
├── utils/
├── app.py
└── requirements.txt
```

---

## ▶️ Getting Started

### Start Ollama

```bash
ollama serve
```

Pull required models

```bash
ollama pull qwen3:8b

ollama pull nomic-embed-text
```

Run the application

```bash
uvicorn app:app --reload
```

Open Swagger

```text
http://localhost:8000/docs
```

---

## 📡 REST APIs

### POST `/api/knowledge/load`

Loads all text documents from the knowledge folder.

---

### GET `/api/knowledge/chunks`

Returns all generated knowledge chunks.

---

### POST `/api/rag/ask`

Ask questions against your knowledge base.

### Request

```json
{
    "question": "What is Amazon DynamoDB?"
}
```

### Response

```json
{
    "answer": "Amazon DynamoDB is a fully managed NoSQL database that provides fast and predictable performance at any scale."
}
```

---

## 🧠 RAG Workflow

Unlike a traditional LLM, Retrieval-Augmented Generation first searches for relevant knowledge before generating an answer.

```text
User Question
       │
       ▼
Generate Query Embedding
       │
       ▼
Semantic Search
       │
       ▼
Top-K Relevant Chunks
       │
       ▼
Prompt Builder
       │
       ▼
Large Language Model
       │
       ▼
Grounded Answer
```

---

## 📚 Knowledge Base

Instead of directly asking the LLM, documents are first loaded into a knowledge repository.

```text
Knowledge Folder
       │
       ▼
Read Documents
       │
       ▼
Split Into Chunks
       │
       ▼
Generate Embeddings
       │
       ▼
Store In Repository
```

Each document is converted into multiple searchable chunks.

---

## ✂️ Document Chunking

Large documents are divided into smaller chunks before embedding generation.

```text
Document

↓

Chunk 1

↓

Chunk 2

↓

Chunk 3

↓

Embedding
```

Chunking allows the retriever to return only the most relevant information instead of entire documents.

---

## 🔍 Semantic Retrieval

When a question is received, it is embedded and compared against every stored chunk.

```text
User Question
       │
       ▼
Query Embedding
       │
       ▼
Compare With Stored Embeddings
       │
       ▼
Cosine Similarity
       │
       ▼
Sort Descending
       │
       ▼
Top-K Chunks
```

Retrieval is based on meaning rather than exact keywords.

---

## 🧩 Prompt Builder

Instead of sending only the user's question to the LLM, the application constructs a grounded prompt.

```text
Question
      │
      ▼
Retrieved Context
      │
      ▼
Prompt Builder
      │
      ▼
Complete Prompt
```

Example

```text
Context

Amazon DynamoDB is a fully managed NoSQL database.

Question

What is DynamoDB?

Answer
```

This instructs the language model to answer using only the provided context.

---

## 🤖 Grounded Generation

The final prompt is sent to the language model.

```text
Prompt
      │
      ▼
Qwen3
      │
      ▼
Grounded Response
```

Unlike traditional prompting, the model is provided with relevant knowledge before generating its answer.

---

## 🚫 Reducing Hallucinations

Traditional LLM Workflow

```text
Question

↓

LLM Memory

↓

Generated Answer
```

RAG Workflow

```text
Question

↓

Retrieve Knowledge

↓

Build Context

↓

LLM

↓

Grounded Answer
```

The language model no longer relies solely on its internal knowledge. Instead, it answers using the retrieved context, significantly reducing hallucinations and improving factual accuracy.

---

## 🗄️ Repository Pattern

The application separates storage logic from business logic.

```python
knowledge_repository.save(chunk)

knowledge_repository.find_all()

knowledge_repository.clear()
```

This allows the in-memory repository to be replaced later with production vector databases such as FAISS, ChromaDB, Pinecone, or Milvus without changing the service layer.

---

## 🧠 Concepts Explored

- Retrieval-Augmented Generation (RAG)
- Document Chunking
- Knowledge Base
- Embeddings
- Semantic Search
- Cosine Similarity
- Top-K Retrieval
- Prompt Engineering
- Grounded Generation
- Hallucination Reduction
- Repository Pattern
- Object-Oriented Design
- Local LLMs
- FastAPI
- Ollama
- Layered Architecture

---

## 💡 Key Learnings

Building this project helped me understand:

- How Retrieval-Augmented Generation works internally
- Why document chunking improves retrieval quality
- How embeddings enable semantic search
- How Top-K retrieval selects the most relevant knowledge
- How prompt construction grounds LLM responses
- How RAG significantly reduces hallucinations by providing trusted context
- How modern AI assistants combine retrieval and generation
- How to build a complete production-style RAG pipeline using FastAPI and Ollama without relying on AI orchestration frameworks

This project focuses on understanding the internal building blocks of Retrieval-Augmented Generation before introducing Vector Databases, Hybrid Search, Re-Ranking, Advanced RAG, and AI Agents in subsequent projects.