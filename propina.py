num = int(input("Digite el total de la cuenta :"))
if num <= 60:
    print ("Aporte :", num)
    print("Tiene 18% de propina")
    print(num + (num*0.18))
    if num > 60 and num < 120 :
        print("Aporte :" , num)
        print(" Tiene 20% de pripina")
        print(num + (num*0.20))
    else  :
            print("Aporte :" , num)
            print("Tiene 25% de propina")
            print(num + (num*0.25))