#29 may
#test1
cake_name = "Strawberry Cake"
cost = 40
selling_price = 75
profit = selling_price-cost
print ("สินค้า ", cake_name)
print ("กำไรต่อชิ้น ", profit)

#test2
cake_name = input("ป้อนชื่อเค้ก : ")
cost = int(input("ป้อนต้นทุน : "))
selling_price = int(input("ป้อนราคาขาย : "))
profit = selling_price-cost
print ("สินค้า ", cake_name)
print ("กำไรต่อชิ้น ", profit)

#test3
if profit < 0 :
    print ("ขาดทุน ควรพิจารณาราคาหรือต้นทุนใหม่")
elif profit == 0 :
    print ("เสมอตัว แนะนำให้เพิ่มมูลค่าสินค้า")
else:
    print ("ได้กำไร น่าลงทุนต่อ")

#test4
my_cake = ["Strawberry Cake", "chocolate cake", "Durian Cake","Mango Cake"]
cake_prices = (45, 45, 99, 85)
for cake in my_cake:
    print("เค้กสูตรพิเศษของเราวันนี้ คือ ", cake)

#test5
my_cake = ["Strawberry Cake", "chocolate cake", "Durian Cake","Mango Cake"]
cake_prices = (45, 45, 99, 85)
for cake, price in zip(my_cake, cake_prices):
    if price >= 80 :
        print ("เค้ก : ", cake , "ราคา : " , price ," บาท (สินค้า Premium)")
    else :
        print ("เค้ก : ", cake , "ราคา : " , price ," บาท (สินค้า Standard)")

#test6
def check_premium(price):
    if price >= 80:
        return "Premium"
    else :
        return "Standard"
print ("ผลการประเมินราคาสินค้า : ", check_premium(99))