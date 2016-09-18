import Math

class Calcu_Later:

    def __init__(self):
        pass

    def selection(self):

        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Modulus")
        print("5. Multiplication")
        print("6. Quit")
        choice = input("[> ]")

        int1 = int(input('First Number: '))
        int2 = int(input('Second Number: '))

        try:
            if int(choice) > 0 and int(choice) < 7:

                if choice != "6":
                    print("")
                    print("What two numbers do you want to Math with?")
                    count = input("> ")
        except:
            pass

        if choice == '1':
               sum = (num1,"+",num2,"=", addition(num1,num2))
               print(sum)

        if choice == '2':
               sum = (num1,"-",num2,"=", subtraction(num1,num2))
               print(sum)

        if choice == '3':
               sum = (num1,"/",num2,"=", division(num1,num2))
               print(sum)

        if choice == '4':
               sum = (num1,"%",num2,"=", modulus(num1,num2))
               print(sum)

        if choice == '5':
               sum = (num1,"*",num2,"=", multiplication(num1,num2))
               print(sum)

        if choice == '6':
               print("Good day to you sir/madam.")
               raise SystemExit()



	def addition(self):
        add(j, g)


        return j + g




if __name__ == "__main__":
  menu = Calcu_Later()
  menu.selection()

