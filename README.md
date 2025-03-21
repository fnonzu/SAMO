# SAMO

> “People aren't rational. We're not thinking machines, we're - we're feeling machines 
> that happen to think.”
> > -Peter Watts


_A personal journey in organizing thoughts and uncovering writing patterns through code_

![Sample Word Cloud](https://github.com/user-attachments/assets/8e1b0583-238c-45bc-84c1-bc350c09af16)![wordcloud]


## About this project 🔍

I created this personalized diary system to:
- 📅 Automatically organize daily entries in chronological structure with easy finding system
- 🇺🇦🇬🇧 Handle multilingual content
- 🔮 Generate visual insights from my writing patterns
- 🧠 Experiment with text analysis techniques

What started as a simple note organizer evolved into an exploration of natural language processing.

## Key Features

### Diary Core
- **Automatic Folder Structure**  
  `~/diary/YYYY-MM/YYYY-MM-DD.md` 
- **Markdown Timestamps**  
  ```markdown
  ## 14:30
  Сьогодні вивчала нові концепції машинного навчання
  ```
- **Unicode Support**  
  Flawless Ukrainian text handling

### Text Insights
- **Bilingual Word Clouds**  
  Visual representations of the language landscape
- **Frequency Analysis**  
  Discover which concepts dominate the thoughts
- **Stop-words**  
  Separate stopword lists for Ukrainian and English (so it doesn't count trashy words)

## Tech Stack 💻

```python
# Core components
from pathlib import Path  # File system 
from datetime import datetime  # Timem
import re  # Text cleaning ninja

# Analysis components
from collections import Counter  # counting guru
import matplotlib.pyplot as plt  # visualization
from wordcloud import WordCloud  #  word counting secret
```


## Future I'd like to see

I want to take this next:

- [ ] **PDF Export**  
  Create beautiful monthly recap documents
- [ ] **Topic Modeling**  
  Auto-discover recurring themes with LDA
- [ ] **Writing Habit Tracker**  
  Analyze my most productive times/days
- [ ] **GUI Interface**  
  Because terminal is cool, but buttons are fun too!

## Why I Built This ❤

This project combines my three great loves:
1. **Organization** - Clean structure brings peace of mind
2. **Project to develope some programming skills**
3. **Data** - Numbers that tell stories about myself



---

_👩💻 Want to participate? Clone the repo and try:_  
`python diary.py` - Pour your thoughts into the digital pages  
`python analysis.py` - See what patterns emerge_
