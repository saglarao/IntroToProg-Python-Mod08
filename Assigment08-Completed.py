# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# SOrellana,06/05/2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ''

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SOrellana,06/05/2022,Modified code to complete assignment 8
    """
    # Constructor ------------------------------------- #
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    # Properties -------------------------------------- #
    # product name
    @property   # getter decorator
    def product_name(self):
        return str(self.__product_name_str).title()

    @product_name.setter    # setter decorator
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name_str = value
        else:
            raise Exception('Product name cannot be number')

    # product price
    @property      # getter decorator
    def product_price(self):
        return str(self.__product_price_str)

    @product_price.setter      # setter decorator
    def product_price(self, value):
        if str(value).isnumeric() == True:
            self.__product_price_str = value
        else:
            raise Exception('Price must be in numbers')

    # Methods -------------------------------------------- #
    def __str__(self):
        return self.product_name + ',' + self.product_price

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SOrellana,06/05/2022,Modified code to complete assignment 8
    """

    def read_data_from_file(self, file_name, list_of_product_objects):
        """ Reads data from a file into a list of rows

        :param file_name: (string) with name of file:
        :return: list_of_product_objects: (list) of objects
        """
        list_of_product_objects.clear()
        with open(file_name, 'r') as file:
            for line in file:
                product, price = line.split(',')
                obj_product = Product(product, price.strip())
                list_of_product_objects.append(obj_product)
        return list_of_product_objects


    def save_data_to_file(self, file_name, list_of_product_objects):
        """ Saves list of product objects to a file
        :param file_name: (string) with file name
        :param list_of_product_objects: (list) of objects
        """
        with open(file_name, 'w') as file:
            for row in list_of_product_objects:
                file.write(str(row) + '\n')
        return 'Data was saved. Goodbye!'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """
    Displaying and collecting user data:

    static methods:
        show_menu():
        input_user_choice(): -> (string) with menu choice
        print_current_data(list_of_product_objects):
        add_product(): -> (object)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SOrellana,06/05/2022,Modified code to complete assignment 8
    """

    @staticmethod
    def show_menu():
        """ Display a menu of choices to the user
        :return: nothing
        """
        print('-' * 33)
        print('''Menu of Options:
        1) Show Current List of Products
        2) Add New Product
        3) Save Data to a File and Exit''')
        print('-' * 33)

    @staticmethod
    def input_user_choice():
        """ Gets menu choice from user
        :return: string
        """
        choice = str(input('Which option would you like to perform? [1 to 3]: '))
        print('-' * 33)  # for looks
        return choice

    @staticmethod
    def print_current_data(list_of_product_objects):
        """ Displays current list of products
        :param list_of_product_objects: (list) with products and prices
        :return: nothing
        """
        print('-----Current List Of Products----')
        for row in list_of_product_objects:   # looping through objects in the list
            print(str(row))
        print()   # extra line for looks

    @staticmethod
    def add_product(list_of_product_objects):
        """ Adds a new product object to the list
        :param list_of_product_objects: (list) of product objects
        :return: (list) of product objects
        """
        try:
            product = input('Please enter a product: ')
            price = input('Please enter product price: ')
            obj_product = Product(product, price)    # new object from Product class
            list_of_product_objects.append(obj_product)
        except Exception as e:   # catching errors for invalid input values
            print(e)
        return list_of_product_objects

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
try:
    objF = FileProcessor()
    lstOfProductObjects = objF.read_data_from_file(strFileName, lstOfProductObjects)
    print('-----Current data in file-------')
    for row in lstOfProductObjects:     # looping through objects in the list
        print(str(row))

except FileNotFoundError as e:
    print('File does not exist, it will be saved after data is added')
    print(e)
while True:
# Show user a menu of options
    IO.show_menu()
# Get user's menu option choice
    strChoice = IO.input_user_choice()
    # Show user current data in the list of product objects
    if strChoice == '1':
        IO.print_current_data(lstOfProductObjects)
    # Let user add data to the list of product objects
    elif strChoice == '2':
        lstOfProductObjects = IO.add_product(lstOfProductObjects)
    # let user save current data to file and exit program
    elif strChoice == '3':
        objF = FileProcessor()
        print(objF.save_data_to_file(strFileName, lstOfProductObjects))
        break
    else:
        print('Choose 1 to 3 only!')

# Main Body of Script  ---------------------------------------------------- #

