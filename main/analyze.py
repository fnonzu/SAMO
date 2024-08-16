import os
import re
from collections import Counter
from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime

# Configuration
DIARY_ROOT = Path.home() / "diary"
ANALYSIS_DIR = Path.home() / "diary_analysis"

def load_diary_entries():
    """Load all diary entries from markdown files"""
    entries = []
    for root, _, files in os.walk(DIARY_ROOT):
        for file in files:
            if file.endswith(".md"):
                path = Path(root) / file
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Remove markdown headers and timestamps
                        content = re.sub(r'^#+.+\n?', '', content, flags=re.MULTILINE)
                        entries.append(content)
                except Exception as e:
                    print(f"Error reading {path}: {str(e)}")
    return "\n".join(entries)

def clean_text(text, lang='uk'):
    """Clean and tokenize text with language-specific processing"""
    # Remove markdown formatting
    text = re.sub(r'[\*\_\[\]\(\)#-]', ' ', text)
    # Remove punctuation (preserving apostrophes for contractions)
    text = re.sub(r'[^\w\s\']', ' ', text, flags=re.UNICODE)
    # Convert to lowercase
    text = text.lower()
    # Tokenize words
    words = re.findall(r"[\w']+", text, flags=re.UNICODE)
    # Remove stopwords and short words
    return [word for word in words if word not in STOPWORDS[lang] and len(word) > 2]

def analyze_diary():
    # Create analysis directory
    analysis_date = datetime.now().strftime("%Y-%m-%d")
    output_dir = ANALYSIS_DIR / analysis_date
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load and process text
    text = load_diary_entries()
    words = clean_text(text)
    word_freq = Counter(words)

    # Generate word cloud
    wordcloud = WordCloud(
        width=1600,
        height=800,
        background_color='white',
        collocations=False
    ).generate_from_frequencies(word_freq)



if __name__ == "__main__":
    try:
        analyze_diary()
    except KeyboardInterrupt:
        print("\nAnalysis cancelled")
