from src.core.dataset_loaders import load_raw_text_data
from src.preprocessing.simple_tokenizer import SimpleTokenizer
from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer

def test_tokenizers():
    sentences = [
        "Hello, world! This is a test.",
        "NLP is fascinating... isn't it?",
        "Let's see how it handles 123 numbers and punctuation!"
    ]

    simple_tokenizer = SimpleTokenizer()
    regex_tokenizer = RegexTokenizer()

    print("=== Testing with Sample Sentences ===")
    print("\n--- SimpleTokenizer ---")
    for sentence in sentences:
        print(f"Input: {sentence}")
        print("Tokens:", simple_tokenizer.tokenize(sentence))
        print()

    print("\n--- RegexTokenizer ---")
    for sentence in sentences:
        print(f"Input: {sentence}")
        print("Tokens:", regex_tokenizer.tokenize(sentence))
        print()

def test_tokenization_with_ud_ewt():
    dataset_path = r"F:\NLP\data\en_ewt-ud-train.txt"
    raw_text = load_raw_text_data(dataset_path)

    if not raw_text:
        print("[ERROR] Dataset could not be loaded.")
        return

    sample_text = raw_text[:500]
    print("\n=== Testing Tokenization with UD_English-EWT Dataset ===")
    print(f"Original sample (first 100 chars): {sample_text[:100]}...\n")

    # Test with SimpleTokenizer
    simple_tokenizer = SimpleTokenizer()
    simple_tokens = simple_tokenizer.tokenize(sample_text)
    print(f"--- SimpleTokenizer Output (first 20 tokens): {simple_tokens[:20]}")
    print()

    # Test with RegexTokenizer
    regex_tokenizer = RegexTokenizer()
    regex_tokens = regex_tokenizer.tokenize(sample_text)
    print(f"--- RegexTokenizer Output (first 20 tokens): {regex_tokens[:20]}")
    print()

def test_count_vectorizer_with_ud_ewt():
    dataset_path = r"F:\NLP\data\en_ewt-ud-train.txt"
    raw_text = load_raw_text_data(dataset_path)
    
    if not raw_text:
        print("[ERROR] Dataset could not be loaded.")
        return
    
    sample_text = raw_text[:500]
    print("=== Testing CountVectorizer with UD_English-EWT Dataset ===")
    print(f"Original sample (first 100 chars): {sample_text[:100]}...\n")

    # Test with SimpleTokenizer
    simple_tokenizer = SimpleTokenizer()
    simple_vectorizer = CountVectorizer(simple_tokenizer)
    
    simple_vectors = simple_vectorizer.fit_transform([sample_text])
    print("--- SimpleTokenizer ---")
    print("Learned Vocabulary:", simple_vectorizer.vocabulary)
    print("Document-Term Vector (first 20 tokens):", simple_vectors[0][:20])
    print()

    # Test with RegexTokenizer
    regex_tokenizer = RegexTokenizer()
    regex_vectorizer = CountVectorizer(regex_tokenizer)
    
    regex_vectors = regex_vectorizer.fit_transform([sample_text])
    print("--- RegexTokenizer ---")
    print("Learned Vocabulary:", regex_vectorizer.vocabulary)
    print("Document-Term Vector (first 20 tokens):", regex_vectors[0][:20])


if __name__ == "__main__":
    test_tokenizers()
    test_tokenization_with_ud_ewt()
    test_count_vectorizer_with_ud_ewt()