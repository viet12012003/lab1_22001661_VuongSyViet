import re
from typing import List
from src.core.interfaces import Tokenizer

class RegexTokenizer(Tokenizer):
    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize the input text using a single regex pattern.
        
        - \w+ matches sequences of word characters (letters, digits, underscore)
        - [^\w\s] matches any character that is not a word character or whitespace 
          (e.g., punctuation)
        """
        text = text.lower()
        tokens = re.findall(r"\w+|[^\w\s]", text)

        return tokens