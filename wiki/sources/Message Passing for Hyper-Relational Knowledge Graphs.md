# 1. Source Document Template: `wiki/sources/galkin-stare-2020.md`

**Metadata**
* **Title**: Message Passing for Hyper-Relational Knowledge Graphs
* **Authors**: Mikhail Galkin, Priyansh Trivedi, Gaurav Maheshwari, Ricardo Usbeck, Jens Lehmann
* **Year**: 2020
* **Venue**: arXiv:2009.10847 [cs.LG] (Preprint)

**Structural Profile**
* **Classification**: Hyper-relational
* **Primary Representation**: Hyper-relational facts represented as a main triple $(s, r, o)$ associated with a set of qualifier pairs $Q = \{(qr_i, qv_i)\}$.

**Key Claims**
* **Introduction of STARE**: The first GNN-based encoder capable of modeling hyper-relational KGs with an arbitrary number of qualifiers while preserving the semantic distinction between the main triple and auxiliary information.
* **Benchmark Flaw Identification**: Demonstrates that existing hyper-relational datasets like JF17K and WikiPeople suffer from significant test leakage and over-reliance on literals.
* **Dataset Contribution**: Introduces **WD50K**, a high-quality Wikidata-based dataset specifically designed to evaluate link prediction in hyper-relational contexts without the flaws of previous benchmarks.
* **Qualifier Utility**: Proves that leveraging qualifiers can improve Link Prediction (LP) performance by up to 25 MRR points compared to triple-only baselines.

**Methodology**
* **Encoder (STARE)**: Extends standard multi-relational GNN message passing. It computes a qualifier vector $h_q$ by aggregating qualifier relation-entity pairs via a composition function $\phi_q$ and a summation. This vector is then integrated with the main relation embedding $h_r$ using a weight-controlled function $\gamma$.
* **Retrieval/Reasoning**: Unlike reification methods that flatten facts into multiple triples, STARE treats the hyper-relational fact as an atomic unit.
* **Decoder**: Uses a Transformer-based decoder that linearizes the query $(s, r, Q)$ and utilizes the updated embeddings to predict the missing object $o$.

**Experimental Benchmarks**
* **Datasets**: WikiPeople, JF17K, WD50K (and its subsets 33, 66, 100).
* **Baseline Comparisons**: m-TransH, RAE, NaLP, and HINGE.
* **Key Result**: STARE (H) + Transformer (H) consistently outperforms HINGE and NaLP across all WD50K variants, particularly as the ratio of qualified facts increases.

---

## 2. Concept Development: `wiki/concepts/`

### **Hyper-relational Fact**
(Update to existing or create new)
* **Definition**: A fact that extends the binary triple $(h, r, t)$ with a set of key-value pairs $\Omega$ (qualifiers) that provide context, restrict validity, or disambiguate the fact.
* **Formalization**: Typically represented as $(s, r, o, Q)$ where $Q = \{(qr_1, qv_1), \dots, (qr_n, qv_n)\}$.
* **Significance**: Proposed by [[galkin-stare-2020]] as a more intuitive model than n-ary representations, which often lose the "main triple" focus.

### **Reification Costs**
(Update to existing or create new)
* **Definition**: The negative impact of converting complex graph structures into binary triples.
* **Paper Context**: [[galkin-stare-2020]] identifies "semantic opacity" and "combinatorial explosion" as primary costs. Specifically, star-to-clique conversions (m-TransH) result in a permanent loss of entity-relation attribution.
* **Fragmentation**: Reification often breaks [[Fact Atomicity]], making it harder for GNNs to aggregate information belonging to a single complex statement.

### **Fact Atomicity**
(New Concept)
* **Definition**: The principle that a hyper-relational statement should be processed as a single structural unit rather than being decomposed into independent key-value pairs.
* **Implementation**: [[galkin-stare-2020]] achieves this through their qualifier aggregation function $h_q$, ensuring that all qualifiers influence the representation of the specific relation instance between a subject and object.

---

## 3. Global Index: `wiki/index.md`

**Hyper-Relational / Specialized**
* **[[galkin-stare-2020]]**: *Message Passing for Hyper-Relational Knowledge Graphs*. (Introduces STARE and WD50K).
* **HINGE**: (Referenced as baseline) Convolutional approach for hyper-relational facts.
* **NaLP**: (Referenced as baseline) Convolutional model that breaks facts into quintuples.

**Triple-Sufficient**
* **CompGCN**: (Basis for STARE) Multi-relational GNN for triple-based graphs.

---

## 4. Ingestion Log: `wiki/log.md`

| Date | Paper FileName | Primary Structural Type | Key Concepts Added |
| :--- | :--- | :--- | :--- |
| 2024-05-22 | galkin-stare-2020.md | Hyper-relational | STARE, WD50K, Fact Atomicity, Qualifier Aggregation |