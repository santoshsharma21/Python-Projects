# import module
from scripts.bms import BakeryManagementSystem

# run program
if __name__ == "__main__":
    # instance of BakeryManagementSystem
    bms = BakeryManagementSystem()
    
    # print options
    print("1. Add Order")
    print("2. View Order")
    print("3. Update Order")
    print("4. Exit", "\n")
    task_continue = True
    while task_continue:
        valid_choice = False
        while not valid_choice:
            try:
                user_choice = int(input("Enter your choice : "))
                valid_choice = True
            except ValueError:
                print("Invalid choice, try again")
        if user_choice == 1:
            bms.add_order()
        elif user_choice == 2:
            bms.view_order()
        elif user_choice == 3:
            bms.update_order()
        elif user_choice == 4:
            task_continue = False
            break
        else:
            continue
