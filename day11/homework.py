#N1-შექმენით ფუნქცია რომელსაც გადაეცემა სამი პარამეტრი სამკუთხედის გვერდები და დაპრინტავს "ასეთი სამკუთხედი იარსებებს" ან დაპრინტავს "ასეთი სამკუთხედი ვერ იარსებებს"
#N2-შექმენით ფუნქცია რომელსაც გადაეცემა სამი სახელი და დაპრინტავს ამ სახელებიისგან სიას 3 პარამეტრი

#homework N2
# def names(saxeli_1,saxeli_2,saxeli_3):
#     list_names=[saxeli_1,saxeli_2,saxeli_3]
#     print(list_names)
    
# names(input("your name"),input("your name"),input("your name"))


# homework N1
def tolgverda_samkutxedi(gverdi_1,gverdi_2,gverdi_3):
    if gverdi_1==gverdi_2==gverdi_3:
        print("es samkutxedi tolgverdaa")
    else:
        print("es samkutxedi ar aris tolgverda")
tolgverda_samkutxedi(int(input("sheiyvanet samkutxedis 1 gverdis sigrdze :")),int(input("sheiyvanet samkutxedis 2 gverdis sigrdze :")),int(input("sheiyvanet samkutxedis 3 gverdis sigrdze :")))