import nltk
import string
from collections import defaultdict

# Download required NLTK data files (only first time)
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize_text(text, num_sentences=3):
    """
    Summarize the input text by extracting the most important sentences.
    Args:
        text (str): The input text to summarize.
        num_sentences (int): Number of sentences to include in the summary.
    Returns:
        str: The summary text.
    """
    # 1. Split text into sentences
    sentences = sent_tokenize(text)
    
    # 2. Preprocess: Lowercase, remove punctuation, tokenize
    stop_words = set(stopwords.words('english'))
    word_frequencies = defaultdict(int)
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        for word in words:
            if word not in stop_words and word not in string.punctuation:
                word_frequencies[word] += 1
    
    # 3. Score sentences by word frequency
    sentence_scores = defaultdict(int)
    for i, sentence in enumerate(sentences):
        words = word_tokenize(sentence.lower())
        for word in words:
            if word in word_frequencies:
                sentence_scores[i] += word_frequencies[word]
    
    # 4. Select top N sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join([sentences[i] for i in sorted(top_sentences)])
    return summary

if __name__ == "__main__":
    print("==============================")
    print(" TEXT SUMMARIZATION TOOL ")
    print("==============================\n")
    print("Enter the text to summarize (end input with an empty line):")
    lines = []
    while True:
        line = input()
        if line.strip() == '':
            break
        lines.append(line)
    text = '\n'.join(lines)
    print("\n--- Input Text ---")
    print(text)
    summary = summarize_text(text)
    print("\n--- Concise Summary ---")
    print(summary)
    print("\n==============================")
