# Script by Félix Sánchez hi@snap.camel

# Github: https://github.com/snapcamel
# Twitter: https://twitter.com/snapcamel
# Instagram: https://instagram.com/snapcamel

# Text colors and stuff
class color:
   PURPLE = '\033[95m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   END = '\033[0m'

print(" ")
print(color.YELLOW + """ 
     ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗████████╗███████╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██║     ██║   ██║██╔████╔██║██████╔╝██║     █████╗     ██║   █████╗█████╗██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
    ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██╔══╝╚════╝██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ███████╗    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                            
                                                                                                                        ███╗   ███╗███████╗███╗   ██╗██╗   ██╗  
                                                                                                                        ████╗ ████║██╔════╝████╗  ██║██║   ██║  
                                                                                                                        ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║  
                                                                                                                        ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║  
                                                                                                                        ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝  
                                                                                                                        ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝                                                                                                                                                                                              
"""+ color.END)
pick = 0
while True:
    print(" ")
    print(color.YELLOW + """
   Select a mode

  d(  Decimals
  n(  None Decimals
    """ + color.END)
    elec = str(input(color.PURPLE + " Chose a mode: "+ color.END) )
    print(" ")
    if elec == 'd':
        import _init_
        _init_.calculatorWithDecimals()
    elif elec == 'n':
        import _init_
        _init_.calculatorWithoutDecimals()
    else:
        print(" ")
        print(color.RED + "     ERROR:"+ color.END + color.YELLOW +" you typed an invalid argument type yes or no."+ color.END)
        continue
