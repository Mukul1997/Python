import random
import string

def id_gen():
    p = ""
    q = ""
    id_gen_1 = string.ascii_letters
    id_gen_2 = string.digits

    for _ in range(5):
        p += random.choice(id_gen_1)
        q += random.choice(id_gen_2)
    return p+q

bill_id = id_gen()
cust_name = input("Enter name : ")
cust_id = id_gen()

if len(cust_name) < 3 or len(cust_name) > 20:
    print('Name error, Enter again')
    cust_name = input("Name : ")

print('-----------Retail World----------------')
print("Bill ID : ",bill_id)
print("Customer ID : ",cust_id)
print("Customer Name : ",cust_name)
