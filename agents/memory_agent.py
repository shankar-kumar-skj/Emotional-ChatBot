class MemoryAgent:
    def __init__(self):
        self.memory = []

    def add_memory(self, user_input, response):
        self.memory.append({
            "user": user_input,
            "bot": response
        })

    def get_memory(self):
        if not self.memory:
            return {
                "message": "No previous conversation.",
                "history": []
            }

        return {
            "message": "Memory available",
            "history": self.memory[-5:]
        }