# Simple calculator with addition, subtraction, multiplication, and division.
def add(x,y):
    return x + y
def min(x,y):
    return x - y
def multi(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return("Error")
    else:
        return x / y

def calculator():
    print("--- Chemistry Significant Figure Calculator ---")

    while True:
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
    
        if choice == '5':
            print("Exiting calculator...")
            break
        if choice in ('1','2','3','4'):
            try:
                num_1 = float(input("Enter your first number: "))
                num_2 = float(input("Enter your second number: "))
            except ValueError:
                print("Invalid number, please only enter numbers")
                continue

        if choice == '1':
            print(f"Result: {num_1} + {num_2} = {add(num_1,num_2)}")
        elif choice == '2':
            print(f"Result: {num_1} - {num_2} = {min(num_1,num_2)}")
        elif choice == '3':
            print(f"Result: {num_1} * {num_2} = {multi(num_1,num_2)}")
        elif choice == '4':
            print(f"Result: {num_1} / {num_2} = {div(num_1,num_2)}")        
        else:
            print("Invalid selection")

if __name__ == "__main__":
    calculator()
