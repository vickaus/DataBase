from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            item = self.show_menu()
            if item == '1':
                self.views()
            elif item == '2':
                self.add()
            elif item == '3':
                self.editing()
            elif item == '4':
                self.delete()
            elif item == '5':
                self.generated_shop()
            elif item == '6':
                break

    def show_menu(self):
        self.view.show_message("\n MENU")
        self.view.show_message("-1. View")
        self.view.show_message("--2. Add")
        self.view.show_message("---3. Editing")
        self.view.show_message("----4. Delete")
        self.view.show_message("-----5. Generated values in Shop")
        self.view.show_message("------6. Exit")
        return input("Input number of menu: ")


    def menu(self):
        self.view.show_message("\n Choose the table:")
        self.view.show_message("-1. Shop")
        self.view.show_message("--2. Product")
        self.view.show_message("---3. Order")
        self.view.show_message("----4. User")
        self.view.show_message("-----5. Delivery")
        self.view.show_message("------6. Exit")
        return input(" Input number of table: ")

    def views(self):
        self.view.show_message("\nView:")
        while True:
            item = self.menu()
            if item == '1':
                self.view_shops()
            elif item == '2':
                self.view_product()
            elif item == '3':
                self.view_order()
            elif item == '4':
                self.view_user()
            elif item == '5':
                self.view_del()
            elif item == '6':
                break
    def add(self):
        self.view.show_message("\nAdd:")
        while True:
            item1 = self.menu()
            if item1 == '1':
                self.add_shop()
            elif item1 == '2':
                self.add_product()
            elif item1 == '3':
                self.add_order()
            elif item1 == '4':
                self.add_user()
            elif item1 == '5':
                self.add_del()
            elif item1 == '6':
                break

    def editing(self):
        self.view.show_message("\nEdit:")
        while True:
            item2 = self.menu()
            if item2 == '1':
                self.editing_shop()
            elif item2 == '2':
                self.editing_product()
            elif item2 == '3':
                self.editing_order()
            elif item2 == '4':
                self.editing_user()
            elif item2 == '5':
                self.editing_del()
            elif item2 == '6':
                break

    def delete(self):
        self.view.show_message("\nDelete:")
        while True:
            item3 = self.menu()
            if item3 == '1':
                self.delete_shop()
            elif item3 == '2':
                self.delete_product()
            elif item3 == '3':
                self.delete_order()
            elif item3 == '4':
                self.delete_user()
            elif item3 == '5':
                self.delete_del()
            elif item3 == '6':
                break

    def generated_shop(self):
        val = self.view.gen_values()
        if val.isdigit():
            self.model.gen_shop(val)
        else:
            print("Error! It must be correct type..")

    # Shop
    def view_shops(self):
        shops = self.model.get_all_shops()
        self.view.show_shops(shops)
    def add_shop(self):
        shop_name = self.view.get_shop_name()
        shop_phone = self.view.get_shop_phone()
        if shop_name.isalpha() and shop_phone.isdigit():
            self.model.add_shop(shop_name, shop_phone)
        else:
            print("Error! It must be correct type..")
    def editing_shop(self):
        shop_id = self.view.get_shop_id()
        shop_name = self.view.get_shop_name()
        shop_phone = self.view.get_shop_phone()
        if shop_id.isdigit() and shop_name.isalpha() and shop_phone.isdigit():
            self.model.editing_shop(shop_id, shop_name, shop_phone)
        else:
            print("Error! It must be correct type..")
    def delete_shop(self):
        shop_id = self.view.get_shop_id()
        if shop_id.isdigit():
            self.model.delete_shop(shop_id)
        else:
            print("Error! It must be correct type..")



    # Product
    def view_product(self):
        product = self.model.get_all_products()
        self.view.show_products(product)
    def add_product(self):
        shop_id, product_name, product_price = self.view.get_product_input()
        if shop_id.isdigit() and product_name.isalpha() and product_price.isdigit():
            self.model.add_product(shop_id, product_name, product_price)
        else:
            print("Error! It must be correct type..")
    def editing_product(self):
        product_id = self.view.get_product_id()
        shop_id, product_name, product_price = self.view.get_product_input()
        if product_id.isdigit() and shop_id.isdigit() and product_name.isalpha() and product_price.isdigit():
            self.model.editing_product(product_id, shop_id, product_name, product_price)
        else:
            print("Error! It must be correct type..")
    def delete_product(self):
        product_id = self.view.get_product_id()
        if product_id.isdigit():
            self.model.delete_product(product_id)
        else:
            print("Error! It must be correct type..")



    # Order
    def view_order(self):
        orders = self.model.get_all_order()
        self.view.show_orders(orders)
    def add_order(self):
        matrix_product_id = []
        id_user = self.view.get_user_id()
        num_product = self.view.get_num_product()
        id_del = self.view.get_del_id()
        for k in range(int(num_product)):
            matrix_product_id.append(self.view.get_product_id())
        if id_user.isdigit() and num_product.isdigit() and id_del.isdigit():
            self.model.add_order(id_user, matrix_product_id, num_product, id_del)
        else:
            print("Error! It must be correct type..")
    def editing_order(self):
        matrix_product_id = []
        order_id = self.view.get_order_id()
        user_id = self.view.get_user_id()
        num_product = self.view.get_num_product()
        id_del = self.view.get_del_id()
        for k in range(int(num_product)):
            matrix_product_id.append(self.view.get_product_id())
        if order_id.isdigit() and user_id.isdigit() and id_del.isdigit():
            self.model.editing_order(matrix_product_id, num_product, order_id, user_id, id_del)
        else:
            print("Error! It must be correct type..")
    def delete_order(self):
        order_id = self.view.get_order_id()
        if order_id.isdigit():
            self.model.delete_order(order_id)
        else:
            print("Error! It must be correct type..")



    #User
    def view_user(self):
        user = self.model.get_all_user()
        self.view.show_user(user)
    def add_user(self):
        name, phone = self.view.get_user_input()
        if name.isalpha() and phone.isdigit():
            self.model.add_user(name, phone)
        else:
            print("Error! It must be correct type..")
    def editing_user(self):
        user_id = self.view.get_user_id()
        name, phone = self.view.get_user_input()
        if user_id.isdigit() and name.isalpha() and phone.isdigit():
            self.model.editing_user(user_id, name, phone)
        else:
            print("Error! It must be correct type..")
    def delete_user(self):
        id_user = self.view.get_user_id()
        if id_user.isdigit():
            self.model.delete_user(id_user)
        else:
            print("Error! It must be correct type..")



    # Delivery
    def view_del(self):
        delivery = self.model.get_all_delivery()
        self.view.show_del(delivery)
    def add_del(self):
        time, adress = self.view.get_del_input()
        self.model.add_del(time, adress)
    def editing_del(self):
        id_del = self.view.get_del_id()
        time, adress = self.view.get_del_input()
        if id_del.isdigit():
            self.model.editing_del(id_del, time, adress)
        else:
            print("Error! It must be correct type..")
    def delete_del(self):
        id_del = self.view.get_del_id()
        if id_del.isdigit():
            self.model.delete_del(id_del)
        else:
            print("Error! It must be correct type..")
