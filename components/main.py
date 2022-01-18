# Script by Antonio Sànchez.
# If you liked the script pls give it an star

# Github: https://github.com/felxansl
# Stack OverFlow: https://es.stackoverflow.com/users/264900/antonio-s%c3%a1nchez
# Twitter: https://twitter.com/felxansl

# Text colors and stuff
class color:
   PURPLE = '\033[95m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   END = '\033[0m'
#========================#
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
    print(color.PURPLE + """
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
