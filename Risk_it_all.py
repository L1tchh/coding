import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.065):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    print_slow("RISK IT ALL - BRUNO MARS", 0.09)
    print_slow("=" * 45, 0.02)
    time.sleep(1.2)
    
    lyrics = [
        "To hold your hand and call you mine",
        "I'm tryna be your man 'til the end of time",
        "Oh, I'll do anything, anything you ask me to",
        "",
        "I would run through a fire",
        "Just to be by your side",
        "If your heart's on the line",
        "You could take mine",
        "",
        "It's crazy, but it's true",
        "There's nothing I won't do",
        "I'd risk it all for you"
    ]
    
    for line in lyrics:
        if line.strip() == "":
            print()
            time.sleep(1.0)
        else:
            print_slow("  " + line, 0.07)
            time.sleep(0.55)
    
    print_slow("\n" + "=" * 45, 0.02)
    print_slow("Bruno Mars", 0.09)

if __name__ == "__main__":
    main()