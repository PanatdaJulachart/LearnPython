import datetime
def diary_menu():
    while True :
        print (">>Enter 1 for New Diary")
        print (">>Enter 2 for Read Diary")
        print (">>Enter 3 Exit")
    
        choice = int(input("Enter 1 2 3"))

        if choice == 1 :
            print (">>Creating a new diary page...")
            entry = input("Enter story today : ")

            now = datetime.datetime.now()
            time_str = now.strftime ("%d/%m/%y %H:%M")
            
            with open ("diary.txt", "a" , encoding="UTF-8") as file :
                file.write (f/"[{time_str}] {entry}/n") 
                file.write ("-" * 40 + "/n")
                
            print ("Saved successfully.")

        elif choice == 2 :
            print ("Opening diary page...")
            try:
                with open ("diary.txt", "r", encoding="UTF-8") as file :
                    content = file.read()
                    print(content)
            except FileNotFoundError : 
                print ("Please create a new diary.")

       
        elif choice == 3 :
            print ("Exit...")
            break

        else:
            print ("Please enter again.")



    diary_menu()