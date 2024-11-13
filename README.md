

# Plagiarism Detection System

This project implements a plagiarism detection system in Python using the A* search algorithm and Levenshtein distance. The program detects potential plagiarism between two documents by comparing their sentences and identifying similar or slightly modified texts.

## Features

- **Text Preprocessing**: The program tokenizes the text into sentences, converts them to lowercase, and removes punctuation.
- **Levenshtein Distance Calculation**: A custom function calculates the Levenshtein distance between sentences, used to measure similarity.
- **Heuristic Function**: Calculates the heuristic cost between remaining sentences for efficient A* search.
- **A* Search for Sentence Alignment**: Finds the best alignment between sentences from two documents, highlighting potentially plagiarized text.
- **Threshold-Based Detection**: Allows adjustment of the Levenshtein distance threshold to fine-tune plagiarism sensitivity.

## Requirements

- Python 3.x
- [NLTK](https://www.nltk.org/) library for sentence tokenization

To install NLTK:
```bash
pip install nltk
```

## Usage

### 1. Clone the repository:

```bash
git clone https://github.com/username/plagiarism-detection.git
cd plagiarism-detection
```

### 2. Run the Code

To use the plagiarism detection system, run the following command:

```bash
python plagiarism_detection.py
```

### 3. Test Cases

The program includes several test cases to demonstrate its effectiveness:

1. **Identical Documents**: Detects if two documents are completely identical.
2. **Slightly Modified Document**: Identifies potential plagiarism with small changes.
3. **Completely Different Documents**: Confirms no plagiarism for entirely different texts.
4. **Partial Overlap**: Detects plagiarism in documents with overlapping sentences.

## Example

```python
# Test Case 1: Identical Documents
doc1 = "This is a test document. It has several sentences. It is used to detect plagiarism."
doc2 = "This is a test document. It has several sentences. It is used to detect plagiarism."
detect_plagiarism(doc1, doc2)
```

Output:
```plaintext
Potential Plagiarism Detected:
Doc1: this is a test document
Doc2: this is a test document

No potential plagiarism detected.
```

## Functions

### `preprocess_text(text)`
Tokenizes, lowers, and removes punctuation from the text.

### `levenshtein_distance(s1, s2)`
Calculates the Levenshtein distance between two sentences.

### `heuristic(remaining_doc1, remaining_doc2)`
Estimates the similarity cost between the remaining sentences.

### `a_star_search(doc1_sentences, doc2_sentences)`
Uses A* search to align sentences and find potential plagiarism.

### `detect_plagiarism(doc1, doc2)`
Runs the entire plagiarism detection process and outputs results.

## Customization

You can adjust the plagiarism threshold in the `detect_plagiarism` function by changing the `levenshtein_distance` threshold value.
