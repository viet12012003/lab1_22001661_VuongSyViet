import string
from typing import List
from src.core.interfaces import Tokenizer

class SimpleTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize the input text by:
        - Converting to lowercase
        - Splitting by whitespace
        - Separating punctuation characters as individual tokens
        """
        text = text.lower()
        tokens = []

        for word in text.split():
            current = []
            for ch in word:
                if ch in string.punctuation:
                    if current:
                        tokens.append("".join(current))
                        current = []
                    tokens.append(ch)
                else:
                    current.append(ch)
            if current:
                tokens.append("".join(current))

        return tokens