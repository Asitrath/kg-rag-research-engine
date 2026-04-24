# 1. Source Document Template (`wiki/sources/timer4.md`)

**Metadata**
* **Title**: TimeR4: Time-aware Retrieval-Augmented Large Language Models for Temporal Knowledge Graph Question Answering
* **Authors**: Xinying Qian, Ying Zhang, Yu Zhao, Baohang Zhou, Xuhui Sui, Li Zhang, Kehui Song
* **Year**: 2024
* **Venue**: EMNLP 2024

**Structural Profile**
* **Classification**: Specialized/Temporal
* **Fact Format**: Quadruple-based $(subject, predicate, object, timestamp)$

**Key Claims**
* **Temporal Hallucination**: Identifies that LLMs fail to reason through implicit temporal questions (e.g., "After the Danish Ministry...") without explicit timestamps.
* **Retrieval Neglect**: Current semantic retrieval (like BM25) ignores time constraints, leading to the retrieval of irrelevant facts that share semantic keywords but exist outside the question's time window.
* **TimeR4 Framework**: Proposes a "Retrieve-Rewrite-Retrieve-Rerank" pipeline to bridge the gap between implicit natural language and explicit temporal graph constraints.

**Methodology**
* **Retrieve-Rewrite**: Uses a Fact Knowledge Store (FKS) to retrieve background facts for implicit temporal references. An LLM then rewrites the question to include explicit timestamps (e.g., "After 2016-01-05").
* **Retrieve-Rerank**: 
    * **Contrastive Time-aware Retrieval**: Fine-tunes a retriever using three types of negatives (time incorrect, content incorrect, and both) to ensure the encoder captures temporal dimensions.
    * **Time-Filtering Rerank**: Implements a score-based reranking function $\phi(q, t)$ that combines semantic cosine similarity with a temporal distance normalization function.
* **Reasoning**: Fine-tunes LLaMA2-Chat-7B on retrieved quadruples formatted as natural language sequences.

**Experimental Benchmarks**
* **Datasets**: 
    * **MULTITQ**: 500K question-answer pairs (ICEWS05-15 based), multi-granularity.
    * **TimeQuestions**: 16K questions (Wikidata based).
* **Performance**: 
    * Achieved **72.8 Hits@1** on MULTITQ (relative gain of 47.8% over previous SOTA).
    * Achieved **78.1 Hits@1** on TimeQuestions (relative gain of 22.5%).

---

## 2. Concept Development (`wiki/concepts/temporal-reasoning.md`)

* **Implicit Temporal Constraints**: Natural language references to events ("after the Obama administration") that require mapping to specific time intervals before a KG can be queried. 
* **Time-Aware Retrieval**: A retrieval strategy where the embedding space or scoring function is explicitly constrained by the temporal distance between the query's time-scope and the fact's timestamp. In [[timer4]], this is achieved via contrastive learning with temporal negatives.
* **Fact Atomicity**: TimeR4 treats the temporal quadruple as the atomic unit of retrieval, ensuring the timestamp is never detached from the (s, p, o) triplet during the retrieval phase, preventing the semantic fragmentation often seen in flattened hyper-relational models.

---

## 3. Global Index (`wiki/index.md`)

* **Structure-Adaptive**
    * ...
* **Triple-Sufficient**
    * ...
* **Specialized/Temporal**
    * **TimeR4**: Retrieve-Rewrite-Retrieve-Rerank framework for temporal quadruples. [[timer4]]
    * **TempoQR**: Earlier TKGQA baseline utilizing context and entity embeddings.

---

## 4. Ingestion Log (`wiki/log.md`)

`2024-05-22 | timer4.md | Specialized/Temporal | Implicit-to-Explicit Rewriting, Time-aware Retrieval`