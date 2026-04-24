# KG-RAG Research Wiki Ingestion: TempAgent

## 1. Source Document Template (`wiki/sources/temp-agent.md`)

**Metadata**
* **Title**: Time-aware ReAct Agent for Temporal Knowledge Graph Question Answering
* **Authors**: Qianyi Hu, Xinhui Tu, Cong Guo, Shunping Zhang
* **Year**: 2025
* **Venue**: NAACL 2025 (Findings)

**Structural Profile**
* **Class**: Specialized/Temporal
* **Structural Assumption**: Temporal Knowledge Graph (TKG) tuples represented as $\langle e, r, e', t \rangle$, where $t$ denotes a timestamp.

**Key Claims**
* Identifies the "absence of temporal constraints in retrieval" as a critical failure point for general LLM agents (like ReAct) in TKGQA tasks.
* Proposes **TempAgent**, an autonomous framework that integrates temporal constraints directly into the retrieval-augmented generation (RAG) loop.
* Demonstrates that multi-granularity time-filtering (day, month, year) significantly reduces retrieval noise and LLM hallucinations.

**Methodology**
* **Framework**: An agent-based paradigm using an iterative "Thought-Action-Observation" loop (based on ReAct).
* **Retrieval Toolbox**: A suite of 10 specialized tools (e.g., `SearchAfterDay`, `SearchOnMonth`, `SearchBeforeYear`) that apply hard filters to the knowledge base before performing semantic similarity searches.
* **Reasoning Operators**: The LLM dynamically generates queries and selects timestamps to invoke specific tools. The process is iterative, allowing the agent to decompose complex temporal queries (e.g., "who visited first after [Event A]") into sequential sub-tasks.
* **Qualifier Handling**: Specifically handles temporal qualifiers by treating time as a hard filter ($G_{filter}$) applied to the Knowledge Graph ($G$) before vector similarity calculation ($top_k$).

**Experimental Benchmarks**
* **Datasets**: MultiTQ (multi-granularity TKGQA), CronQuestions (standard TKGQA).
* **Performance**: 
    *   Achieved **70.2% Hits@1** on MultiTQ using GPT-4.
    *   Reported a **41.3% improvement** over the MultiQA baseline and **32.2%** over the ARI (Abstract Reasoning Induction) method.

---

## 2. Concept Development (`wiki/concepts/`)

* **Multi-granularity Time-Filtering**: The process of restricting retrieval to specific subsets of a knowledge base based on temporal resolution (day, month, or year) provided in a query. Used in [[temp-agent]] to discard irrelevant facts before semantic matching.
* **Temporal Constraint Retrieval**: A retrieval strategy where technical qualifiers (timestamps) are used as hard filters rather than soft semantic features. This mitigates the "semantic opacity" of temporal data in standard vector-only RAG.
* **Zero-shot TKGQA**: The application of LLM agents to temporal knowledge graphs without task-specific fine-tuning, relying instead on specialized tool-use and prompting. Featured in [[temp-agent]].

---

## 3. Global Index (`wiki/index.md`)

* **Specialized/Temporal**
    * [[temp-agent]]: Time-aware ReAct Agent for Temporal Knowledge Graph Question Answering (NAACL 2025).
* **Structure-Adaptive**
    * (Other entries...)
* **Triple-Sufficient**
    * (Other entries...)

---

## 4. Ingestion Log (`wiki/log.md`)

`2024-05-22 | temp-agent.md | Specialized/Temporal | Multi-granularity Time-Filtering, Temporal Constraint Retrieval, Zero-shot TKGQA`