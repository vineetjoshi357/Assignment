import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            description TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY,
            ingredient TEXT UNIQUE NOT NULL,
            quantity INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS allergens (
            id INTEGER PRIMARY KEY,
            allergen TEXT UNIQUE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY,
            product_name TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Functions for managing seasonal flavors
def add_seasonal_flavor(name, description):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO seasonal_flavors (name, description) VALUES (?, ?)', (name, description))
        conn.commit()
        print("Flavor added successfully!")
    except sqlite3.IntegrityError:
        print("Flavor already exists!")
    conn.close()

def search_flavors(keyword):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors WHERE name LIKE ?', (f'%{keyword}%',))
    results = cursor.fetchall()
    conn.close()
    return results

# Functions for managing allergens
def add_allergen(allergen):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO allergens (allergen) VALUES (?)', (allergen,))
        conn.commit()
        print("Allergen added successfully!")
    except sqlite3.IntegrityError:
        print("Allergen already exists!")
    conn.close()

# Functions for managing cart
def add_to_cart(product_name):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO cart (product_name) VALUES (?)', (product_name,))
        conn.commit()
        print("Product added to cart!")
    except sqlite3.IntegrityError:
        print("Product already in cart!")
    conn.close()

def view_cart():
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    items = cursor.fetchall()
    conn.close()
    return items

# Application interface
def main():
    setup_database()
    while True:
        print("\nWelcome to the Ice Cream Parlor!")
        print("1. Add Seasonal Flavor")
        print("2. Search Seasonal Flavors")
        print("3. Add Allergen")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter flavor name: ")
            description = input("Enter flavor description: ")
            add_seasonal_flavor(name, description)
        elif choice == '2':
            keyword = input("Enter search keyword: ")
            results = search_flavors(keyword)
            if results:
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}")
            else:
                print("No flavors found.")
        elif choice == '3':
            allergen = input("Enter allergen name: ")
            add_allergen(allergen)
        elif choice == '4':
            product_name = input("Enter product name to add to cart: ")
            add_to_cart(product_name)
        elif choice == '5':
            cart_items = view_cart()
            if cart_items:
                for item in cart_items:
                    print(f"Product: {item[1]}")
            else:
                print("Cart is empty.")
        elif choice == '6':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
