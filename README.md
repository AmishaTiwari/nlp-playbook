# NLP Playbook

This repository is a structured playbook for building, understanding, and applying practical Natural Language Processing (NLP) systems.

It focuses on taking raw text data and systematically converting it into reliable, production-ready machine learning pipelines.

---

## It contains:

### 1. NLP pipeline stages:
- Text preprocessing (cleaning, normalization)
- Vectorization (Bag of Words, TF-IDF, n-grams)
- Classical models (Naive Bayes, Logistic Regression)
- Embeddings (Word2Vec, sentence embeddings)
- Transformers (HuggingFace, fine-tuning basics)

---

### 2. Practical NLP workflows:
- End-to-end text classification pipelines
- Feature representation comparison (TF-IDF vs embeddings)
- Model evaluation and error analysis
- Baseline → improvement → advanced model progression

---

## Repository structure:

Each section represents a stage in an NLP pipeline and contains:

- A Jupyter notebook with clean, minimal, step-by-step implementation
- A `notes.md` file with concise, interview-focused explanations:
  - What the step does
  - Why it is needed
  - When to use / avoid
  - Key parameters and trade-offs
  - Common mistakes and failure cases

---

## Additional components:

- `data/`
  - Raw and processed datasets used across experiments
  - Shared to ensure consistency across different approaches

- `src/`
  - Reusable utility functions for preprocessing, feature extraction, and modeling
  - Gradually built to reflect production-style code organization

- `experiments/`
  - Observations, results, and comparisons across different techniques

---

## Goals of this repository:

- Build strong intuition for text representation and NLP pipelines
- Practice industry-grade NLP workflows (not just model usage)
- Understand trade-offs between classical methods and modern approaches
- Develop reproducible and well-structured experiments
- Serve as a reference for real-world NLP problem solving