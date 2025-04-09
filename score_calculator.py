# score_calculator.py

class ScoreCalculator:
    @staticmethod
    def calculate_average_score(feedback_list):
        if not feedback_list:
            return 0
        total_score = sum(feedback['score'] for feedback in feedback_list)
        return total_score / len(feedback_list)
