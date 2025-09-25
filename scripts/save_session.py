"""Small helper to append LLM session data with timestamps.

Usage example:
    python scripts/save_session.py labs/class01/labA_completion/llm_output.md "Option 1: ..."
"""
import sys, datetime, pathlib

def main():
    if len(sys.argv) < 3:
        print("Usage: save_session.py <file> <text>")
        sys.exit(1)
    path = pathlib.Path(sys.argv[1])
    text = sys.argv[2]
    ts = datetime.datetime.now().isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"\n\n---\nTimestamp: {ts}\n{text}\n")
    print(f"Appended to {path}")

if __name__ == "__main__":
    main()
