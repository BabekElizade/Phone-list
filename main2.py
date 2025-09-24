phone = {
    "new_sum":"SUMMA",
    "old_sum":"SUMMA1",
    "phone name":"NAME",
    "year": "YEAR"
}



with open("C:\\Users\\orkha\\Downloads\\Phones_data_comma.csv", "r") as excel_file:
    file = excel_file.read().split(";")

operation = input("Choose operation: ").upper()

#-------------------------------------------------------------------------------------------------------

if operation == phone["new_sum"]:
    say = int(input("Enter Number: "))
    summa = []
    i = 13
    while i <= say and i < len(file):
        summa.append(file[i])
        i += 15

    summa_copy = [float(x.replace(",", ".")) for x in summa]

    cem = sum(summa_copy)
    print("Summa:", cem)

#-----------------------------------------------------------------------------------------------------    

if operation == phone["old_sum"]:
    say1 = int(input("Enter Number: "))
    summa1 = []
    i = 14
    while i <= say1 and i < len(file):
        summa1.append(file[i])
        i += 15

    summa_copy1 = [float(x1.replace(",", ".")) for x1 in summa1]

    cem1 = sum(summa_copy1)
    print("Summa:", cem1)
    
#-----------------------------------------------------------------------------------------------------

if operation == phone["year"]:
    say2 = int(input("Enter Number:"))
    year_list = []
    phone_list = []
    son1 = []
    i = 11
    i_1 = 0
    p = 0
    while i < say2:
        year_list.append(file[i])
        i += 15
    while i_1 < say2:
        phone_list.append(file[i_1])
        i_1 += 15
        cleaned_phones = [element.strip() for element in phone_list]
        son = "{phone_name}: ".format(phone_name = cleaned_phones[p]), year_list[p]
        son1.append(son)
        if (say2//16) > p:
            p += 1
    print(son1)
    
#----------------------------------------------------------------------------------------------------


        
