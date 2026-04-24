B=[] #list for books
def add_books():
    add_book=input("which book you want to add to collection:-")
    B.append(add_book)
    print(f"{add_book},added succesfully :)")
def show_books():
    print(f"the available books :-{B}")
def return_books():
    return_book=input("which book you want to return:-")
    B.append(return_book)
    print(f"{return_book},added succesfully :)")
def issue_books():
    issued_book=input(f"which book you want? here's the books:-{B}")
    B.remove(issued_book)
    print(f"{issued_book},issued succesfully :)")         
def library():
    while True:
        print("1.add books")
        print("2.show books")
        print("3.return books")
        print("4.issue books")
        print("5.exit")
        choice=int(input("enter number 1 to 5:-"))
        if choice==1:
            add_books()
        elif choice==2:
            show_books()
        elif choice==3:
            return_books()
        elif choice==4:
            issue_books() 
        elif choice == 5:
           print("Exiting...")
           break              
    
library() #calling library