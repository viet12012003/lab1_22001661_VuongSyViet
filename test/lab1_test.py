from src.preprocessing.simple_tokenizer import SimpleTokenizer

if __name__ == "__main__":
    tokenizer = SimpleTokenizer()
    text = "Hello, world!"
    tokens = tokenizer.tokenize(text)
    print(tokens)