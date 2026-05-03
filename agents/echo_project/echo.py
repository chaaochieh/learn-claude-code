#!/usr/bin/env python3
"""A simple echo program that repeats user input."""

def main():
    print("Echo Program - Type something and press Enter to echo it back!")
    print("Type 'quit' or 'exit' to exit.\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ('quit', 'exit', 'q'):
            print("Goodbye!")
            break
        
        print(f"Echo: {user_input}")

if __name__ == "__main__":
    main()