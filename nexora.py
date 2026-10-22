import datetime
import random

NAME = "NEXORA AI"
VERSION = "0.1"

GREEN = "\033[92m"
RESET = "\033[0m"

def show_banner():
    print(GREEN + """
╔══════════════════════════════╗
║        NEXORA AI             ║
║   Your Personal Assistant    ║
║        Version 0.1           ║
╚══════════════════════════════╝
""" + RESET)

def get_response(message):
    text = message.lower().strip()

    if text in ["hello", "hi", "hey", "hello nexora"]:
        return "Hello! I'm Nexora, your personal assistant."

    if "your name" in text or "who are you" in text:
        return "I'm Nexora AI, your personal assistant."

    if "time" in text:
        now = datetime.datetime.now()
        return "The time is " + now.strftime("%I:%M %p")

    if "date" in text or "today" in text:
        today = datetime.datetime.now()
        return today.strftime("Today's date is %A, %d %B %Y.")

    if "creator" in text or "who made you" in text:
        return "I am being built by my creator, one step at a time!"

    if "joke" in text:
        jokes = [
            "Why do programmers love dark mode? Because light attracts bugs!",
            "There are 10 types of people: those who understand binary and those who don't.",
            "Why did the computer go to the doctor? It had a virus!"
        ]
        return random.choice(jokes)

    if text in ["help", "commands"]:
        return (
            "Try asking me:\n"
            "- Hello\n"
            "- What is your name?\n"
            "- What time is it?\n"
            "- What is today's date?\n"
            "- Tell me a joke\n"
            "- Who made you?\n"
            "- Type exit to close me."
        )

    return (
        "I heard you say: " + message +
        "\nMy basic brain doesn't know that answer yet. "
        "We're going to connect a real AI next!"
    )

def main():
    show_banner()
    print("NEXORA: Hello! What can I help you with?")
    print("Type 'help' to see commands.\n")

    while True:
        try:
            message = input("YOU > ").strip()

            if not message:
                continue

            if message.lower() in ["exit", "quit", "bye"]:
                print("NEXORA > Goodbye! See you soon.")
                break

            answer = get_response(message)
            print("\nNEXORA > " + answer + "\n")

        except KeyboardInterrupt:
            print("\nNEXORA > Shutting down. Goodbye!")
            break

if __name__ == "__main__":
    main()
