# TextRank Extractive Summarizer

A lightweight Python implementation of the **TextRank** algorithm used for graph-based sentence ranking and extractive text summarization. This project builds a text similarity graph using log-normalized common word overlaps and scores sentences using an iterative PageRank algorithm with damping factors.

Based on the original research paper:  
> **TextRank: Bringing Order into Texts** by Rada Mihalcea and Paul Tarau (2004).

### Key Features
* **Zero External Dependencies**: Implemented using pure Python standard modules (`re`, `math`).
* **Custom Sentence Tokenization**: Splitting logic handling punctuation and formatting.
* **Log-Normalized Similarity Metric**: Computes sentence edge weights based on shared tokens normalized by sentence lengths.
* **Iterative PageRank Engine**: Supports customizable damping factors (`damping_factor`), maximum iterations (`max_iter`), and convergence tolerance (`tol`).

### Architecture & Pipeline
1. `split_sentences(text)`: Cleans input and parses sentences by sentence-ending punctuation.
2. `tokenize(text, stopwords)`: Normalizes tokens to lowercase and removes custom stop words.
3. `similarity(words1, words2)`: Calculates content similarity between two token sets.
4. `build_similarity_graph(sentences, stopwords)`: Constructs an adjacency matrix representing sentence-to-sentence graph weights.
5. `page_rank(matrix)`: Iteratively updates sentence scores until convergence to rank top sentences for extraction.
