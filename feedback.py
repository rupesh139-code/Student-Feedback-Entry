# feedback_entry.py

class FeedbackEntry:
    def __init__(self):
        self.feedback_list = []

    def add_feedback(self, student_name, score, comments):
        feedback = {
            'student_name': student_name,
            'score': score,
            'comments': comments
        }
        self.feedback_list.append(feedback)

    def get_feedback(self):
        return self.feedback_list
