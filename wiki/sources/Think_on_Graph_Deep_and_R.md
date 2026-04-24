# KG-RAG Research Wiki Ingestion: Think-on-Graph (ToG)

---

## 1. Source Document Template (`wiki/sources/think-on-graph.md`)

**Metadata**
* **Title**: Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph
* **Authors**: Jiashuo Sun, Chengjin Xu, Lumingyuan Tang, Saizhuo Wang, Chen Lin, Yeyun Gong, Lionel M. Ni, Heung-Yeung Shum, Jian Guo
* **Year**: 2024
* **Venue**: ICLR 2024

**Structural Profile**
* **Class**: Triple-Sufficient. 
* **Reasoning**: The method explicitly operates on standard $(h, r, t)$ triples. It models reasoning as a path discovery problem through a sequence of entities and relations without addressing hyper-relational qualifiers or complex n-ary structures.

**Key Claims**
* **Beam Search Reasoning**: Introduces an iterative beam search algorithm to explore KGs, identifying the most promising reasoning paths.
* **Knowledge Traceability**: Enables the tracing of model outputs back to explicit KG paths, reducing "black-box" opacity.
* **Knowledge Correctability**: Demonstrates that errors in the KG can be identified and corrected through LLM interaction (knowledge infusion).
* **Efficiency with Small Models**: Claims that small LLMs (e.g., Llama-2-70B) using ToG can outperform larger models like GPT-4 on complex reasoning tasks.
* **Plug-and-Play**: A training-free framework that works across different LLMs and KGs without additional fine-tuning.

**Methodology**
The ToG pipeline consists of three iterative phases:
1.  **Initialization**: LLM extracts topic entities $E^0$ from the natural language question.
2.  **Exploration (Beam Search)**:
    *   **Relation Exploration**: For each path, the LLM-as-agent searches for candidate relations and prunes them based on relevance to the query.
    *   **Entity Exploration**: The agent identifies the most relevant tail entities for the selected relations.
3.  **Reasoning**: After each hop, the LLM evaluates the current top-$N$ reasoning paths. If the information is sufficient, it generates the final answer; otherwise, it increments the search depth $D$ (up to $D_{max}$).

**Experimental Benchmarks**
* **Datasets**: Evaluated on 9 datasets across Multi-hop KBQA (CWQ, WebQSP, GrailQA, QALD10-en), Single-hop KBQA (Simple Questions), Open-Domain QA (WebQuestions), Slot Filling (T-REx, Zero-Shot RE), and Fact Checking (Creak).
* **Performance**: Achieved overall SOTA in 6 out of 9 datasets. Notably outperformed GPT-4 on CWQ and WebQSP when using GPT-4 as the backbone with the ToG framework.

---

## 2. Concept Development (`wiki/concepts/`)

### Beam Search Reasoning
The application of the [[beam search]] algorithm to Knowledge Graph exploration, where a Large Language Model (LLM) acts as the pruning agent to maintain a set of $N$ most-likely reasoning paths. This prevents the exponential expansion of paths while ensuring the retrieval stays contextually relevant to the question. Introduced in [[think-on-graph]].

### Knowledge Traceability
The ability of a system to provide an explicit, human-readable provenance for its conclusions. In the context of [[think-on-graph]], this is achieved through the generation of reasoning paths comprised of KG triples $(h, r, t)$, allowing users to verify the factual basis of an LLM's response.

### Knowledge Correctability
A property of RAG systems where the interaction between an LLM and an external KG allows for the identification of outdated or incorrect facts. As seen in [[think-on-graph]], the model can perform "self-evaluation" to find suspicious triples and suggest updates to the KG (knowledge infusion).

---

## 3. Global Index (`wiki/index.md`)

* **Structure-Adaptive**
    * (Empty)
* **Triple-Sufficient**
    * [[think-on-graph]] (ToG): Iterative beam search on triples for deep reasoning.
* **Specialized/Temporal**
    * (Empty)

---

## 4. Ingestion Log (`wiki/log.md`)

| Date | Paper FileName | Primary Structural Type | Key Concepts Added |
| :--- | :--- | :--- | :--- |
| 2024-05-22 | think-on-graph.pdf | Triple-Sufficient | Beam Search Reasoning, Knowledge Traceability, Knowledge Correctability |