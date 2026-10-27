# This is a textrank implementation in python for extraction text summarization and keyword extraction in english language. 
# It is based on the paper "TextRank: Bringing Order into Texts" by Rada Mihalcea and Paul Tarau.

import re
from math import log

def split_sentences(text: str)-> list[str]:
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    results = []
    for part in parts:
        if not part:
            continue
        if part[-1] not in ".!?":
            part += "."
        results.append(part)
    return results
#print(split_sentences("This is a sentence. This is another sentence! Is this a question? Yes, it is."))  # Output: ['This is a sentence.', 'This is another sentence!', 'Is this a question?', 'Yes, it is.']


STOPWORDS = {"the", "and", "is", "in", "to", "of", "a", "that", "it", "on", "for", "with", "as", "this", "by", "an", "be", "are", "from", "at", "or", "which"}

def tokenize(text: str, stopwords: set[str])-> list[str]:
    words = re.findall(r'\w+', text.lower())
    results = []
    for word in words:
        if word in stopwords:
            continue
        results.append(word)
    return results
#print(tokenize("The cat sleeps on the sofa.", STOPWORDS))  # Output: ['cat', 'sleeps', 'sofa']

def similarity(words1: list[str], words2: list[str]) -> float:
    if not words1 or not words2:
        return 0.0
    common_words = set(words1) & set(words2)
    #print(f"Common words: {common_words}")  
    denominator = log(len(words1)) + log(len(words2))
    
    if denominator == 0:
        return 0.0
    #cosinus de similarité
    cosinus = len(common_words) / denominator

    return cosinus
#print(similarity(['cat', 'sleeps', 'sofa'], ['dog', 'sleeps', 'bed']))

def build_similarity_graph(sentences: list[str], stopwords: set[str]) -> list[list[float]]:
    tokens = []
    for s in sentences:
        tokens.append(tokenize(s, stopwords))
    n = len(sentences)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0.0)
            else:
                row.append(similarity(tokens[i], tokens[j]))
        matrix.append(row)
    return matrix
#sents = ["The cat sleeps on the sofa.", "The dog sleeps on the bed.", "Stars shine at night."]
#print(build_similarity_graph(sents, STOPWORDS))
# la case [0][1] est > 0 ("sleeps" en commun), les cases impliquant la phrase 3 valent 0

def page_rank(matrix: list[list[float]], damping_factor: float = 0.85, max_iter: int = 100, tol: float = 1e-4) -> list[float]:
    n: int = len(matrix)
    if n == 0:
        return []

    scores = [1.0] * n

    sum_total_weight: list[float] = []
    for row in matrix:
        sum_total_weight.append(sum(row))

    for _ in range(max_iter):
        new_scores = []
        for i in range(n):
            incoming = 0.0
            for j in range(n):
                if j == i or sum_total_weight[j] == 0:
                    continue
                incoming += matrix[j][i] / sum_total_weight[j] * scores[j]
            new_scores.append((1 - damping_factor) + damping_factor * incoming)

        delta = max(abs(new_scores[i] - scores[i]) for i in range(n))
        scores = new_scores
        if delta < tol:
            break

    return scores