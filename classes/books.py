import requests
import csv
import os.path
from read import Read

class Store:
    
    def __init__(self, name):
        self.name = name
        self.reading_list = Read.read()
        self.search_list = []
        self.books_to_add = []
        

    def save_read_list(self):
        self.books_to_save()
        
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/reading_list.csv")
        
        with open(path, 'w') as csvfile:
            csvfile.truncate(0)
            reading_csv = csv.writer(csvfile, delimiter=',')
            reading_csv.writerow(["title" , "publisher" , "authors"])
            for books in self.books_to_add:
                reading_csv.writerow([books['title'], books['publisher'], books['authors']])
        self.books_to_add = []   
                        
    def search_for_a_book(self, book_title):
        self.search_list = []
        num = 1 
        
        search = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={book_title}&maxResults=5').json()
        
        for book in search['items']:
            book_info = {
                'title' : book['volumeInfo'].get('title'),
                'publisher' : book['volumeInfo'].get('publisher'),
                'authors': book['volumeInfo'].get('authors')
            }
            self.search_list.append(book_info)
    
        for book in self.search_list:
            print(f"""
        Selection: {num}
        Title: {book['title']} 
        Publisher: {book['publisher']}
        Authors: {book['authors']}""")
            num += 1

    def view_reading_list(self):
        if len(self.books_to_add) > 0:
            self.books_to_save()
            for num, book in enumerate(self.books_to_add):
                print(f"""
        Selection: {num + 1}
        Title: {book['title']} 
        Publisher: {book['publisher']}
        Authors: {book['authors']}""") 
        else:    
            if len(self.reading_list) == 0:
                print('\nYou do not have any items in your reading list')
            else:    
                print('\n')
                for num, book in enumerate(self.reading_list):
                    print(f"""
            Selection: {num + 1}
            Title: {book.title} 
            Publisher: {book.publisher}
            Authors: {book.authors}""")

    def add_book_to_reading_list(self):
        num = 1    
        for book in self.search_list:
            print(f"""
    {num}, Title: {book['title']}, Publisher: {book['publisher']}, Authors: {book['authors']}
        """)
            num += 1
        selection = input("please select a book number to add to your reading list (1-5): ")
        if selection == '1':
            self.books_to_add.append(self.search_list[0])
        elif selection == '2':
            self.books_to_add.append(self.search_list[1])
        elif selection == '3':
            self.books_to_add.append(self.search_list[2])
        elif selection == '4':
            self.books_to_add.append(self.search_list[3])
        elif selection == '5':
            self.books_to_add.append(self.search_list[4])
        else:
            print('You have not entered a valid option.')
            self.add_book_to_reading_list(self)
        
        
    def books_to_save(self):
        for num, book in enumerate(self.reading_list):
            book_info = {
            "title" : book.title, 
            "publisher" : book.publisher,
            "authors" : book.authors
            }
            self.books_to_add.append(book_info)
        