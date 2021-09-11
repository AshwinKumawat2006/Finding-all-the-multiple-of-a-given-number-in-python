run = True

while run:
    number = int(input("Enter the number whoes multiple you want to know \n"))


    # here common difference is same as number
    def get_ap():
        divide_num_100 = 100 % number
        first_num = ((100 - divide_num_100) + number)
        divide_num_1000 = 1000 % number
        last_number = 1000 - divide_num_1000
        term = int(((last_number - first_num) / number) + 1)
        print(f"There are {term} numbers which are multiple of {number} between 100 and 1000")

        for i in range(term):
            print_term = (first_num + (i * (number)))
            i = 1 + i

            print(print_term)


    get_ap()


    repeat = input("Do you want to do it again (y/n) \n")

    if repeat == "y":
        print("")
    elif repeat == "n":
        print("COME AGAIN !!!")
        break
    else:
        print('               *********************  INVAID CHOICE ***********************')
        print('Try again later')
        break
