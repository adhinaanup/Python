import re
import nltk
from nltk.tokenize import sent_tokenize

# Download the required NLTK data
nltk.download('punkt')

def structured_to_normal_text_nltk(structured_text):
    # Step 1: Preprocess the structured text
    # Remove bullet points, numbers, and special characters
    preprocessed_text = re.sub(r"[\-\*\•\d]+\s", "", structured_text)  # Remove bullets or numbering
    preprocessed_text = re.sub(r"\s+", " ", preprocessed_text).strip()  # Remove extra spaces

    # Step 2: Tokenize the text into sentences
    sentences = sent_tokenize(preprocessed_text)

    # Step 3: Join the sentences into a paragraph
    normal_text = " ".join(sentences)

    return normal_text

# Example Structured Text
structured_text = """
- Python is a high-level programming language.
- It supports multiple programming paradigms.
- Created by Guido van Rossum and first released in 1991.
- Widely used for web development, data analysis, and AI/ML applications.
"""

# Convert to normal text
normal_text = structured_to_normal_text_nltk(structured_text)
print("Normal Text:\n", normal_text)
