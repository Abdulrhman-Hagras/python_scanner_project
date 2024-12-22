grammar = []

def add_grammar():
    print("Enter grammar rules (type 'done' to finish):")
    while True:
        rule = input("Rule: ").strip()  # Remove extra spaces
        if rule.lower() == "done":      # Exit loop if user types 'done'
            break
        grammar.append(rule)           # Add rule to grammar list
    print("Grammar saved:", grammar)   # Display saved rules

def test_grammar():
    if not grammar:  # If no rules exist, prompt to add grammar first
        print("No grammar rules found. Add grammar first.")
        return
    simple_tokens = {"KEYWORD", "IDENTIFIER", "SYMBOL", "NUMBER"}
    print("The grammar is simple." if all(rule in simple_tokens for rule in grammar) else "The grammar is not simple.")

def test_input():
    if not grammar:  # Ensure grammar is defined
        print("No grammar rules found. Add grammar first.")
        return
    input_text = input("Enter the input text: ").strip()
    words = input_text.split()  # Split input into words

    tokens = []  # Tokenize the input text
    for word in words:
        if word.isalpha():  # Check if word contains only letters
            tokens.append("KEYWORD" if word in ["int", "float", "if", "else"] else "IDENTIFIER")
        elif word.isdigit():  # Check if word is a number
            tokens.append("NUMBER")
        else:  # Treat other characters as symbols
            tokens.append("SYMBOL")

    # Compare tokens with grammar rules
    if tokens == grammar:
        print("Input matches the grammar.")
    else:
        print("Input does not match the grammar.")
        print("Expected:", grammar)
        print("Got:", tokens)

def main():
    while True:
        print("\nChoose an option:\n1. Add grammar\n2. Test if grammar is simple\n3. Test input against grammar\n4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_grammar()
        elif choice == "2":
            test_grammar()
        elif choice == "3":
            test_input()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
