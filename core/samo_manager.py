from pathlib import Path
from datetime import datetime
import os

class SamoManager:
    @staticmethod
    def get_diary_root():
        return Path.home() / "diary"
    
    @staticmethod
    def save_entry(content):
        now = datetime.now()
        diary_root = SamoManager.get_diary_root()
        year_month = now.strftime("%Y-%m")
        day_file = now.strftime("%Y-%m-%d") + ".md"
        
        month_dir = diary_root / year_month
        month_dir.mkdir(parents=True, exist_ok=True)
        file_path = month_dir / day_file
        
        timestamp = now.strftime("%H:%M")
        md_content = f"\n\n## {timestamp}\n{content}"
        
        with open(file_path, 'a', encoding='utf-8') as f:
            if os.stat(file_path).st_size == 0:
                f.write(f"# {now.strftime('%Y-%m-%d')}\n")
            f.write(md_content)
        
        return str(file_path)
