# recordings of (name, age, id)

# save new record
# search by id
# print age average
# print all names 
# print all ids
# print all records
# print specific record by index

records = []
entries = {}

# indexing in list - O(1)
# seraching in dictionary - O(1)

age_sum = 0
age_count = 0


def print_record(record):
    print(f"ID: {record['id']}")
    print(f"Name: {record['name']}")
    print(f"Age: {record['age']}")


def printAgesAverage():  
    if age_count == 0:
        print("0")
    else:
        print(f"{age_sum / age_count}")
    # s = 0
    # for r in records:
    #     s += int(r['age'])
    # avg = s/len(records) if len(records) > 0 else 0

    # print(f"{avg}")


def print_menu():
    print('1. Save a new entry')
    print('2. Search by ID')
    print('3. Print ages average')
    print('4. Print all names')
    print('5. print all IDs')
    print('6. print all entries')
    print('7. print entry by index')
    print('8. Exit')

# new_record
def saveNewEntry():
    global age_sum, age_count
    id = input("ID: ")
    if id in entries:
        print(f"Error: Id already exists { {'name': entries[id]['name'], 'age': entries[id]['age']} }")
        return 
    
    if not id.isdigit():
        print(f"Error: ID must be a number, {id} is not a number")
        return
    
    name = input("Name: ")
    age = input("Age: ")

    records.append({ 'id': id, 'name': name, 'age': age})
    entries['id'] = {'name': name, 'age': age}

    age_sum += int(age)
    age_count += 1

    print(f"ID [{id}] saved successfuly")
    

def printAllNames():
    for i,r in enumerate(records):
        print(f"{i}. {r['name']}")

def printAllIds():
    for i,r in enumerate(records):
        print(f"{i}. {r['id']}")

def printAllEntries():
    for i,r in enumerate(records):
        print(f"{i}. {r['id']}")
        print(f"\tName: {r['name']}")
        print(f"\tAge: {r['age']}")
    
def searchById():
    id_val = input("Please enter the ID you want to look for: ")
    if not id_val.isdigit():
        print(f"Error: ID must be a number. {id_val} is not a number.")
        return 

    if id_val in entries:
        print_record(entries[id_val])
        return

    print(f"Error: ID {id_val} is not saved")

def printEntryByIndex():
    index = input("Please enter the index of the entry you want to print: ")
    if not index.isdigit():
        print(f"Error: Index must be a number. {index} is not a number.")
        return 
    
    index = int(index)

    if index >= 0 and index < len(records):
        print_record(records[index]) 
    else:
        print(f"Index out of range. The maximum index allowed is {len(records)-1}")
        return 
        


while True:
    print_menu()
    try:
        choice = int(input("Please enter your choice: "))
    except:
        continue

    if choice == 1:
        saveNewEntry()
    elif choice == 2:
        searchById()
    elif choice == 3:
        printAgesAverage()
    elif choice == 4:
        printAllNames()
    elif choice == 5:
        printAllIds()
    elif choice == 6:
        printAllEntries()
    elif choice == 7:
        printEntryByIndex()
    elif choice == 8:
        ans = input("Are you sure? (y/n)")
        while ans != 'y' and ans != 'n':
            ans = input("Are you sure? (y/n) ")

        if ans == 'y':
            print('Goodbye!')
            exit()
        elif ans == 'n':
            continue
        
    else:
        print(f"Option [{choice}] does not exist. Please try again.")
        continue
    
    input("Press Enter to continue ")
