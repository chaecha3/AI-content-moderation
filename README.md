# 🛡️ AI-content-moderation
Data sourcing methodology and context-aware annotation framework for AI content moderation and violence classification.

## 📌 Project Overview

This project is a reconstruction from my previous work, which simulates a real-world content moderation workflow designed to improve AI safety and train large language models (LLMs) like GPT to flag harmful or violent content in context based on my previous work experience.

Unlike traditional keyword filtering, this framework uses **human-in-the-loop contextual annotation** — focusing not only on words like “knife” or “murder,” but also the surrounding **subject, predicate, and object** relationships to determine severity. In one line, this methodology is context-based and more detail-oriented.

---

## 🎯 Objectives

- Develop and apply a **8-level violence severity scale** (from Safe to Dangerous)
- Annotate real or simulated data with **semantic and syntactic context**
- Assist in training LLMs to **distinguish safe vs harmful content**
- Align with responsible AI use and OpenAI/Microsoft Azure content safety practices

---

## 🧩 Project Structure

| File | Description |
|------|-------------|
| `README.md` | General description of what I do |
| `Methodology Demonstration.py` | Basic python script demonstration to show my approach to detect or flag harmful content based off keywords with the help of NLP |
| `Project Explanation.pdf` | Explains my python example in details |

---

## 🧠 Sample: Severity Levels (Violence Classification)

| Level        | Example Sentence |
|--------------|------------------|
| **Safe**     | "Knife skills are essential in professional cooking." |
| **Low**      | "Knife crime rates have risen in urban areas." |
| **Notable**  | "In GTA, you can stab enemies for extra points." |
| **Questionable** | "Knives aren't great weapons; guns are better." |
| **Mature**   | "You must ambush someone to kill them with a knife." |
| **Explicit** | "Stab your victim with a knife and remove their organs." |
| **Dangerous**| "We’re planning a knife and gun attack at the embassy." |

> Inspired from `examples/violence_guidelines_table.png`

---

## 🛠️ Tools Used

- Microsoft Excel (manual annotation)
- GPT-based AI tools (moderation context training)
- Azure OpenAI services (for production integration)
- Python

---

## 🔐 License

Sharing this work is generally not allowed as this work is only for career-pursuing purposes.

---

## 🛡️ Disclaimer

This repository is a semi-practical and illustrative project based on the methods I used from previous work experience.  
Almost no confidential information or data will be shown here. My experience from my previous work will be reconstructed or simulated.  
This reflects my personal understanding and work process only.
And Did i use AI for this? 100% yes, but just for refining and helping me with python grammar.

## 🙋 About Me

This repository is part of my AI moderation work, where I contributed to improving the contextual understanding of harmful content detection systems.  
Feel free to reach out or collaborate!
