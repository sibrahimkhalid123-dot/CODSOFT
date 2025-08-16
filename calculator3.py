def fetch_number(label):
    while True:
        try:
            value = float(input(f"🔢 Enter {label} number: "))
            return value
        except ValueError:
            print("❌ That's not a valid number. Try again.")

def choose_action():
    print("\n🧭 What would you like to do?")
    print("  [A] Add")
    print("  [S] Subtract")
    print("  [M] Multiply")
    print("  [D] Divide")
    action = input("👉 Type A, S, M, or D: ").strip().upper()
    return action

def perform_action(x, y, action):
    if action == "A":
        return x + y
    elif action == "S":
        return x - y
    elif action == "M":
        return x * y
    elif action == "D":
        if y == 0:
            return "🚫 Division by zero is undefined."
        return x / y
    else:
        return "❓ Unknown operation."

def start_calculator():
    print("🧮 Welcome to your personal calculator!")
    num1 = fetch_number("first")
    num2 = fetch_number("second")
    operation = choose_action()
    outcome = perform_action(num1, num2, operation)
    print(f"\n📣 Result: {outcome}")

if __name__ == "__main__":
    start_calculator()