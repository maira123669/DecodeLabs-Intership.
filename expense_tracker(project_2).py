def main():
    total_spent = 0.0

    print("==========================================")
    print("      DECODELABS EXPENSE TRACKER          ")
    print("==========================================")
    print("Enter expense amounts. Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter expense ($) or 'quit': ").strip().lower()

        if user_input in ['quit', 'exit', 'done', 'stop']:
            print("\n------------------------------------------")
            print(f"FINAL TOTAL SPENT: ${total_spent:.2f}")
            print("------------------------------------------")
            break

        try:
            expense = float(user_input)

            if expense < 0:
                print("[!] Error: Expense cannot be negative.\n")
                continue

            total_spent += expense
            print(f"[+] Added: ${expense:.2f} | Current Total: ${total_spent:.2f}\n")

        except ValueError:
            print("[!] Invalid Data: Enter a valid number or 'quit'.\n")

if __name__ == "__main__":
    main()