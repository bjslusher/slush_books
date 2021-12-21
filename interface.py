from books import *
home_selection = ''


def home():
    home_selection = input("""
    ------- What would you like to do? -------
    [1] Search for a Book
    [2] View curent reading list
    [3] Quit
    """)
    return home_selection

def options(home_selection):
    if home_selection == '1':
        search_for_a_book()
        view_search_results()
        add_book = input("\nwould you like to add any of these books to your reading list? (y/n) ")
        if add_book == 'y' or add_book == 'Y':
            add_book_to_reading_list()
            add_book = input("\nwould you like to would you like to add another book to your reading list? (y/n) ")
            if add_book == 'y' or add_book == 'Y':
                search_for_a_book()
                save_read_list()
            else:
                options(home())
        else:
            options(home())

    elif home_selection == '2':
        view_reading_list()
        menu = input('\npress [1] to return to the home screen, press any other key to exit: ')
        if menu == '1':
            options(home())
        else:
            exit

    else:
        exit


options(home())



    