class Library():
    def __init__(self):
        self.file = open("books.txt","a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_inf = self.file.readlines()

        if not book_inf:
            print("There aren't any books in the libary")
            return


        for item in book_inf:
            books = item.split(',')
            print(f"Title: {books[0]},Author: {books[1]}")







    def add_books(self):
        title = input("Enter the title:")
        author = input("Enter the author:")
        release_year = input("Enter the release year:")
        page_number = input("Enter the number of pages:")
        book_ınf =f"{title},{author},{release_year},{page_number}\n"
        self.file.write(book_ınf)
        print("Book added successfully")





    def remove_book(self):
        title =input("Enter the title of the book you want to remove:")
        lines = self.file.readlines()
        self.file.seek(0)
        books = []
        for book in self.file.readlines():
            if title.lower() not in book.lower():
                books += book
        self.file.seek(0)
        self.file.truncate(0)
        self.file.writelines(books)
        if lines != books:
            print("This book doesn't exist")
        else:
            print("The book removed succesfully")










def main():
    lib = Library()

    while (True):
        print("***MENU***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")



        click = input("Choose the action you want to do:")

        if click =='1':
            lib.list_books()
        if click == '2':
            lib.add_books()
        if click=='3':
            lib.remove_book()












if  __name__ == "__main__":
    main()









