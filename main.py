"""Last Out of Office: The AI That Went Barista — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The reply: the agent quit to pull espresso shots — your email waits between latte art.
TEXT = "I am out of office — I have quit to become a barista. Your email will be answered between latte art and my new life."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
