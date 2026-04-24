import os
import time
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# 1. Setup paths
BASE_DIR = Path(__file__).resolve().parent
WIKI_DIR = BASE_DIR / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
CONCEPTS_DIR = WIKI_DIR / "concepts"
SYNTHESIS_DIR = WIKI_DIR / "synthesis"

# 2. Load environment and initialize
load_dotenv(BASE_DIR / ".env")
client = genai.Client()

def get_full_wiki_context():
    """Aggregates all wiki content with encoding error handling."""
    context = "--- FULL RESEARCH WIKI CONTEXT ---\n\n"
    
    # Add Source Summaries
    if SOURCES_DIR.exists():
        for file in SOURCES_DIR.glob("*.md"):
            # Added errors="ignore" to prevent UnicodeDecodeError from special characters
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                context += f"## SOURCE: {file.stem}\n{f.read()}\n\n"
                
    # Add Concept Notes
    if CONCEPTS_DIR.exists():
        for file in CONCEPTS_DIR.glob("*.md"):
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                context += f"## CONCEPT: {file.stem}\n{f.read()}\n\n"
                
    return context

def generate_synthesis():
    print("Gathering all wiki notes...")
    full_context = get_full_wiki_context()
    
    if len(full_context) < 500:
        print("Your wiki is too small to synthesize. Ingest more papers first!")
        return

    # Create synthesis directory
    SYNTHESIS_DIR.mkdir(exist_ok=True)

    # TASK 1: Structural Comparison Table
    print("Generating Structural Comparison Table...")
    table_prompt = f"""
    Using the provided wiki context, create a detailed markdown table comparing the KG-RAG methods.
    
    Columns: [Method], [Structural Focus (Triple/Hyper/Mixed)], [Key Innovation], [Reification Awareness].
    
    In the 'Reification Awareness' column, specifically note if the method addresses:
    1. Path Inflation
    2. Retrieval Fragmentation
    3. Semantic Opacity
    (As defined in the UniKG-RAG paper).
    
    CONTEXT:
    {full_context}
    """
    
    table_response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=table_prompt
    )
    
    with open(SYNTHESIS_DIR / "structural_comparison.md", "w", encoding="utf-8") as f:
        f.write("# Comparative Analysis: Structural Awareness in KG-RAG\n\n")
        f.write(table_response.text)

    # RATE LIMIT PROTECTION: Wait 10 seconds between large requests
    print("Cooling down for 10 seconds to respect API limits...")
    time.sleep(10)

    # TASK 2: Literature Review Draft
    print("Drafting formal Literature Review...")
    review_prompt = f"""
    Write a formal academic literature review focusing on the transition from triple-based to structure-adaptive KG-RAG.
    
    Structure:
    1. **Introduction**: Evolution of KG-RAG systems.
    2. **Triple-Based Paradigms**: Analysis of methods like ToG and GNN-RAG.
    3. **Specialized Domains**: How temporal and hyper-relational baselines handle complexity.
    4. **The Structural Boundary Challenge**: Deep dive into the findings of UniKG-RAG regarding heterogeneous compositionality.
    5. **Critical Synthesis**: Comparison of 'Fact Atomicity' vs 'Reification'.
    
    Use [[wikilinks]] for all papers and concepts to ensure it works perfectly in Obsidian.
    
    CONTEXT:
    {full_context}
    """
    
    review_response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=review_prompt
    )
    
    with open(SYNTHESIS_DIR / "literature_review_draft.md", "w", encoding="utf-8") as f:
        f.write("# Literature Review: The Landscape of Heterogeneous KG-RAG\n\n")
        f.write(review_response.text)
    
    print(f"\nSuccess! Synthesis files created in {SYNTHESIS_DIR}")

if __name__ == "__main__":
    generate_synthesis()