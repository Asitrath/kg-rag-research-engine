# KG-RAG Research Wiki Schema Ingestion: Temp-R1

## 1. Source Document Template (`wiki/sources/temp-r1.md`)

*   **Metadata**:
    *   **Title**: Temp-R1: A Unified Autonomous Agent for Complex Temporal KGQA via Reverse Curriculum Reinforcement Learning
    *   **Authors**: Zhaoyan Gong, Zhiqiang Liu, Songze Li, Xiaoke Guo, Yuanxiang Liu, Xinle Deng, Zhizhen Liu, Lei Liang, Huajun Chen, Wen Zhang
    *   **Year**: 2026
    *   **Venue**: arXiv (cs.CL)
*   **Structural Profile**: **Specialized/Temporal** (Focuses on Temporal Knowledge Graphs where facts are quadruples including timestamps).
*   **Key Claims**:
    *   Identifies the **Overloaded Internal Reasoning** problem where a monolithic reasoning tag (e.g., `<think>`) causes cognitive overload in complex TKGQA.
    *   Proposes **Reverse Curriculum Learning** to mitigate the **Shortcut Trap** in reinforcement learning, forcing the model to master complex tool-chains on difficult questions before transitioning to easier ones.
    *   Establishes an autonomous agent that decouples reasoning into an expanded action space (`<plan>`, `<filter>`, `<rank>`) rather than following fixed workflows.
*   **Methodology**:
    *   **Retrieval Pipeline**: An autonomous rollout loop using a Markov Decision Process (MDP) framework. It interleaves internal reasoning with external `<search>` actions.
    *   **Reasoning Operators**:
        *   `<plan>`: Initial problem analysis and decomposition.
        *   `<filter>`: Semantic and temporal constraint application on retrieved facts.
        *   `<rank>`: Chronological ordering of filtered facts by timestamp.
        *   `<think>`: Traditional analytical reasoning.
    *   **Training Strategy**: A two-stage process: (1) Supervised Fine-Tuning (SFT) "Cold Start" using high-quality GPT-4o generated trajectories, followed by (2) Group Relative Policy Optimization (GRPO) reinforcement learning.
*   **Experimental Benchmarks**:
    *   **MULTITQ**: 0.780 Hits@1 (State-of-the-Art, 19.8% improvement on complex questions).
    *   **TIMELINEKGQA-CRON**: 0.705 Hits@1.
    *   **TIMELINEKGQA-ICEWS-ACTOR**: 0.642 Hits@1 (Out-of-domain evaluation).

---

## 2. Concept Development (`wiki/concepts/`)

*   **Overloaded Internal Reasoning**: A phenomenon in LLM agents where a single reasoning block is tasked with simultaneous strategy, search, semantic filtering, and ranking. This often leads to "cognitive overload," resulting in hallucinations or logical failures. Decoupling these into specific internal actions (like `<filter>` and `<rank>`) improves logical rigor.
*   **Reverse Curriculum Learning**: A counter-intuitive training strategy for RL agents. Instead of progressing from easy to hard tasks, the model is trained on high-difficulty environments first. This prevents the development of "path dependency" on simple shortcuts and compels the model to acquire sophisticated tool-chain logic.
*   **The Shortcut Trap**: A failure mode in reinforcement learning where an agent discovers a low-complexity path to a reward (e.g., a simple `<search>` -> `<answer>` pattern) and ceases to explore the complex tool combinations required for more difficult instances.
*   **Fact Atomicity**: Within [[Temp-R1]], fact atomicity is maintained by treating retrieved temporal quadruples (`<subject, predicate, object, timestamp>`) as the fundamental units for reasoning, which are then processed by specialized `<filter>` and `<rank>` actions to preserve temporal structure.

---

## 3. Global Index (`wiki/index.md`)

*   **Structure-Adaptive**:
    *   ...
*   **Triple-Sufficient**:
    *   ...
*   **Specialized/Temporal**:
    *   **[[Temp-R1]]**: Autonomous RL agent using reverse curriculum learning for complex TKGQA.
    *   **[[TimeR4]]**: A baseline method that explicitly reveals implicit time constraints through question rewriting.
    *   **[[TempAgent]]**: Adapts ReAct paradigms to the temporal domain with a specific toolkit.

---

## 4. Ingestion Log (`wiki/log.md`)

| Date | Paper FileName | Primary Structural Type | Key Concepts Added |
| :--- | :--- | :--- | :--- |
| 2025-05-22 | temp-r1.md | Specialized/Temporal | Reverse Curriculum Learning, Overloaded Internal Reasoning, Shortcut Trap |