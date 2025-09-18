from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer

def test_count_vectorizer():
    tokenizer = RegexTokenizer()
    vectorizer = CountVectorizer(tokenizer)
    
    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]
    
    vectors = vectorizer.fit_transform(corpus)
    
    print("Learned Vocabulary:", vectorizer.vocabulary)
    print("Document-Term Matrix (Count Vectors):")
    for i, vector in enumerate(vectors):
        print(f"Document {i + 1}: {vector}")

if __name__ == "__main__":
    test_count_vectorizer()