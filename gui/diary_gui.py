import tkinter as tk
import sys
from tkinter import ttk, scrolledtext, messagebox
from core.samo_manager import SamoManager
from core.analysis import analyze_diary 
import threading
import os

class DiaryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Diary")
        self.geometry("800x900")
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header_frame = ttk.Frame(self)
        header_frame.pack(pady=20)
        
        ttk.Label(header_frame, text="Digital Diary", 
                style="TLabel", font=('Arial', 18)).pack()
        
        # Text editor
        self.text_area = scrolledtext.ScrolledText(self,
                                                 wrap=tk.WORD,
                                                 font=('Arial', 14),
                                                 padx=20,
                                                 pady=20)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Button panel
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)
        
        # Save button
        self.save_btn = ttk.Button(button_frame,
                                 text="Save Entry",
                                 command=self.save_entry)
        self.save_btn.pack(side=tk.LEFT, padx=10)
        
        # Analyze button
        self.analyze_btn = ttk.Button(button_frame,
                                    text="Analyze Diary",
                                    command=self.start_analysis)
        self.analyze_btn.pack(side=tk.LEFT, padx=10)
        
        # Status bar
        self.status_bar = ttk.Label(self,
                                  text="Ready",
                                  relief=tk.SUNKEN,
                                  anchor=tk.W)
        self.status_bar.pack(fill=tk.X)
        
    def start_analysis(self):
        """Start analysis in a separate thread to prevent GUI freeze"""
        self.update_status("Starting analysis...")
        threading.Thread(target=self.run_analysis, daemon=True).start()
        
    def run_analysis(self):
        """Perform the actual analysis"""
        try:
            results = analyze_diary()  # Assuming this returns file paths
            
            # Update GUI in main thread
            self.after(0, lambda: self.show_analysis_results(results))
            
        except Exception as e:
            self.after(0, lambda: self.update_status(f"Analysis failed: {str(e)}"))
            
    def show_analysis_results(self, results):
        """Display analysis results to user"""
        self.update_status("Analysis complete!")
        messagebox.showinfo(
            "Analysis Results",
            f"Created analysis files:\n\n"
            f"📊 Word Cloud: {results['wordcloud']}\n"
            f"📈 Frequency Chart: {results['frequency_chart']}\n"
            f"📝 Word Frequencies: {results['frequencies_file']}"
        )
        
        # Open file explorer to show results
        output_dir = os.path.dirname(results['wordcloud'])
        if os.name == 'nt':  # Windows
            os.startfile(output_dir)
        else:  # Mac/Linux
            os.system(f'open "{output_dir}"' if sys.platform == "darwin" else f'xdg-open "{output_dir}"')

    def update_status(self, message):
        self.status_bar.config(text=message)
        
    def save_entry(self):
        content = self.text_area.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Empty Entry", "Please write something!")
            return
        
        try:
            file_path = SamoManager.save_entry(content)
            self.text_area.delete("1.0", tk.END)
            self.update_status(f"Entry saved to: {file_path}")
            messagebox.showinfo("Success", "Entry saved!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save:\n{str(e)}")
