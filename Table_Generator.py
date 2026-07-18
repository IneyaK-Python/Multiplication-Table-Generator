# ---  Multiplication Table Tool ---
# Beginner Python Team Assignment

def run_table_generator():
    print("==================================================")
    print("   Welcome to the Multiplication Table System   ")
    print("==================================================")
    
    # Keeps the program running in a loop until the user decides to stop
    while True:
        try:
            # Gather input from the user
            user_entry = input("\nEnter a whole number to view its table (or type 'exit' to stop): ")
            
            # Check if the user wants to leave the application
            if user_entry.strip().lower() == 'exit':
                print("Closing the program. Thank you for practicing math today!")
                break
                
            # Change the text input into an integer whole number
            target_number = int(user_entry)
            
            # Print a neat header for the multiplication output
            print(f"\n[ Showing Table For: {target_number} ]")
            print("=" * 28)
            
            # Loop from 1 to 10 to calculate and structure each line cleanly
            for row in range(1, 11):
                product = target_number * row
                print(f" {target_number}  x  {row:2d}  =  {product}")
                
            print("=" * 28)
            
        except ValueError:
            # Triggers a helpful warning if they type letters, symbols, or decimals
            print("⚠️ Input Error: That is not a valid whole number. Please try again.")

# Automatically executes the function when the script runs
if _name_ == "_main_":
    run_table_generator()
