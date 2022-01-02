import os.path
import csv

class Read:
    
    def __init__(self, title, publisher, authors):
        self.title = title
        self.publisher = publisher
        self.authors = authors
        
    @classmethod
    def read(cls):
        read_list = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/reading_list.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                read_list.append(Read(**dict(row)))

        return read_list