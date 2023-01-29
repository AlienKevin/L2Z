import contractions
import spacy
import utils

class Filter:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_trf')
        self.core = utils.load_vocab("core")
        self.MAX_NUM_OUT_OF_VOCAB = 2

    def is_valid_example(self, example: str, target_word: str) -> bool:
        """Check if an example is valid
        Valid conditions:
        1. Number of out-of-vocab words <= MAX_NUM_OUT_OF_VOCAB
        2. Contains the target_word exactly once

        >>> f.is_valid_example("This is the peril of a valid example", "peril")
        True
        
        Invalid because target word not present
        >>> f.is_valid_example("This is a valid example.", "peril")
        False

        Valid because has a few out-of-vocab words
        >>> f.is_valid_example("This is the peril of valid example. We got an unseen word B12.", "peril")
        True
        
        Invalid because too many out-of-vocab words
        >>> f.is_valid_example("This is the peril of valid example. We got unseen words like B12 and JavaScript.", "peril")
        False
        """
        example = contractions.fix(example)
        # Source: https://www.geeksforgeeks.org/python-lemmatization-approaches-with-examples/
        doc = self.nlp(example)
        num_out_of_vocab = 0
        has_seen_target_word = False
        for token in doc:
            # Skip uninteresting tokens
            if token.is_punct or token.is_currency or token.is_digit or token.is_punct or token.is_space or token.is_stop or token.like_num or token.pos_ == "PROPN":
                continue
            if token.lemma_ == target_word:
                if has_seen_target_word:
                    return False
                else:
                    has_seen_target_word = True
            elif not token.lemma_ in self.core:
                num_out_of_vocab += 1
                if num_out_of_vocab > self.MAX_NUM_OUT_OF_VOCAB:
                    return False
        return has_seen_target_word

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'f': Filter()})
