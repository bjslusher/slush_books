# slush_books
Application to search Google Books API

This application was built on python 3.9.9

before running this application:
please run "pip install -r requirements.txt" in your command terminal. 
alternatively, you could just use "pip install requests" from your command terminal

To begin application, run the (runner.py) file.

When the application loads, select the first option to search for a book. Alphanumeric characters, spacess and commas are read,
all other punctuation is not nessassary and may send you back to the main menu.  Once you find a book you would
like to add to your reading list, the application will save your selection to a .csv (reading_list.csv) file so you do not have to 
worry about leaving the program and comming back.  Your reading list will be right here waiting for you.  If you would like to 
print out your reading list, the file can be located in the data folder.



• Type in a query and display a list of 5 books matching that query.
• Each item in the list should include the book's author, title, and publishing company.
• A user should be able to select a book from the five displayed to save to a “Reading List”
• View a “Reading List” with all the books the user has selected from their queries -- this is a local reading list and not tied to Google Books’s account features.
