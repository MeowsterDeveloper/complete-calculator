# Script by Félix Sánchez hi@snap.camel

# Github: https://github.com/snapcamel
# Twitter: https://twitter.com/snapcamel
# Instagram: https://instagram.com/snapcamel

# Text colors and stuff
class color:
   PURPLE = '\033[95m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   END = '\033[0m'

def calculatorWithDecimals():
    global n1, n2
    print(color.YELLOW + """        
     ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗████████╗███████╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗   
    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗  
    ██║     ██║   ██║██╔████╔██║██████╔╝██║     █████╗     ██║   █████╗█████╗██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝  
    ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██╔══╝╚════╝██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗  
    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ███████╗    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║  
     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝  
                                                                                                                                                              
                                                                                                ██████╗ ███████╗ ██████╗██╗███╗   ███╗ █████╗ ██╗     ███████╗
                                                                                                ██╔══██╗██╔════╝██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝
                                                                                                ██║  ██║█████╗  ██║     ██║██╔████╔██║███████║██║     ███████╗
                                                                                                ██║  ██║██╔══╝  ██║     ██║██║╚██╔╝██║██╔══██║██║     ╚════██║
                                                                                                ██████╔╝███████╗╚██████╗██║██║ ╚═╝ ██║██║  ██║███████╗███████║
                                                                                                ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝                                                                                                                                                                                                                                                                 
"""+ color.END)
    print(" ")
    pick = 0
    while True:
        n1 = input(color.PURPLE + " Type your first number (Decimals): "+ color.END)
        print(" ")
        n2 = input(color.PURPLE + " Type your second number (Decimals): "+ color.END)
        try:
            n1 = float(n1)
            n2 = float(n2)
        except:
            print(" ")
            print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " you typed an invalid argument pls use only float numbers."+ color.END)
            print(" ")
        else:
            break
    option = 0
    while True:
        print(color.YELLOW + """ 
        Chose an option for your numbers:

        1( Add.
        2( Multiply.
        3( Substract them.
        4( Divide.
        5( Change my numbers.
        6( Change my numbers (without decimals).
        7( Exit.
        """+ color.END)
        opt = 0
        while True:
            try:
                option = int(input(color.PURPLE + " Pick a number: " + color.END) )
            except:
                print(" ")
                print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " you typed an invalid argument pls use only float numbers."+ color.END)
                print(" ")
            else:
                break
        if option == 1:
            print(" ")
            print(color.GREEN + " The total of", n1, "+", n2, "is:", n1+n2)
        elif option == 2:
            print(" ")
            print(color.GREEN + " The total of", n1, "x", n2, "is:", n1*n2)
        elif option == 3:
            print(" ")
            print(color.GREEN + " The total of", n1, "-", n2, "is:", n1-n2)
        elif option == 4:
            print(" ")
            print(color.GREEN + " The total of", n1, "/", n2, "is:", n1/n2)
        elif option == 5:
            while True:
                n1 = input(color.PURPLE + " Type your first number (Decimals): "+ color.END)
                print(" ")
                n2 = input(color.PURPLE + " Type your second number (Decimals): "+ color.END)
                try:
                    n1 = float(n1)
                    n2 = float(n2)
                except:
                    print(" ")
                    print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " you typed an invalid argument pls use only numbers with decimals."+ color.END)
                    print(" ")
                else:
                    break
        elif option == 6:
            calculatorWithoutDecimals()
        elif option == 7:
            print(color.YELLOW + """ 
    ██████╗ ██╗   ██╗███████╗██╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║
    ██████╔╝ ╚████╔╝ █████╗  ██║
    ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
    ██████╔╝   ██║   ███████╗██╗
    ╚═════╝    ╚═╝   ╚══════╝╚═╝     
        """+ color.END)
        else:
            print(" ")
            print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " please introduce a list number:"+ color.END)

def calculatorWithoutDecimals():
    global n1, n2
    print(color.YELLOW + """ 
     ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗████████╗███████╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██║     ██║   ██║██╔████╔██║██████╔╝██║     █████╗     ██║   █████╗█████╗██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
    ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██╔══╝╚════╝██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ███████╗    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                            
                                                     ███╗   ██╗ ██████╗ ███╗   ██╗███████╗    ██████╗ ███████╗ ██████╗██╗███╗   ███╗ █████╗ ██╗     ███████╗ 
                                                     ████╗  ██║██╔═══██╗████╗  ██║██╔════╝    ██╔══██╗██╔════╝██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝ 
                                                     ██╔██╗ ██║██║   ██║██╔██╗ ██║█████╗      ██║  ██║█████╗  ██║     ██║██╔████╔██║███████║██║     ███████╗ 
                                                     ██║╚██╗██║██║   ██║██║╚██╗██║██╔══╝      ██║  ██║██╔══╝  ██║     ██║██║╚██╔╝██║██╔══██║██║     ╚════██║ 
                                                     ██║ ╚████║╚██████╔╝██║ ╚████║███████╗    ██████╔╝███████╗╚██████╗██║██║ ╚═╝ ██║██║  ██║███████╗███████║ 
                                                     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═════╝ ╚══════╝ ╚═════╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝                                                                                                                                                                                                                                                
"""+ color.END)
    print(" ")
    pick = 0
    while True:
        n1 = input(color.PURPLE + " Type your first number (None decimals): "+ color.END)
        print(" ")
        n2 = input(color.PURPLE + " Type your second number (None decimals): "+ color.END)
        try:
            n1 = int(n1)
            n2 = int(n2)
        except:
            print(" ")
            print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " you typed an invalid argument pls use only numbers without decimals."+ color.END)
            print(" ")
        else:
            break
    option = 0
    while True:    
        print(color.YELLOW + """ 
        Chose an option:

        1( Add.
        2( Multiply.
        3( Substract them.
        4( Divide.
        5( Change my current numbers (without decimals).
        6( Change my numbers to (with decimals).
        7( Exit.
        """ + color.END)
        opt = 0
        while True:
            option = input(color.PURPLE + " Pick a number: " + color.END)
            try:
                option = int(option)
            except:
                print(" ")
                print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " you typed an invalid argument pls use only numbers without decimals."+ color.END)
                print(" ")
            else:
                break
        if option == 1:
            print(" ")
            print(color.GREEN + " The total of", n1, "+", n2, "is:", n1+n2)
        elif option == 2:
            print(" ")
            print(color.GREEN + " The total of", n1, "x", n2, "is:", n1*n2)
        elif option == 3:
            print(" ")
            print(color.GREEN + " The total of", n1, "-", n2, "is:", n1-n2)
        elif option == 4:
            print(" ")
            print(color.GREEN + " The total of", n1, "/", n2, "is:", n1/n2)
        elif option == 5:
            while True:
                n1 = input(color.PURPLE + " Type your first number (None decimals): "+ color.END)
                print(" ")
                n2 = input(color.PURPLE + " Type your second number (None decimals): "+ color.END)
                try:
                    n1 = int(n1)
                    n2 = int(n2)
                except:
                    print(" ")
                    print(color.RED + "     ERROR:"+ color.END + color.YELLOW + " you typed an invalid argument pls use only numbers without decimals."+ color.END)
                    print(" ")
                else:
                    break
        elif option == 6:
            calculatorWithDecimals()
        elif option == 7:
            print(color.YELLOW + """ 
    ██████╗ ██╗   ██╗███████╗██╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║
    ██████╔╝ ╚████╔╝ █████╗  ██║
    ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
    ██████╔╝   ██║   ███████╗██╗
    ╚═════╝    ╚═╝   ╚══════╝╚═╝ 
            """+ color.END)
            exit()
        else:
            print(" ")
            print(color.RED + "     ERROR:" + color.END + color.YELLOW + " please introduce a list number:"+ color.END)