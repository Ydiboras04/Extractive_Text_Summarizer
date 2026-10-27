from textrank import summarize

def load_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    text = load_text("text.txt")
    print("=== SUMMARY (3 sentences) ===")
    for sentence in summarize(text, num_sentences=3):
        print("-", sentence.strip())
