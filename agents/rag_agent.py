class RAGAgent:
    def __init__(self):
        self.knowledge_base = [
            "Stress can be reduced using breathing exercises.",
            "Talking to friends helps emotional health.",
            "Exercise improves mental well-being.",
            "Sleep is important for mental stability.",
            "Meditation reduces anxiety and sadness."
        ]

    def retrieve(self, query):
        query_words = query.lower().split()

        scored_docs = []

        for doc in self.knowledge_base:
            score = sum(1 for w in query_words if w in doc.lower())
            if score > 0:
                scored_docs.append((doc, score))

        scored_docs.sort(key=lambda x: x[1], reverse=True)

        if not scored_docs:
            return ["No relevant context found."]

        return [doc for doc, _ in scored_docs[:3]]