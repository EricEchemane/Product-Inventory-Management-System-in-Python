# Product Inventory Management System in Python
This is a command line or console application base on python. This application allows you to store data like a database where in you can create or add product, read data, as well as update and delete data.

Here the main storage of Data is a csv file inside the ./database/ folder.

### Features
- User Log-in System with **1 Layer of Encryption**
- View Product
- Add Product
- Update Product
- Delete Product
- Restore Deleted Products
  This feature is currently in the development process
  
### Used libraries
- Pandas
- Dataframe
- CSV

### File Contents
- **main.py**
  This is main interface and function of the program.
- **login.py**
  User login system with 1 strong layer of encryption.
- **masking.py**
  User defined function where in the characters you are typing is hidden in the console or replaced with an asterisk.
- **gotoxy.py**
  gotoxy function allow you to manipulate console cursor position set by the given point x and y. This is very helpful in organizing user inputs and prompts.
- **database folder**
  - **inventory.csv**
    Main storage of the products
  - **deleted.py**
    Back-up file for unintentional deletion
