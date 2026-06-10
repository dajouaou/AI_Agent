class StateManager:
    def __init__(self):
        self.history = []

    def create_state(self, question):
        return {
            "question": question,
            "retrieved_context": "",
            "answer": "",
            "confidence": 0,
            "status": "started",
            "feedback": None
        }

    def save_interaction(
        self,
        question,
        answer,
        confidence=0,
        status="answered",
        feedback=None
    ):
        self.history.append({
            "question": question,
            "answer": answer,
            "confidence": confidence,
            "status": status,
            "feedback": feedback
        })

    def get_history(self):
        return self.history

    def get_last_question(self):
        if self.history:
            return self.history[-1]["question"]
        return None

    def get_last_answer(self):
        if self.history:
            return self.history[-1]["answer"]
        return None

    def get_last_confidence(self):
        if self.history:
            return self.history[-1]["confidence"]
        return None

    def get_last_status(self):
        if self.history:
            return self.history[-1]["status"]
        return None

    def clear_history(self):
        self.history = []

    def interaction_count(self):
        return len(self.history)