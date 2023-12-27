class View:
    def show_message(self, message):
        print(message)

    #Shop
    def show_shops(self, Shop):
        if Shop:
            print("Shops:")
            for shops in Shop:
                print(f"Shop id: {shops[0]}, name shop: {shops[1]}, phone shop: {shops[2]}")
        else:
            print("Not found!")

    def get_shop_name(self):
        shop_name = input("Input shop name: ")
        return shop_name

    def get_shop_id(self):
        shop_id = input("Input shop id: ")
        return shop_id

    def get_shop_phone(self):
        shop_phone = input("Input shop number phone: ")
        return shop_phone


    #Product
    def show_products(self, product):
        if product:
            print("Products:")
            for p in product:
                print(f"id_product: {p[0]}, id_shop: {p[1]}, name_product: {p[2]}, price: {p[3]}")
        else:
            print("Not found")

    def get_product_input(self):
        shop_id = input("Input shop id: ")
        product_name = input("Input product name: ")
        product_price = input("Input product price: ")
        return shop_id, product_name, product_price

    def get_product_id(self):
        product_id = input("Input product id: ")
        return product_id

    #Order
    def show_orders(self, Order):
        if Order:
            print("Shops:")
            for o in Order:
                print(f"id_order: {o[0]}, id_user: {o[1]}, sum: {o[2]}, id_delivery: {o[3]}")
        else:
            print("No order found.")

    def get_num_product(self):
        num = input("Input number of products: ")
        return num

    def get_order_id(self):
        order_id = input("Input id order: ")
        return order_id

    # user
    def show_user(self, user):
        if user:
            print("Users:")
            for U in user:
                print(f"id: {U[0]}, name: {U[1]}, phone: {U[2]}")
        else:
                print("Not found")

    def get_user_input(self):
        name = input("Input name user: ")
        phone = input("Input phone user: ")
        return name, phone

    def get_user_id(self):
        user_id = input("Input user id: ")
        return user_id

    #Delivery
    def show_del(self, delivery):
        if delivery:
            print("Delivery:")
            for D in delivery:
                print(f"id: {D[0]}, time: {D[1]}, adress: {D[2]}")
        else:
                print("Not found")

    def get_del_input(self):
        time = input("Input time delivery: ")
        adress_del = input("Input adress delivery: ")
        return time, adress_del

    def get_del_id(self):
        id_del = input("Input delivery id: ")
        return id_del

    def gen_values(self):
        val = input("Input number of generated values: ")
        return val
