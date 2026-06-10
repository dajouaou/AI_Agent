import csv
import os
from datetime import datetime

FEEDBACK_FILE = "logs/feedback.csv"


def save_feedback(question, feedback, confidence, status):
    file_exists = os.path.exists(FEEDBACK_FILE)

    with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "question",
                "feedback",
                "confidence",
                "status"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            question,
            feedback,
            confidence,
            status
        ])


def count_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return 0

    with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
        return max(0, sum(1 for _ in file) - 1)