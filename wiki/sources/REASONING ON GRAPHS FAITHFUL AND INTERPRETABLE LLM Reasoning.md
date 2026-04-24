# 1. Source Document Template (`wiki/sources/reasoning-on-graphs.md`)

**Metadata**
* **Title**: Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning
* **Authors**: Linhao Luo, Yuan-Fang Li, Gholamreza Haffari, Shirui Pan
* **Year**: 2024
* **Venue**: ICLR 2024

**Structural Profile**
* **Class**: **Triple-Sufficient** (Utilizes standard $(h, r, t)$ triples from Freebase, but enhances reasoning through structured relation paths).

**Key Claims**
* Proposes **Reasoning on Graphs (RoG)**, a framework that synergizes LLMs with Knowledge Graphs (KGs) for faithful and interpretable reasoning.
* Introduces a **Planning-Retrieval-Reasoning** pipeline to mitigate LLM hallucinations and lack of up-to-date knowledge.
* Demonstrates that distilling KG structural knowledge into LLMs via "planning optimization" allows the model to generate valid reasoning plans even for arbitrary LLMs during inference.
* Achieves state-of-the-art (SOTA) performance on WebQSP and CWQ datasets.

**Methodology**
* **Planning Module**: Prompts the LLM to generate "Relation Paths" ($z$) as faithful plans. These are sequences of relations (e.g., `marry_to` $\rightarrow$ `father_of`) grounded by the KG.
* **Retrieval Module**: Uses a constrained breadth-first search (BFS) to find actual "Reasoning Paths" ($w_z$) in the KG that follow the generated relation paths starting from question entities.
* **Reasoning Module**: An LLM (using a Fusion-in-Decoder approach) takes the retrieved reasoning paths as context to generate the final answer and an interpretable explanation.
* **Optimization**:
    * **Planning Optimization**: Minimizes the KL divergence between the LLM's generated paths and the valid shortest paths in the KG.
    * **Retrieval-Reasoning Optimization**: Maximizes the probability of generating the correct answer based on retrieved paths.

**Experimental Benchmarks**
* **Datasets**: 
    * **WebQuestionsSP (WebQSP)**: Hits@1: 85.7%, F1: 70.8%
    * **Complex WebQuestions (CWQ)**: Hits@1: 62.6%, F1: 56.2%
* **Background KG**: Freebase (88M entities, 20k relations).

---

## 2. Concept Development (`wiki/concepts/`)

### Relation Path
A sequence of relations $z = \{r_1, r_2, \dots, r_l\}$ that represents a reasoning strategy or plan. Unlike raw triples, a relation path captures the semantic intent of a multi-hop query without requiring specific entity instances initially. See [[reasoning-on-graphs]].

### Reasoning Path
The grounded instance of a **Relation Path** within a KG, represented as $w_z = e_0 \xrightarrow{r_1} e_1 \xrightarrow{r_2} \dots \xrightarrow{r_l} e_l$. These paths serve as the factual evidence for LLM reasoning to prevent [[hallucination]].

### Planning-Retrieval-Reasoning
A three-stage RAG architecture where the model first generates a structural plan (relations), retrieves evidence matching that structure, and then synthesizes an answer. This differs from standard RAG which often retrieves based on semantic similarity of text rather than structural graph paths.

---

## 3. Global Index (`wiki/index.md`)

* **Structure-Adaptive**
    * [Empty]
* **Triple-Sufficient**
    * [[reasoning-on-graphs]] (RoG): Uses relation-path planning to guide triple retrieval.
    * ToG (referenced in paper)
    * GNN-RAG (referenced in paper)
* **Specialized/Temporal**
    * [Empty]

---

## 4. Ingestion Log (`wiki/log.md`)

| Date | Paper FileName | Primary Structural Type | Key Concepts Added |
| :--- | :--- | :--- | :--- |
| 2024-05-22 | reasoning-on-graphs.pdf | Triple-Sufficient | Relation Path, Planning-Retrieval-Reasoning, Faithful Reasoning |