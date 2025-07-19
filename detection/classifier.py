from transformers import pipeline
import torch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project_config import THREAT_LABELS, THREAT_THRESHOLD

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=0 if torch.cuda.is_available() else -1, framework="pt")

def detect_threat(text):
    result = classifier(text, THREAT_LABELS)
    threats = []
    for label, score in zip(result["labels"], result["scores"]):
        if score >= THREAT_THRESHOLD:
            threats.append((label, score))
    return threats

# if __name__ == "__main__":
#     sample_text = "I will hurt you if you come any closer."
#     threats = detect_threat(sample_text)

#     if threats:
#         print("🚨 Threats Detected:")
#         for label, score in threats:
#             print(f"- {label} ({round(score, 2)})")
#     else:
#         print("✅ No threats detected.")
