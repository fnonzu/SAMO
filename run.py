import argparse
import sys
from gui.diary_gui import DiaryApp
from cli.diary_cli import cli_entry

def check_tkinter():
    try:
        import tkinter
        return True
    except ImportError:
        return False

def main():
    parser = argparse.ArgumentParser(description="Digital Diary System")
    parser.add_argument('--cli', action='store_true', help='Launch TUI version')
    args = parser.parse_args()

    if args.cli:
        cli_entry()
    else:
        if check_tkinter():
            app = DiaryApp()
            app.mainloop()
        else:
            print("Error: Tkinter required for GUI. Install with:")
            print("Linux: sudo apt-get install python3-tk")
            print("Mac: Install ActiveTcl from https://www.activestate.com/products/tcl/")
            print("Windows: Should be included by default")
            sys.exit(1)

if __name__ == "__main__":
    main()
