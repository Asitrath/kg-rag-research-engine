# Wiki Lint Report - 1776970284.1356258

This Research Lint report evaluates the current state of the KG-RAG Research Wiki based on the provided source summaries and concept definitions.

### 1. Identification of Logical Gaps
The **Structural Boundary** problem (defined in UniKG-RAG) refers to the performance drop and "path inflation" that occurs when a system restricted to triples $(h, r, t)$ attempts to process hyper-relational data via reification.

*   **Triple-Sufficient Baselines (ToG, GNN-RAG, RoG):** These models all exhibit a significant logical gap. They claim efficiency in "multi-hop" reasoning but fail to account for the fact that a single-hop hyper-relational query (e.g., "Who was the CEO of X *in 2010*?") becomes a multi-hop query in their architectures due to triple-flattening. 
*   **Specialized Temporal Baselines (Temp-R1, TempAgent, TimeR4):** These address the boundary for **temporal** data but represent a secondary logical gap: they are **"Structural Silos."** While they handle quadruples $(s, p, o, t)$, they lack the mechanism to handle general-purpose qualifiers (e.g., *role, location, or coordinates*) found in models like ShrinkE or UniKG-RAG.
*   **GNN-RAG Specific Gap:** GNN-RAG focuses on "shortest paths." In a hyper-relational context, the "shortest path" between two entities may be a single hyper-edge, but GNN-RAG will perceive it as a longer path through a reified dummy node, leading to a sub-optimal retrieval ranking.

### 2. Terminology Consistency
There is a minor but critical inconsistency in how auxiliary fact data is described:

*   **Qualifiers:** Used consistently in `galkin-stare-2020`, `ShrinkE`, and `UniKG-RAG`. This is the standard term in Wikidata-style modeling.
*   **Attributes:** Used in `holmes-2024` (specifically referring to document titles). 
*   **Modifiers:** Used in the `ShrinkE` summary ("qualifiers as modifiers").
*   **Technical Qualifiers:** Used in `TempAgent`.

**Recommendation:** Adopt **"Qualifiers"** as the primary term for the key-value pairs in a hyper-relational fact. Update `holmes-2024` to note that it treats *document metadata* as a specific subset of qualifiers (Attributes).

### 3. Link Suggestions
To better integrate the structural arguments, add the following [[wikilinks]]:

1.  In **`gnn-rag.md`**: Link "Triple-Sufficient" to **[[Fact-Atomicity]]** to highlight that its retrieval unit is restricted, potentially causing fragmentation.
2.  In **`holmes-2024.md`**: Link "Contextual Ambiguity Resolution" to **[[Reification-Costs]]**, as the paper argues that its method avoids the overhead inherent in standard triple processing.
3.  In **`think-on-graph.md`**: Add a "Comparison" section linking to **[[reasoning-on-graphs]]** (RoG), as both use LLM-guided path exploration but differ in planning vs. search-based execution.
4.  In **`ShrinkE.md`**: Link "Geometric containment" to **[[Fact-Atomicity]]**. ShrinkE is one of the few embedding models that maintains atomicity by not breaking facts into triples.
5.  In **`index.md`**: Create a cross-link between **[[Temp-R1]]** and **[[temp-agent.md]]** under a new sub-heading: "Autonomous Agents for TKGQA."

### 4. Contradiction Detection
*   **GNN-RAG vs. UniKG-RAG:** `gnn-rag.md` claims "Superiority in Multi-hop/Multi-entity Tasks" and "Token Efficiency." However, `UniKG-RAG` proves that triple-sufficient models (like GNN-RAG) suffer from **Path Inflation (1.70x)** and **Semantic Opacity (24.6% vacuous nodes)** when dealing with complex facts. GNN-RAG's claim of "efficiency" is only true within the "Triple-Sufficient" silo; it is demonstrably *inefficient* when the data complexity crosses the Structural Boundary.
*   **HOLMES vs. Fact-Atomicity:** `holmes-2024` claims to achieve "Fact Atomicity" by appending document titles. However, the definition of Fact Atomicity in `UniKG-RAG` requires preserving *all* qualifiers. HOLMES only preserves *provenance* (the document title), which is a partial implementation of atomicity. If a query requires a temporal qualifier (e.g., "Who was the point guard *in 1995*?") and that date isn't in the document title, HOLMES fails the atomicity test.
*   **ToG vs. Knowledge Traceability:** `ToG` claims high "Knowledge Traceability" because paths are triples. However, if a fact is hyper-relational and has been reified, the "traceable" path includes "vacuous nodes" (reification IDs) that have no natural language meaning, contradicting the claim of human-readable interpretability.