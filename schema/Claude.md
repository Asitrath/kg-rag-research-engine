# KG-RAG Research Wiki Schema

This guide defines the standards for ingesting research into the `wiki/` folder. Every time a paper is processed from `raw/`, follow these instructions precisely.

---

## 1. Source Document Template (`wiki/sources/[paper-name].md`)
Create a new file for each paper using this structure:

* **Metadata**: Title, Authors, Year, and Venue.
* **Structural Profile**: Classify the method based on its assumptions (e.g., Triple-based, Hyper-relational, Temporal-only, or Structure-adaptive).
* **Key Claims**: List the primary contributions (e.g., "Identifies the structural boundary problem").
* **Methodology**: Describe the retrieval pipeline, reasoning operators, and how it handles qualifiers (if at all).
* **Experimental Benchmarks**: Record the datasets used (e.g., LC-QUAD 2.0, WD50K) and reported performance.

---

## 2. Concept Development (`wiki/concepts/`)
If a paper introduces or heavily utilizes a technical concept, update or create the corresponding `.md` file. Use **`[[wikilinks]]`** to connect concepts to papers.

* **Structural Boundary**: The transition in a reasoning path between plain triples and qualifier-dependent facts.
* **Hyper-relational Fact**: Facts of the form $(h, r, t, \Omega)$ where $\Omega$ contains qualifier-value pairs.
* **Reification Costs**: The overhead of flattening hyper-relational facts, including path inflation, retrieval fragmentation, and semantic opacity.
* **Fact Atomicity**: The assumption that retrieved units preserve full fact structure rather than splitting qualifiers into fragments.

---

## 3. Global Index (`wiki/index.md`)
Maintain a master list of all papers categorized by their structural awareness:
* **Structure-Adaptive**: Papers that handle mixed structural forms (e.g., UniKG-RAG).
* **Triple-Sufficient**: Methods assuming binary (h, r, t) formats (e.g., ToG, GNN-RAG).
* **Specialized/Temporal**: Methods limited to specific qualifier types like time-scoped facts (e.g., TimeR4, Temp-R1).

---

## 4. Ingestion Log (`wiki/log.md`)
Record every ingestion event:
`[Date] | [Paper FileName] | [Primary Structural Type] | [Key Concepts Added]`