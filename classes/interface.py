from books import Store


class StoreInterface:
    
    def __init__(self, store_name):
        self.store = Store(store_name)
        
    def run(self):
        print(f"""
===== WELCOME TO {self.store.name.upper()}! =====
        """)
        while True:
            mode = input(self.menu())
            if mode == '1':
                book_title = input('Enter a title to search for :\n')
                if book_title.isspace():
                    print("Your book title is not valid.\n")
                    self.menu()
                elif book_title.isalnum() or " " in book_title or "," in book_title: 
                    self.store.search_for_a_book(book_title)
                    add_book = input("\nwould you like to add any of these books to your reading list? (y/n) ")
                    if add_book == 'y' or add_book == 'Y':
                        self.store.add_book_to_reading_list()
                        add_book = input("\nwould you like to would you like to add another book to your reading list? (y/n) ")
                        if add_book == 'y' or add_book == 'Y':
                            self.menu()
                        else:
                            print('You have either selected "no", or did not select a valid option, you will now be redirected to the main menu.\n')
                            self.menu()
                    else:
                        print('You have either selected "no", or did not select a valid option, you will now be redirected to the main menu.\n')
                        self.menu()
                else:
                    print("Your book title is not valid.\n")
                    self.menu()

            elif mode == '2':
                self.store.view_reading_list()
                menu = input('\npress [1] to return to the home screen, press any other key to exit: ')
                if menu == '1':
                    self.menu()
                else:
                    self.store.save_read_list()
                    break

            elif mode == '3':
                self.store.save_read_list()
                print((f"""
                
===== THANK YOU FOR USING {self.store.name.upper()} =====
        
        """))
                break 
            
            else:
                print("You have not selected a valid option, you will now be redirected to the main menu.\n")
                self.menu()
                


    def menu(self):
        return"""
------- What would you like to do? -------
[1] Search for a Book
[2] View curent reading list
[3] Quit
"""