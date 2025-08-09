COMPANY: CODTECH IT SOLUTIONS

NAME: Sambhav Shrivastava

INTERN ID: CT04DZ728

DOMAIN: AI

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

Description: This project presents a simple yet effective text summarization tool built from scratch using Python and Natural Language Processing (NLP) techniques. The primary objective of this tool is to generate concise summaries from longer pieces of text, making it easier for users to quickly grasp the essential information without reading the entire content. The tool is designed to be user-friendly, requiring no prior knowledge of NLP or programming, and can be run directly from the command line.

How the Tool Works

The summarization tool employs an extractive summarization approach. Extractive summarization involves selecting the most important sentences from the original text and concatenating them to form a summary. This method is straightforward and often produces grammatically correct summaries since it uses actual sentences from the input.

The process begins by prompting the user to enter or paste the text they wish to summarize. The user can input multiple lines, and the input is terminated by entering an empty line. Once the input is complete, the tool displays the full input text for reference, ensuring transparency and clarity in the summarization process.

The core of the summarization logic is based on word frequency analysis. The tool first splits the input text into individual sentences using sentence tokenization. It then preprocesses the text by converting all words to lowercase, removing punctuation, and filtering out common English stopwords (such as “the,” “is,” “and,” etc.) using the NLTK library. This preprocessing step ensures that only meaningful words contribute to the summary.

Next, the tool calculates the frequency of each remaining word in the text. Words that appear more frequently are considered more important. Each sentence is then scored based on the sum of the frequencies of its constituent words. Sentences containing more high-frequency words receive higher scores, indicating their importance in the context of the entire text.

After scoring all sentences, the tool selects the top N sentences with the highest scores (by default, three sentences) to form the summary. These sentences are presented in the order they appeared in the original text to maintain coherence and readability.

Features and Benefits

User-Friendly Interface: The tool runs in the terminal and guides the user through the input process, making it accessible to users with minimal technical background.
Transparency: Both the original input text and the generated summary are displayed, allowing users to compare and verify the summarization.
Efficiency: By focusing on the most important sentences, the tool helps users save time and quickly understand the main points of lengthy documents.
Customizable: The number of sentences in the summary can be easily adjusted in the code to suit different needs.
Conclusion

This text summarization tool demonstrates the practical application of basic NLP techniques for real-world tasks. It showcases how simple algorithms, such as word frequency analysis and sentence scoring, can be combined to create useful tools for information extraction and content reduction. The project serves as a solid foundation for further exploration into more advanced NLP methods, such as abstractive summarization or machine learning-based approaches.
