#The code is an interactive menu which enable the user navigate through options and be able to add or remove items using the .append() and .remove().
#Below is a welcome intro.
while True:
    name = input('Enter Name:')
    age = int(input('Enter age:'))
    if age <= 17:
        print('You are young for the platform')
        break
    else:
        print('YOU CAN MOVE TO THE MAIN MAIN.')
        


    print('-----------------------------')
    items = ['Shoe','Clothes','Tops']
    print("\n ----MENU----")
    print("1. Veiw items")
    print("2. Add items")
    print("3. Remove items")
    print("4. Exit")
    #Starting up with the choices
    choice = input('Enter option:')
    #Control flow
    if choice == "1":
        if not items:
            print("No items in the list")
        else:
            print(f"-{items}")
    elif choice == "2":
        item = input("Enter Item to add in the list:")
        items.append(item)
        print(f"{item} added")

    elif choice == "3":
        item = input("Enter Item to remove from the list:")
        if item in items:
            items.remove(item)
            print(f"{item} removed")
        else:
            print(f"'{item}'removed")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter option in the menu")
       
        
        
                          
                          
        


   
         
          
           
     
      
            
           
      
     
         
            
         
            
          
          

          

          
