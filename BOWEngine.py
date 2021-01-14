import re
from SearchEngineBase import SearchEngineBase
from SearchEngineBase import main


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        # Use regular expressions to remove punctuation and line breaks
        text = re.sub(r'[^\w]', ' ', text)
        text = text.lower()
        # Generate a list of all words
        word_list = text.split(' ')
        # Removing blank words
        word_list = filter(None, word_list)
        # Return a set of words
        return set(word_list)


search_engine = BOWEngine()
main(search_engine)