from expense import Expense

def main():
    print(f"running expense tracker!")
    
    # take input from user for expense 
    get_user_expense()
    expense_name = input("Enter Expense Name:")
    expense_amount = float(input("Enter amount:"))
    print(f"you've entered {expense_name}, {expense_amount}")

    expense_category = [
        "food" , 
        "home" ,
        "transportation" ,
        "internet"]
    
    while True:
        print("select category:")
        # i stands for index of item , value of the item.
        for i, category_name in enumerate (expense_category):
             print(f" {i +1}.{category_name} ")
        value_range = f"[1 - {len(expense_category)}]"

        selected_index = int(input(f"enter category number {value_range}:")) -1 
        if selected_index in range(len(expense_category)) :
            selected_category = expense_category
            new_expense = Expense(name = expense_name , category = selected_category , amount = expense_amount ) #using the class Expence from the other file 

            return  new_expense
        
        else :
            print("invalid category pls , check entered value!")
     


    #write the expense on a list or dict
    save_expense_inlist()


    #read and summurize expenses from the list or dict
    read_summurize_expense()


def get_user_expense():
    print(f"Get user expense...")  
    

def save_expense_inlist():
    print(f"Save user expense...")     

def read_summurize_expense():
    print(f"summurize user expense...") 

if __name__ == "__main__":
    main()