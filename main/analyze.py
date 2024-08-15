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
STOPWORDS = {
    'uk': {'та', 'і', 'у', 'на', 'з', 'до', 'не', 'що', 'як', 'але', 'це', 'за', 'для', 'в', 'зо', 'від', 'про'},
    'en': {'the', 'and', 'to', 'of', 'a', 'in', 'that', 'is', 'it', 'with', 'for', 'on', 'was', 'as', 'at', 'be'}
}

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

    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(output_dir / "wordcloud.png", bbox_inches='tight')
    plt.close()

    # Generate frequency chart
    top_words = word_freq.most_common(20)
    words, counts = zip(*top_words)
    
    plt.figure(figsize=(12, 8))
    plt.barh(words[::-1], counts[::-1])  # Reverse for descending order
    plt.title("Top 20 Most Frequent Words")
    plt.xlabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_dir / "frequency_chart.png")
    plt.close()

    # Save raw frequency data
    with open(output_dir / "word_frequencies.txt", 'w', encoding='utf-8') as f:
        for word, count in word_freq.most_common():
            f.write(f"{word}: {count}\n")

    print(f"Analysis saved to: {output_dir}")

if __name__ == "__main__":
    try:
        analyze_diary()
    except KeyboardInterrupt:
        print("\nAnalysis cancelled")
