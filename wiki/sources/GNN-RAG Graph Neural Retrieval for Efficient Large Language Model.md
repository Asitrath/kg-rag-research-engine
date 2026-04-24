# KG-RAG Research Wiki Schema Ingestion

## 1. Source Document Template (`wiki/sources/gnn-rag.md`)

**Metadata**
* **Title**: GNN-RAG: Graph Neural Retrieval for Efficient Large Language Model Reasoning on Knowledge Graphs
* **Authors**: Costas Mavromatis, George Karypis
* **Year**: 2025
* **Venue**: ACL 2025 (Findings)

**Structural Profile**
* **Classification**: **Triple-Sufficient**. The framework assumes the KG represents factual knowledge in the form of triplets $(head, relation, tail)$ and focuses on retrieving shortest paths between entities.

**Key Claims**
* **GNNs as Efficient Retrievers**: Demonstrates that lightweight GNNs can replace costly LLM calls for KG traversal and path generation.
* **Superiority in Multi-hop/Multi-entity Tasks**: Outperforms LLM-based retrieval approaches (like ToG or RoG) by 8.9�15.5% points at answer F1 on complex questions.
* **Token Efficiency**: Surpasses long-context inference performance while utilizing 9� fewer KG tokens.
* **LLM Agnostic**: Shows that a 7B tuned LLM (Llama-2) paired with GNN-RAG can match or exceed GPT-4 performance.

**Methodology**
1.  **Dense Subgraph Retrieval**: Extracts a question-specific subgraph using entity linking and Pagerank Nibble.
2.  **GNN Reasoning (Retrieval Phase)**: A multi-layer GNN assigns importance weights to nodes based on their relevance to decomposed question embeddings.
3.  **Iterative Traversal**: Implements a "reset" mechanism at intermediate layers to revisit question entities with deep embeddings, refining the traversal.
4.  **Path Extraction**: Identifies the top-scoring candidate answer nodes and extracts the shortest paths connecting them to the original question entities.
5.  **Verbalized RAG**: These paths are converted to natural language and provided to a downstream LLM for final answer generation.
6.  **Augmentation & Routing**: Optionally combines GNN retrieval with semantic parsing (RA) or routes queries between GNN-RAG and long-context retrieval based on response alignment.

**Experimental Benchmarks**
* **WebQSP**: 71.3 F1 (GNN-RAG), 73.5 F1 (GNN-RAG+RA).
* **CWQ (Complex WebQuestions)**: 59.4 F1 (GNN-RAG), 60.4 F1 (GNN-RAG+RA).
* **MetaQA-3**: 98.6 H@1.

---

## 2. Concept Development (`wiki/concepts/`)

*   **Fact Atomicity**: GNN-RAG maintains [[Fact Atomicity]] by retrieving and verbalizing complete shortest paths (sequences of triplets) rather than isolated entities, ensuring the LLM receives the full relational context.
*   **Iterative KG Traversal**: A technique introduced in [[gnn-rag]] where the node probability vector is reset to the starting entities at a specific layer (e.g., $l=L/2$). This allows the GNN to re-evaluate node importance using "refined" deep graph embeddings.
*   **GNN-based Retrieval**: The core contribution of [[gnn-rag]], positioning GNNs not as the reasoner, but as a specialized filter that identifies candidate paths for a larger LLM, addressing the "needle in a haystack" problem in large-scale KGs.
*   **Path Verbalization**: The process of converting retrieved graph paths (nodes and edges) into structured natural language templates (e.g., "Entity A -> Relation B -> Entity C") to mitigate the modality mismatch between graphs and LLMs.

---

## 3. Global Index (`wiki/index.md`)

*   **Triple-Sufficient**
    *   ToG (Sun et al., 2024)
    *   RoG (Luo et al., 2024a)
    *   **GNN-RAG (Mavromatis & Karypis, 2025)**: Utilizes GNNs for efficient path-based retrieval on triple-based graphs.
*   **Structure-Adaptive**
    *   UniKG-RAG (pending ingestion)
*   **Specialized/Temporal**
    *   (Existing entries)

---

## 4. Ingestion Log (`wiki/log.md`)

| Date | Paper FileName | Primary Structural Type | Key Concepts Added |
| :--- | :--- | :--- | :--- |
| 2024-05-20 | gnn-rag.md | Triple-Sufficient | GNN-based Retrieval, Iterative KG Traversal, Path Verbalization |