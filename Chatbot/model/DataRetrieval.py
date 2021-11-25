from gensim.summarization.bm25 import BM25


class DataRetrieval:

    def __init__(self, nlp):
        self.tokenize = lambda text: [token.lemma_ for token in nlp(text)]
        self.bm25 = None
        self.passages = None

    def data_preprocess(self, doc):
        passages = [p for p in doc.split('\n') if p and not p.startswith('=')]
        print("number of passages: ", len(passages))
        return passages

    def fit(self, docs):
        passages = self.data_preprocess(docs)
        corpus = [self.tokenize(p) for p in passages]
        self.bm25 = BM25(corpus)
        self.passages = passages

    def most_similar(self, question, top_number=10):
        tokens = self.tokenize(question)
        scores = self.bm25.get_scores(tokens)
        pairs = [(s, i) for i, s in enumerate(scores)]
        pairs.sort(reverse=True)
        passages = [self.passages[i] for _, i in pairs[:top_number]]
        print(passages)
        return passages
