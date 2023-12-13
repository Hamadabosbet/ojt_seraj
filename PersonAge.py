from Person import Person




def main():
    name=(input('Please enter a persons name.\n'))
    age = int(input('Please enter a persons age.\n'))
    person=Person(name,age)

    person.printAge()

if __name__=="__main__":
    main()