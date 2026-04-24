# KG-RAG Research Wiki Ingestion: ShrinkE

## 1. Source Document Template (`wiki/sources/ShrinkE.md`)

**Metadata**
* **Title**: Shrinking Embeddings for Hyper-Relational Knowledge Graphs
* **Authors**: Bo Xiong, Mojtaba Nayyeri, Shirui Pan, Steffen Staab
* **Year**: 2023
* **Venue**: ACL (Association for Computational Linguistics)

**Structural Profile**
* **Class**: Hyper-relational / Geometric Embedding
* **Assumptions**: The model assumes that a hyper-relational fact consists of a primary triple contextualized by a set of key-value qualifiers. It explicitly adopts the **[[Qualifier Monotonicity]]** assumption: adding qualifiers can only narrow the possible answer set.

**Key Claims**
* **Qualifier Monotonicity Modeling**: Introduces "box shrinking" to geometrically ensure that qualifiers reduce the volume of the possible answer space.
* **Logical Pattern Capture**: Explicitly models qualifier-level inference patterns including implication, mutual exclusion, and intersection.
* **Efficiency**: Provides a neuro-symbolic approach that requires fewer parameters than heavy Transformer-based or GNN-based hyper-relational models while maintaining high performance.

**Methodology**
* **Primal Triple Embedding**: Maps the head entity point to a relation-specific box (query box) using a spatial-functional transformation (rotation $\Theta_r$ and translation $b_r$).
* **Qualifier Embedding**: Each qualifier $(k:v)$ is modeled as a shrinking operator $\mathcal{S}$ that produces a sub-box within the original query box. 
* **Reasoning Operator**: The final answer set is the intersection of all qualifier boxes.
* **Scoring Function**: Uses a specialized point-to-box distance function $D(e, Box)$ to measure the plausibility of a tail entity being within the shrunken box.

**Experimental Benchmarks**
* **Datasets**: WikiPeople, JF17K, and WD50K (including density-specific splits: WD50K-33, WD50K-66, WD50K-100).
* **Performance**: 
    *   Achieved state-of-the-art (SOTA) on JF17K (MRR: 0.589) and WD50K-100 (MRR: 0.695).
    *   Demonstrated that performance gains over triple-only baselines increase significantly as the ratio of qualifier-rich facts in the dataset increases.

---

## 2. Concept Development (`wiki/concepts/`)

### Hyper-relational Fact
*   **Definition**: A fact of the form $(h, r, t, Q)$ where $Q = \{(k_i : v_i)\}_{i=1}^m$ is a set of qualifiers (key-value pairs).
*   **Context**: ShrinkE treats the primary triple $(h, r, t)$ as the base unit and $Q$ as modifiers that restrict the validity of the triple.
*   **Related**: **[[Fact Atomicity]]**.

### Qualifier Monotonicity
*   **Definition**: A logical property where the set of valid tail entities for a query $q_1 = ((h, r, ?), Q_1)$ is a subset of the answers for $q_2 = ((h, r, ?), Q_2)$ if $Q_2 \subseteq Q_1$.
*   **Implementation**: In **[[ShrinkE]]**, this is represented by the geometric containment of boxes; shrunken boxes are strictly subsets of the primal relation box.

### Qualifier Implication
*   **Definition**: A pattern where the presence of qualifier $q_i$ logically necessitates qualifier $q_j$.
*   **Geometric Representation**: Modeled in ShrinkE when the box associated with $q_i$ is spatially contained within the box for $q_j$.

### Point-to-Box Distance
*   **Definition**: A scoring metric used in geometric embeddings to determine the proximity of an entity (point) to a concept (box).
*   **ShrinkE Implementation**: A two-part function that grows slowly when the point is inside the box and rapidly when outside, inversely correlated with box size.

---

## 3. Global Index (`wiki/index.md`)

### Hyper-Relational / Structure-Aware
*   **[[ShrinkE]]**: Geometric box-shrinking model for qualifier monotonicity.
*   **StarE**: Message-passing approach for hyper-relational KGs (Baseline).
*   **HINGE**: Convolutional approach for triple+qualifier compatibility (Baseline).

### Triple-Sufficient
*   **TransE**: Translation-based embedding (Foundational).
*   **RotatE**: Rotation-based embedding (Basis for ShrinkE's primal transformation).

---

## 4. Ingestion Log (`wiki/log.md`)

| Date | Paper FileName | Primary Structural Type | Key Concepts Added |
| :--- | :--- | :--- | :--- |
| 2024-05-22 | ShrinkE.pdf | Hyper-relational | Qualifier Monotonicity, Qualifier Implication, Point-to-Box Distance |