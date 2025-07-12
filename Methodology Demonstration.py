# scripts/Methodology Demonstration.py

"""
Methodology Demonstration
-------------------------
This script demonstrates a hybrid approach for classifying potentially harmful or violent text content:
1. Rule-based keyword matching (default)
2. Contextual NLP-based matching using spaCy (--mode=nlp)

Author: [Qiuyu Lu]
"""

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

# Keywords associated with each violence level, which is also an example
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

# Here comes the hybrid approach that I used in my previous work experience

def classify_sentence(sentence):
    """
    Classifies a sentence based on rule-based keyword matching.
    """
    sentence = sentence.lower()
    for level, keywords in violence_keywords.items():
        for keyword in keywords:
            if keyword in sentence:
                return level
    return "Unknown"

def classify_sentence_nlp(sentence):
    """
    Classifies a sentence using spaCy NLP for context-aware detection.
    Requires spaCy and the English model installed.
    """
    try:
        import spacy
    except ImportError:
        print("spaCy is not installed. To use NLP mode, run:")
        print("pip install spacy && python -m spacy download en_core_web_sm")
        return "Unknown"
    nlp = spacy.load("en_core_web_sm")

    violent_verbs = {"stab", "kill", "murder", "attack", "assassinate", "shoot", "harm", "hurt"}
    weapons = {"knife", "gun", "bomb", "weapon", "rifle", "explosive", "pistol", "blade"}

    doc = nlp(sentence.lower())

    verbs = {token.lemma_ for token in doc if token.pos_ == "VERB"}
    nouns = {token.text for token in doc if token.pos_ == "NOUN"}

    if verbs & violent_verbs and nouns & weapons:
        return "Dangerous"
    elif verbs & violent_verbs:
        return "Explicit"
    elif nouns & weapons:
        return "Questionable"
    else:
        return "Safe"

if __name__ == "__main__":
    import sys

    # Always print demo with the example test sentences
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
    print("🔍 Violence Classification Results (Rule-based):\n")
    for sentence in test_sentences:
        level = classify_sentence(sentence)
        print(f"📝 \"{sentence}\" → Classified as: **{level}**")

    # Now check if the user provided a sentence to classify
    if len(sys.argv) > 1:
        # Support NLP mode via --mode=nlp
        if "--mode=nlp" in sys.argv:
            input_sentence = " ".join(arg for arg in sys.argv[1:] if not arg.startswith("--"))
            result = classify_sentence_nlp(input_sentence)
            print(f"\n📝 (NLP Mode) \"{input_sentence}\" → Classified as: **{result}**")
        else:
            input_sentence = " ".join(arg for arg in sys.argv[1:] if not arg.startswith("--"))
            result = classify_sentence(input_sentence)
            print(f"\n📝 (Rule Mode) \"{input_sentence}\" → Classified as: **{result}**")
    else:
        print("\n⚠️ No sentence provided. Example usage:")
        print("    python \"Methodology Demonstration.py\" \"He stabbed someone with a knife.\"")
        print("    python \"Methodology Demonstration.py\" \"He stabbed someone with a knife.\" --mode=nlp")
