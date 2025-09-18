from src.core.interfaces import Vectorizer
from typing import List

class CountVectorizer(Vectorizer):
    def __init__(self, tokenizer):
        """
        Initialize the CountVectorizer with a tokenizer instance.
        
        Args:
            tokenizer: Tokenizer instance from Lab 1
        """
        self.tokenizer = tokenizer
        self.vocabulary = {}

    def fit(self, corpus: List[str]):
        """
        Learn the vocabulary from a list of documents (corpus).
        
        Args:
            corpus (List[str]): List of documents to learn vocabulary from
        """
        unique_tokens = set()
        for document in corpus:
            tokens = self.tokenizer.tokenize(document)
            unique_tokens.update(tokens)
        
        # Create vocabulary dictionary by mapping each unique token to an index
        self.vocabulary = {token: idx for idx, token in enumerate(sorted(unique_tokens))}

    def transform(self, documents: List[str]) -> List[List[int]]:
        """
        Transform a list of documents into a list of count vectors
        based on the learned vocabulary.
        
        Args:
            documents (List[str]): List of documents to transform
            
        Returns:
            List[List[int]]: List of count vectors
        """
        vectors = []
        vocab_size = len(self.vocabulary)
        
        for document in documents:
            vector = [0] * vocab_size
            tokens = self.tokenizer.tokenize(document)
            
            for token in tokens:
                if token in self.vocabulary:
                    vector[self.vocabulary[token]] += 1
            
            vectors.append(vector)
        
        return vectors

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Convenience method that performs fit and then transform on the same data.
        
        Args:
            corpus (List[str]): List of documents to fit and transform
            
        Returns:
            List[List[int]]: List of count vectors
        """
        self.fit(corpus)
        return self.transform(corpus)