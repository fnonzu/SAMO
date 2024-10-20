import sys
from datetime import datetime
from core.samo_manager import SamoManager
from core.analysis import analyze_diary

def get_note_content():
    """Get multi-line note input from user with Ukrainian/English support"""
    print("\n📝 Enter your note (Press Enter twice to finish):")
    lines = []
    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            print("\n⚠️  Entry cancelled!")
            return None
        if line == "":
            if len(lines) > 0 and lines[-1] == "":
                lines.pop()
                break
        lines.append(line)
    return "\n".join(lines).strip()

def show_analysis_report():
    """Display analysis summary in CLI"""
    print("\n🔍 Analyzing your diary...")
    try:
        results = analyze_diary()
        print(f"\n📊 Analysis complete! Check these files:")
        print(f"📁 {results['wordcloud']}")
        print(f"📁 {results['frequency_chart']}")
        print(f"📁 {results['frequencies_file']}")
    except Exception as e:
        print(f"\n❌ Analysis failed: {str(e)}")

def cli_entry():
    """Main CLI interface"""
    print("\n" + "="*40)
    print("🌟 My Digital Diary CLI".center(40))
    print("="*40)
    
    while True:
        print("\nOptions:")
        print("1. ✍️  Write new entry")
        print("2. 📈 Run diary analysis")
        print("3. Exit")
        
        choice = input("\nChoose option (1-3): ").strip()
        
        if choice == "1":
            content = get_note_content()
            if content:
                try:
                    path = SamoManager.save_entry(content)
                    print(f"\n✅ Saved to: {path}")
                except Exception as e:
                    print(f"\n❌ Save failed: {str(e)}")
                    
        elif choice == "2":
            show_analysis_report()
            
        elif choice == "3":
            print("\n📔 Keep writing your story! Goodbye!\n")
            sys.exit(0)
            
        else:
            print("\n⚠️  Invalid option, please try again")

if __name__ == "__main__":
    cli_entry()
