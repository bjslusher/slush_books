import requests
import csv
import os.path


search_list = []
reading_list =[]

def read_list():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "./reading_list.csv")
    
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book_info = {
                'title' : row.title,
                'publisher' : row.publisher,
                'authors': row.authors
        }
            search_list.append(book_info)

    return reading_list
        
def save_read_list():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "./reading_list.csv")

    with open(path, 'w') as csvfile:
        reading_csv = csv.writer(csvfile, delimiter=',')
        reading_csv.writerow(["title" , "publisher" , "authors"])
        for books in reading_list:
            reading_csv.writerow([books['title'], books['publisher'], books['authors']])   
                     
def search_for_a_book():
    book_search = input("Book Search: ")
    r = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={book_search}&maxResults=5').json()

    for i in r['items']:
        book_info = {
            'title' : i['volumeInfo'].get('title'),
            'publisher' : i['volumeInfo'].get('publisher'),
            'authors': i['volumeInfo'].get('authors')
        }
        search_list.append(book_info)

def view_search_results():
    num = 1    
    for book in search_list:
        print(f"""
    Selection: {num}
    Title: {book['title']} 
    Publisher: {book['publisher']}
    Authors: {book['authors']}""")
        num += 1

def view_reading_list():
    read_list()
    num = 1
    if len(reading_list) == 0:
        print('You do not have any items in your reading list')
    else:    
        for book in reading_list:
            print(f"""
        Selection: {num}
        Title: {book['title']} 
        Publisher: {book['publisher']}
        Authors: {book['authors']}""")
            num += 1

def add_book_to_reading_list():
    num = 1    
    for book in search_list:
        print(f"""
{num}, Title: {book['title']}, Publisher: {book['publisher']}, Authors: {book['authors']}
    """)
        num += 1
    selection = input("please select a book number to add to your reading list (1-5): ")

    if selection == '1':
        reading_list.append(search_list[0])
    elif selection == '2':
        reading_list.append(search_list[1])
    elif selection == '3':
        reading_list.append(search_list[2])
    elif selection == '4':
        reading_list.append(search_list[3])
    elif selection == '5':
        reading_list.append(search_list[4])
        
            