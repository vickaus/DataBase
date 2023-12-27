import psycopg2
import random
import string
class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='lab1',
            user='postgres',
            password='0000',
            host='localhost',
            port=5432
        )
        
    def gen_shop(self, val):
        c = self.conn.cursor()
        val = int(val)
        for i in range(val):
            name_shop = ''.join(random.choices(string.ascii_letters, k=6))
            phone_shop = ''.join(random.choices(string.digits, k=8))
            c.execute('INSERT INTO "Shop" ("name_shop", "phone_shop") VALUES (%s, %s)',(name_shop, phone_shop))
        self.conn.commit()
        print("Value in Shop is generated!")

    # Shop
    def add_shop(self, shop_name, shop_phone):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Shop" ("name_shop", "phone_shop") VALUES (%s, %s)', (shop_name, shop_phone))
        self.conn.commit()
        print("Shop added successfully!")

    def editing_shop(self, shop_id, shop_name, shop_phone):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Shop" WHERE "id_shop" = %s', (shop_id,))
        check1 = c.fetchall()
        if check1:
            c.execute('UPDATE "Shop" SET "name_shop"=%s, "phone_shop"=%s WHERE "id_shop"=%s ', (shop_name, shop_phone, shop_id))
            self.conn.commit()
            print("Shop edited successfully!")
        else:
            print("Error! Can't find shop with this id")

    def delete_shop(self, shop_id):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Shop" WHERE "id_shop" = %s', (shop_id,))
        check1 = c.fetchall()
        c.execute('SELECT * FROM "Product" WHERE "id_shop" = %s', (shop_id,))
        check2 = c.fetchall()
        if check1 and check2:
            c.execute('SELECT "id_product" FROM "Product" WHERE "id_shop" = %s', (shop_id,))
            n = c.fetchall()
            c.execute('DELETE FROM "Order_Product" WHERE "id_product"= %s', (n[0],))
            self.conn.commit()
            c.execute('DELETE FROM "Product" WHERE "id_shop"=%s', (shop_id,))
            self.conn.commit()
            c.execute('DELETE FROM "Shop" WHERE "id_shop"=%s', (shop_id,))
            self.conn.commit()
            print("Catalog deleted successfully!")
        elif check1:
            c.execute('DELETE FROM "Shop" WHERE "id_shop"=%s', (shop_id,))
            self.conn.commit()
            print("Shop deleted successfully!")
        else:
            print("Error! This id_shop not exist")

    def get_all_shops(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Shop"')
        return c.fetchall()


    #Product
    def add_product(self, id_shop, name_product, price):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Shop" WHERE "id_shop" = %s', (id_shop,))
        check1 = c.fetchall()
        if check1:
             c.execute('INSERT INTO "Product" ("id_shop", "name_product", "price") VALUES (%s, %s, %s)',( id_shop, name_product, price))
             self.conn.commit()
             print("Product added successfully!")
        else:
             print("Error! This identifier id_shop exists")

    def editing_product(self, id_product, id_shop, name_product, price):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Product" WHERE "id_product" = %s', (id_product,))
        check = c.fetchall()
        if check:
            c.execute('UPDATE "Product" SET "id_shop"=%s, "name_product"=%s, "price"=%s WHERE "id_product"=%s',(id_shop, name_product, price, id_product))
            self.conn.commit()
            print("Product edited successfully!")
        else:
            print("Error! Can't find product with this id")

    def delete_product(self, id_product):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Product" WHERE "id_product" = %s', (id_product,))
        check1 = c.fetchall()
        c.execute('SELECT * FROM "Product" WHERE "id_product" = %s', (id_product,))
        check2 = c.fetchall()
        if check1 and check2:
            c.execute('DELETE FROM "Order_Product" WHERE "id_product"=%s', (id_product,))
            self.conn.commit()
            c.execute('DELETE FROM "Product" WHERE "id_product"=%s', (id_product,))
            self.conn.commit()
            print("Product deleted successfully!")
        elif check1:
            c.execute('DELETE FROM "Product" WHERE "id_product"=%s', (id_product,))
            self.conn.commit()
            print("Product deleted successfully!")
        else:
            print("Error! This id_product not exist")

    def get_all_products(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Product"')
        return c.fetchall()


    # Order
    def add_order(self, id_user, matrix_product_id, num_product, id_del):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "User" WHERE "id_user" = %s', (id_user,))
        user = c.fetchall()
        if user:
            summ = 0
            for k in range(int(num_product)):
                c.execute('SELECT * FROM "Product" WHERE "id_product"=%s', ( matrix_product_id[k]))
                value = c.fetchone()[0]
                summ = summ + value
            c.execute('INSERT INTO "Order" ("id_user", "sum", "id_delivery") VALUES (%s, %s, %s) RETURNING "id_order"', (id_user, summ, id_del))
            order_id = c.fetchone()[0]
            for m in range(int(num_product)):
                c.execute('INSERT INTO "Order_Product" ("id_order", "id_product") VALUES (%s, %s)', (order_id, matrix_product_id[m]))
            self.conn.commit()
            print("Order added successfully!")
        else:
            print("Error. not found user")

    def editing_order(self, matrix_product_id, num_product, order_id, user_id, id_del):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Order" WHERE "id_order" = %s', (order_id,))
        check = c.fetchall()
        if check:
            sum = 0
            for k in range(int(num_product)):
                c.execute('SELECT * FROM "Product" WHERE "id_product"=%s', (matrix_product_id[k]))
                value = c.fetchone()[0]
                sum = sum + value
            c.execute('UPDATE "Order" SET ("id_user"=%s, "sum"=%s, "id_delivery"=%s) WHERE "id_order"=%s', (user_id, sum, id_del, order_id))
            self.conn.commit()
            c.execute('DELETE FROM "Order_Product" WHERE "id_order"=%s', (order_id,))
            self.conn.commit()
            for m in range(int(num_product)):
                c.execute('INSERT INTO "Order_product" ("id_order", "id_product") VALUES (%s, %s)',(order_id, matrix_product_id[m]))
                self.conn.commit()
            print("Order edited successfully!")
        else:
            print("Error! This id_order not exist")

    def delete_order(self, id_order):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Order" WHERE "id_order" = %s', (id_order,))
        check1 = c.fetchall()
        c.execute('SELECT * FROM "Order_Product" WHERE "id_order" = %s', (id_order,))
        check2 = c.fetchall()
        if check1 and check2:
            c.execute('DELETE FROM "Order_Product" WHERE "id_order"=%s', (id_order,))
            self.conn.commit()
            c.execute('DELETE FROM "Order" WHERE "id_order"=%s', (id_order,))
            self.conn.commit()
            print("Order deleted successfully!")
        elif check1:
            c.execute('DELETE FROM "Order" WHERE "id_order"=%s', (id_order,))
            self.conn.commit()
            print("Order deleted successfully!")
        else:
            print("Error! This id_order not exist")

    def get_all_order(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Order"')
        return c.fetchall()

    # User
    def add_user(self, name, phone):
        c = self.conn.cursor()
        c.execute('INSERT INTO "User" ("name_user", "phone_user") VALUES (%s, %s)', (name, phone))
        self.conn.commit()
        print("User added successfully!")

    def get_all_user(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "User"')
        return c.fetchall()

    def editing_user(self, id_user, name, phone):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "User" WHERE "id_user" = %s', (id_user,))
        check = c.fetchall()
        if check:
            c.execute('UPDATE "User" SET "name_user"=%s, "phone_user"=%s WHERE "id_user"=%s', (name, phone, id_user))
            self.conn.commit()
            print("User edited successfully!")
        else:
            print("Error! This id_user not exist")

    def delete_user(self, id_user):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "User" WHERE "id_user" = %s', (id_user,))
        check1 = c.fetchall()
        if check1:
            c.execute('SELECT "id_order" FROM "Order" WHERE "id_user"=%s', (id_user,))
            order_ids = c.fetchall()
            for order_id in order_ids:
                c.execute('DELETE FROM "Order_Product" WHERE "id_order"=%s', (order_id[0],))
                self.conn.commit()
            c.execute('DELETE FROM "Order" WHERE "id_user"=%s', (id_user,))
            self.conn.commit()
            c.execute('DELETE FROM "User" WHERE "id_user"=%s', (id_user,))
            self.conn.commit()
            print("User deleted successfully!")
        else:
            print("Error! This id_user does not exist")

    # Delivery
    def add_del(self, time_del, adress_del):
        c = self.conn.cursor()
        c.execute('INSERT INTO "Delivery" ("time", "adress") VALUES (%s, %s)', (time_del, adress_del))
        self.conn.commit()
        print("Delivery added successfully!")

    def get_all_delivery(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Delivery"')
        return c.fetchall()

    def editing_del(self, id_del, time, adress):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Delivery" WHERE "id_delivery" = %s', (id_del,))
        check1 = c.fetchall()
        if check1:
            c.execute('UPDATE "Delivery" SET "time"=%s, "adress"=%s WHERE "id_delivery"=%s', (time, adress, id_del))
            self.conn.commit()
            print("Delivery deleted successfully!")
        else:
            print("Error! This id_delivery does not exist")

    def delete_del(self, id_del):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Delivery" WHERE "id_delivery" = %s', (id_del,))
        check1 = c.fetchall()
        if check1:
            c.execute('SELECT "id_order" FROM "Order" WHERE "id_delivery"=%s', (id_del,))
            order_ids = c.fetchall()
            for order_id in order_ids:
                c.execute('DELETE FROM "Order_Product" WHERE "id_order"=%s', (order_id[0],))
            c.execute('DELETE FROM "Order" WHERE "id_delivery"=%s', (id_del,))
            c.execute('DELETE FROM "Delivery" WHERE "id_delivery"=%s', (id_del,))
            self.conn.commit()
            print("Delivery deleted successfully!")
        else:
            print("Error! This id_delivery does not exist")
