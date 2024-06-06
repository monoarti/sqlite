import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
''')

def add_expense(date, category, amount, description):
    c.execute('INSERT INTO Expenses (date, category, amount, description) VALUES (?, ?, ?, ?)', (date, category, amount, description))
    conn.commit()

def view_expenses():
    c.execute('SELECT * FROM Expenses')
    for row in c.fetchall():
        print(row)

def update_expense(id, date, category, amount, description):
    c.execute('UPDATE Expenses SET date = ?, category = ?, amount = ?, description = ? WHERE id = ?', (date, category, amount, description, id))
    conn.commit()

def delete_expense(id):
    c.execute('DELETE FROM Expenses WHERE id = ?', (id,))
    conn.commit()

def main_menu():
    while True:
        print("1. add")
        print("2. view")
        print("3. update")
        print("4. Delete")
        print("5. Exit")
        choice = input("choose one ")
        
        if choice == '1':
            date = input("date ")
            category = input("category : ")
            amount = float(input("amount : "))
            description = input("description : ")
            add_expense(date, category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            id = int(input("The cost ID you want to update: "))
            date = input("New date ")
            category = input("New category: ")
            amount = float(input("New amount "))
            description = input("New description: ")
            update_expense(id, date, category, amount, description)
        elif choice == '4':
            id = int(input("The cost ID you want to delete: "))
            delete_expense(id)
        elif choice == '5':
            print("Exit the program.")
            break
        else:
            print("The option is invalid. Please try again.")

if __name__ == '__main__':
    main_menu()