def display_menu():
  print("Shopping List Manager")
  print("1. Add Item")
  print("2. Remove Item")
  print("3. View List")
  print("4. Exit")
def main():
  shopping_list = []
  while True:
    display_menu()
    choice = input("Enter your choice!")
    
    if choice == '1':
      item = input("Enter the item to add: ")
      shopping_list.append(item)
      print(f"{item} has been added to the shopping list. ")
    elif choice == '2':
      item = input("enter the item to remove: ")
      if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} item has been removed from the shopping list. ")
      else:
        print(f"{item} not found in teh shopping list. ")
    elif choice == '3':
      print("shopping list")
      if not shopping_list:
        print("The list is currently empty.")
      else:
        for idx, item in enumerate(shopping_list, start=1):
          print(f"{idx}. {item}")
    elif choice == '4':
      print("Goodbye!")
      break
    else:
      print("INvalid choice. Please try again.")
 
   