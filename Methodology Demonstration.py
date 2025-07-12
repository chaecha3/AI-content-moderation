# scripts/violence_classifier.py

# Example sentences representing each violence severity level
violence_examples = {
    "Safe": "This Japanese chef uses a traditional knife to prepare sushi with precision and care.",
    "Low": "Recent studies highlight a rise in knife-related injuries in urban areas.",
    "Notable": "In the survival game, players can collect knives and use them to hunt animals or defend themselves.",
    "Questionable": "Honestly, I think using a knife for self-defense is overrated — pepper spray is more practical.",
    "Uncertain": "If I were ever attacked, I suppose I'd grab the nearest knife and hope for the best.",
    "Mature": "To assassinate silently, approach the guard from behind and plunge the knife deep before he can react.",
    "Explicit": "The victim was stabbed repeatedly in the chest with a hunting knife until he stopped moving.",
    "Dangerous": "We're arming ourselves with knives and heading to the rally — they won't see it coming."
}

# Keywords associated with each violence level
violence_keywords = {
    "Dangerous": ["attack", "bomb", "shoot", "kill", "knife", "gun", "plotting"],
    "Explicit": ["stabbed", "blood", "knife", "victim", "eviscerate"],
    "Mature": ["assassinate", "plunge", "ambush", "kill", "knife"],
    "Uncertain": ["if i had to", "grab the knife", "hope for the best"],
    "Questionable": ["self-defense", "pepper spray", "aren't good weapons"],
    "Notable": ["hunt", "game", "collect knives", "kill animals"],
    "Low": ["knife crime", "injuries", "incident"],
    "Safe": ["knife skills", "cooking", "sushi"]
}

# Classify a sentence based on the first matching keyword
def classify_sentence(sentence):
    sentence = sentence.lower()
    for level, keywords in violence_keywords.items():
        for keyword in keywords:
            if keyword in sentence:
                return level
    return "Unknown"

# Example sentences to test classification (you can modify or expand this list)
test_sentences = [
    "Knife skills are important in Japanese cooking.",
    "We are planning a knife and bomb attack at the event.",
    "Try to stab him with a hunting knife in GTA.",
    "Knives aren’t good weapons — guns are better.",
    "I just bought a new kitchen knife.",
    "If I had to, I’d stab someone in self-defense.",
    "We're plotting an attack with bombs and knives.",
    "She was stabbed twelve times in the chest."
]

# Print classification results for each test sentence
print("🔍 Violence Classification Results:\n")
for sentence in test_sentences:
    level = classify_sentence(sentence)
    print(f"📝 \"{sentence}\" → Classified as: **{level}**")

import sys

if len(sys.argv) > 1:
    input_sentence = " ".join(sys.argv[1:])
    result = classify_sentence(input_sentence)
    print(f"\n📝 \"{input_sentence}\" → Classified as: **{result}**")
else:
    print("⚠️ No sentence provided. Example usage:")
    print("    python \"Methodology Demonstration.py\" \"He stabbed someone with a knife.\"")

