while True:
    try:
        number = input("Write a number to check if it is Armstrong Number: ")
        int_number = int(number)
        len_number = len(number)
        total = 0
        for i in number:
            total += int(i)**len(number)

        if total == int(number):
            print(f"{number} is an Armstrong Number.")
        else:
            print(f"{number} is not an Armstrong Number.")
        break
    except:
        print("You wrote an invalid value, please write a valid value!")
        
