# List of favorite books (title, author)
favorite_books = [
    ("Lady of the Empire", "Raymond E. Feist"),
    ("Basic Econimics", "Thomas Sowell"),
    ("Echoes of Honor", "David Weber"),
    ("War is a Racket", "Smedley Butler"),
    ("We are Legion(We are Bob)", "Dennis E. Taylor"),
    ("The Forever War", "Joe Haldeman")

]

def threeBooks():
    return favorite_books[:3]


student_db = {
    1: {"firstName": "SpongeBob", "lastName": "SquarePants","Major": "Culinary Arts"},
    2: {"firstName": "Patrick", "lastName": "Star", "Major": "Chemistry"},
    3: {"firstName": "Sandy", "lastName": "Cheeks","Major": "Marine Biology"},
    4: {"firstName": "Squidward", "lastName": "Tentacles", "Major": "Clarinet"},
}

def studentInfo(id):
    return student_db.get(id)

if __name__=="__main__":
    print("My Favorite books:")
    print("Title : Author")
    for b in favorite_books:
        print(f"{b[0]} : {b[1]}")

    print("############################")
    print("Students in the db")    
    for ID,s in student_db.items():
        print(f"ID: {ID}, {s["firstName"]} {s["lastName"]}, Major: {s["Major"]}")    