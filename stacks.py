"""
Stack implementation using Python

Operations include:
    1. Display
    2. Push
    3. Pop
    4. Peek
    5. Check if empty
    6. Get size
    7. Clear stack
"""
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("Stack Operations Menu:")
    print("1. Display stack")
    print("2. Push")
    print("3. Pop")
    print("4. Peek")
    print("5. Check if stack is empty")
    print("6. Get size")
    print("7. Clear the stack")
    print("8. Exit")

stack = []

def main():

    print("Welcome!\n")
    while True:
        menu()
        choice = int(input(": "))

        if choice == 1:
            print("\nStack:", stack, "\n")

        elif choice == 2:
            x = input("\nEnter item to be pushed: ")
            stack.append(x)
            print(x, "pushed into the stack successfully.\n")

        elif choice == 3:
            if len(stack) > 0:
                stack.pop()
                print("\nStack popped successfully.\n")
            else:
                print("\nStack underflow.\n")

        elif choice == 4:
            print("\nTop: ", stack[-1], "\n")

        elif choice == 5:
            if len(stack) == 0:
                print("\nStack is empty.\n")
            else:
                print("\nStack is not empty.\n")

        elif choice == 6:
            print("\nSize of stack: ", len(stack), "\n")

        elif choice == 7:
            stack.clear()
            print("\nStack cleared successfully.\n")

        elif choice == 8:
            print("\nGoodbye!\n")
            break

        else:
            print("\nInvalid choice, try again.\n")

if __name__ == "__main__":
    clear_screen()
    main()