# SAMO

> “People aren't rational. We're not thinking machines, we're - we're feeling machines 
> that happen to think.”
> > -Peter Watts


_A personal journey in organizing thoughts and uncovering writing patterns through code_

![Sample Word Cloud](https://github.com/user-attachments/assets/8e1b0583-238c-45bc-84c1-bc350c09af16)


## About this project 🔍

I created this personalized diary system to:
- 📅 Automatically organize daily entries in chronological structure with easy finding system
- 🇺🇦🇬🇧 Handle multilingual content
- Generate visual insights from my writing patterns
- Experiment with text analysis techniques

What started as a simple note organizer evolved into an exploration of natural language processing and much more is awaiting.

## Key Features

### Diary Core
- **Automatic folder structure**  
  `~/diary/YYYY-MM/YYYY-MM-DD.md`
- **Markdown timestamps**  
  ```markdown
  ## 14:30
  Сьогодні вивчала нові концепції машинного навчання
  ```
  It helps to save multiple entries from one day in single markdown note.

### Text analysis
- **Bilingual word clouds**  
  Visual representations of the language landscape
- **Frequency analysis**  
  Discover which concepts dominate your thoughts
- **Stop-words**  
  Separate stopword lists for Ukrainian and English (so it doesn't count trashy words).

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

# GUI
from tkinter import ttk, scrolledtext, messagebox
```


## Future I'd like to develope

- [ ] **PDF Export**  
  Create beautiful monthly recap documents, conversion to pdf and more file handling
- [ ] **Topic modeling and more language analysis**  
  Auto-discover recurring themes with LDA; more exciting word analysis
- [ ] **Writing habit tracker**  
  Analyze the most productive times/days/seasons
- [ ] ~**GUI interface**~ **Updated and more cool GUI**  
  I implemented the most basic GUI but much more could be done
- [ ] **Wrap up an application**

## Why I Built This

1. **Organization** - Clean structure brings peace of mind
2. **Project to develope some programming skills** - I simply wanted to practice some python
3. **Data** - Numbers that tell stories about yourSELF





---

_👩💻 Want to use SAMO? Clone the repo and try:_  
`python run.py` - Explore the GIU
`python run.py --cli` - Explore the initial terminal version
