from pathlib import Path
from datetime import datetime
import os

def get_note_content():
    """Get multi-line note input from user"""
    print("\nEnter your note (Press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            # Check if previous line was also empty
            if len(lines) > 0 and lines[-1] == "":
                lines.pop()
                break
        lines.append(line)
    return "\n".join(lines).strip()

def save_note():
    # Get current date and time
    now = datetime.now()
    
    # Create directory structure
    diary_root = Path.home() / "diary"
    year_month = now.strftime("%Y-%m")  # Format: "2024-01"
    day_file = now.strftime("%Y-%m-%d") + ".md"  # Format: "2024-01-01.md"
    
    month_dir = diary_root / year_month
    month_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = month_dir / day_file
    
    # Get note content
    note_content = get_note_content()
    if not note_content:
        print("No content provided. Note not saved.")
        return
    
    # Prepare Markdown content
    timestamp = now.strftime("%H:%M")
    md_content = f"\n\n## {timestamp}\n{note_content}"
    
    # Write to file
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            # Add date header if file is new
            if os.stat(file_path).st_size == 0:
                f.write(f"# {now.strftime('%Y-%m-%d')}\n")
            f.write(md_content)
        print(f"Note saved successfully at: {file_path}")
    except Exception as e:
        print(f"Error saving note: {str(e)}")

if __name__ == "__main__":
    save_note()
