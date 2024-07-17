class shop:
    def __init__(self):
        self.pid = 0
        self.pname = ""
        self.amt = 0

    def add(self):
        cnt = 0
        self.pid = int(input('Enter Product id :'))
        self.pname = input('Enter Product name :')
        self.amt = int(input('Enter Product price :'))
        cnt += 1
   
    def dlt():
        id = input('Enter Id you want to delete :')
        for i in range(len(products)):
            if id == str(products[i].pid):
                products.pop(i)
                print('Product deleted successfully')
                break
            else:
                print('Product not found')
    def total():
        total_amt = 0
        for i in products:
            total_amt += i.amt
        print('Total amount :',total_amt)

class display(shop):
     def show(self):
        print('Product id :',self.pid)
        print('Product Name :',self.pname)
        print('Product Price :',self.amt)

products = []
while True:
    print('Menu:')
    print('1. Add Product')
    print('2. Display Products')
    print('3. Delete Product')
    print('4. Calculate Total Amount')
    print('5. Quit')
    
    choice = input('Enter Choice: ')
    if choice == '1':
        p = display()
        p.add()
        products.append(p)
        print('Product Added succesfully')
    elif choice == '2':
        for product in products:
            product.show()
    elif choice == '3':
        shop.dlt()
    elif choice == '4':
        shop.total()
    elif choice == '5':
        print('Thank you')
        break
