# Nipur Patel

import nltk
import string
import heapq

# Text Preprocessing Function
def preprocess_text(text):
    sentences = nltk.sent_tokenize(text)
    sentences = [s.lower().translate(str.maketrans('', '', string.punctuation)) for s in sentences]
    return sentences

# Levenshtein Distance Function
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    previous_row = range(len(s2) + 1)
    
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# Heuristic Function
def heuristic(remaining_doc1, remaining_doc2):
    if not remaining_doc2:
        return float('inf')
    return sum(min(levenshtein_distance(s1, s2) for s2 in remaining_doc2) for s1 in remaining_doc1)

# A* Search Function
def a_star_search(doc1_sentences, doc2_sentences):
    def levenshtein_distance(s1, s2):
        if len(s1) < len(s2):
            return levenshtein_distance(s2, s1)
        
        previous_row = range(len(s2) + 1)
        
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def heuristic(remaining_doc1, remaining_doc2):
        if not remaining_doc2:
            return float('inf')
        return sum(min(levenshtein_distance(s1, s2) for s2 in remaining_doc2) for s1 in remaining_doc1)

    open_list = []
    heapq.heappush(open_list, (0, 0, 0, []))
    closed_list = set()

    while open_list:
        current_cost, skip_cost, pos, alignment = heapq.heappop(open_list)

        if pos >= len(doc2_sentences):
            return alignment

        if pos + 1 < len(doc2_sentences):
            heapq.heappush(open_list, (skip_cost + heuristic(doc1_sentences, doc2_sentences[pos+1:]), skip_cost, pos + 1, alignment + [("", doc2_sentences[pos])]))

        for i, sentence in enumerate(doc1_sentences):
            cost = levenshtein_distance(sentence, doc2_sentences[pos])
            heapq.heappush(open_list, (current_cost + cost, skip_cost, pos + 1, alignment + [(sentence, doc2_sentences[pos])]))

        if not doc1_sentences:
            return alignment

    return []

# Plagiarism Detection System
def detect_plagiarism(doc1, doc2):
    doc1_sentences = preprocess_text(doc1)
    doc2_sentences = preprocess_text(doc2)

    alignment = a_star_search(doc1_sentences, doc2_sentences)

    if alignment is None:
        alignment = []

    # Adjust threshold for detecting plagiarism
    detected = False
    for sentence_pair in alignment:
        if levenshtein_distance(sentence_pair[0], sentence_pair[1]) < 10:  # Increased threshold
            print(f"Potential Plagiarism Detected:\nDoc1: {sentence_pair[0]}\nDoc2: {sentence_pair[1]}\n")
            detected = True


    if not detected:
        print("No potential plagiarism detected.")




# Test Cases

# Test Case 1: Identical Documents
doc1 = "This is a test document. It has several sentences. It is used to detect plagiarism."
doc2 = "This is a test document. It has several sentences. It is used to detect plagiarism."
print("Test Case 1: Identical Documents")
detect_plagiarism(doc1, doc2)

# Test Case 2: Slightly Modified Document
doc3 = "This is a test file. It contains many sentences. It helps to check plagiarism."
print("\nTest Case 2: Slightly Modified Document")
detect_plagiarism(doc1, doc3)

# Test Case 3: Completely Different Documents
doc4 = "The quick brown fox jumps over the lazy dog. Programming is fun."
print("\nTest Case 3: Completely Different Documents")
detect_plagiarism(doc1, doc4)

# Test Case 4: Partial Overlap
doc5 = "This is a test document. Some content overlaps. It helps to detect similar texts."
print("\nTest Case 4: Partial Overlap")
detect_plagiarism(doc1, doc5)
