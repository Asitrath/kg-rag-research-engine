# wiki/sources/holmes-2024.md

**Metadata**
* **Title**: HOLMES: Hyper-Relational Knowledge Graphs for Multi-hop Question Answering using LLMs
* **Authors**: Pranoy Panda, Ankush Agarwal, Chaitanya Devaguptapu, Manohar Kaul, Prathosh A P
* **Year**: 2024
* **Venue**: arXiv (cs.CL)

**Structural Profile**
* **Class**: Hyper-relational
* **Primary Representation**: Hyper triples defined as $(e_s, r, e_o, a)$, where $a \in A_{dt}$ represents document title attributes providing contextual qualifiers to standard $(h, r, t)$ triples.

**Key Claims**
* **Contextual Ambiguity Resolution**: Argues that standard triples are query-agnostic and ambiguous; utilizes a context-aware **[[Hyper-relational Fact]]** structure to preserve validity.
* **Token Efficiency**: Achieves up to 67% reduction in input tokens compared to state-of-the-art (SoTA) methods by distilling KGs into query-relevant subgraphs.
* **Performance Superiority**: Reports significant gains in Exact Match (EM) and F1 scores (18.7% to 26% improvement) on multi-hop datasets like HotpotQA and MuSiQue.

**Methodology**
1.  **Entity-Document Graph Construction**: Builds a bipartite graph linking named entities to their source documents.
2.  **Structured Information Extraction**: Uses a level-order traversal (breadth-first) starting from query entities to extract triples, which are then elevated to hyper triples by appending source document metadata.
3.  **Knowledge Schema Construction**: Derives a query-aligned schema from the question and an "Auxiliary Graph Schema" (pre-computed from in-domain questions) to filter irrelevant relations.
4.  **Pruning**: Refines the KG by calculating cosine similarity between relation embeddings in the graph and the query-aligned schema.
5.  **Reasoning**: Verbalizes the pruned hyper-relational graph into natural language for the Reader LLM, including a "Complementary Fact Retrieval" step to mitigate extraction omissions.

**Experimental Benchmarks**
* **Datasets**: HotpotQA (Bridge and Comparison questions), MuSiQue (2-hop, 3-hop, and 4-hop).
* **Models**: GPT-3.5, GPT-4, Gemini-Pro.
* **Reported Performance**:
    *   HotpotQA (GPT-4): 0.66 EM (vs. 0.55 for StructQA).
    *   MuSiQue (GPT-4): 0.48 EM (vs. 0.42 for StructQA).
    *   Maintains performance stability across increasing hop counts (2 to 4 hops) compared to baseline degradation.

---

# wiki/concepts/Hyper-relational-Fact.md

**Definition**: A **[[Hyper-relational Fact]]** is an extension of a binary relation that includes additional context or qualifiers. In the context of [[holmes-2024]], this is formalized as $(e_s, r, e_o, a)$, where $e_s$ and $e_o$ are entities, $r$ is the relation, and $a$ is an attribute set (specifically document titles) that serves as a contextual anchor.

**Role in RAG**:
*   Prevents the "ambiguity problem" where a triple like `(Apple, prices rose, 10%)` lacks the context to distinguish between the fruit and the tech company.
*   Enables **[[Fact Atomicity]]** by ensuring the LLM receives the triple and its provenance/qualifier as a single unit.

---

# wiki/concepts/Fact-Atomicity.md

**Definition**: The principle that a retrieved knowledge unit should contain all necessary qualifiers and context required for its interpretation without needing to cross-reference fragmented triples.

**Application**: [[holmes-2024]] enforces this by transforming unstructured text into hyper-relational structures. By appending document titles as attributes to every triple, the method avoids the **[[Reification Costs]]** associated with splitting context into separate nodes or losing it during pruning.

---

# wiki/concepts/Reification-Costs.md

**Definition**: The computational and cognitive overhead incurred when complex facts are broken down into simpler, binary triples. This often leads to path inflation and retrieval fragmentation.

**In [[holmes-2024]]**: The authors argue that previous methods like StructQA suffer from high reification costs by outputting redundant information or long prompts. HOLMES minimizes these costs through a "query-aligned graph schema" that prunes the graph before it reaches the LLM, reducing the token burden (up to 67% fewer tokens) and the "filtering burden" on the reader model.

---

# wiki/index.md

## Structural Awareness Categorization

### Structure-Adaptive
*   **[[UniKG-RAG]]**: Handles mixed structural forms.
*   **[[holmes-2024]]**: Dynamically constructs query-focused hyper-relational subgraphs from unstructured text.

### Triple-Sufficient
*   **ToG**: Token-based graph reasoning.
*   **GNN-RAG**: Neural-graph retrieval.

### Specialized/Hyper-relational
*   **[[holmes-2024]]**: Specifically targets multi-hop reasoning using document-level qualifiers.

---

# wiki/log.md

| Date | Paper FileName | Primary Structural Type | Key Concepts Added |
| :--- | :--- | :--- | :--- |
| 2024-06-10 | [[holmes-2024]] | Hyper-relational | [[Hyper-relational Fact]], [[Fact Atomicity]], [[Reification Costs]] |