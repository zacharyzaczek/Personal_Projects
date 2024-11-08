#Brians 3D Printing Program
#Created by Best Friend, Zachary Zaczek 10/4/2024

def main():
    print(" _____ ____     ____                              _             ")
    print("|___ /|  _ \   / ___|___  _ ____   _____ _ __ ___(_) ___  _ __  ")
    print("  |_ \| | | | | |   / _ \| '_ \ \ / / _ \ '__/ __| |/ _ \| '_ \ ")
    print(" ___) | |_| | | |__| (_) | | | \ V /  __/ |  \__ \ | (_) | | | |")
    print("|____/|____/_  \____\___/|_| |_|\_/ \___|_|  |___/_|\___/|_| |_|")
    print(" / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __                  ")
    print("| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|                 ")
    print("| |__| (_| | | (__| |_| | | (_| | || (_) | |                    ")
    print(" \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|                    ")
    print(" ")
    #space


    def Brian():
         print("           _                                                       ")
         print("          ' )     )                                                ")
         print("          /'    /'                                                 ")
         print("       ,/'    /' ____      ____     ____                           ")
         print("      /`---,/' /'    )   /'    )--/'    )--/'    /                 ")
         print("    /'    /' /'    /'  /'    /' /'    /' /'    /'                  ")
         print("(,/'     (_,(___,/(__/(___,/' /(___,/'  (___,/(__                  ")
         print("                   /'       /'             /'                      ")
         print("                 /'       /'       /     /'                        ")
         print("               /'       /'        (___,/'                          ")
         print("              _                                                    ")
         print("            /' `\                  /'  /'             /'           ")
         print("          /'     )             --/'--/'             /'             ")
         print("        /' (___,/'O   ____     /'  /'__     _____,/' ____          ")
         print("      /'     )  /'  )'    )--/'  /'    )  /'    /' /'    )  /'    /")
         print("    /'      /'/'  /'       /'  /'    /' /'    /' /'    /' /'    /' ")
         print("(,/' (___,/' (__/'        (__/'    /(__(___,/(__(___,/(__(___,/(__ ")
         print("                                                            /'     ")
         print("                                                    /     /'       ")
         print("                                                   (___,/'         ")
         print("              _                                                    ")
         print("            /' `\                                      /'          ")
         print("          /'     )                                   /'            ")
         print("        /' (___,/'____     O  ____     ,____       /'              ")
         print("      /'     )  )'    )--/' /'    )   /'    )    /'                ")
         print("    /'      /'/'       /' /'    /'  /'    /'   /'                  ")
         print("(,/' (___,/'/'        (__(___,/(__/'    /(__ O                     ")

         print("From: Your Friend Zachary Zaczek")

    def InchesToMillimeter():
            print(" ")
            while True:
                print(" ")
                try:
                    InchInput = (input("Enter Inches: "))
                    if InchInput == 'exit':
                        exit()
                    if InchInput == 'm':
                        MillimeterToInches()
                    if InchInput != 'done':
                        FloatInchInput = (float(InchInput))
                        print("Total Number of Millimeters: ",FloatInchInput * 25.4)
                except ValueError:
                    pass
    

    def MillimeterToInches():
            print(" ")
            while True:
                print(" ")
                try:
                    MMInput = (input("Enter Millimeters: "))
                    if MMInput == 'exit':
                        exit()
                    if MMInput == 'i':
                        InchesToMillimeter()
                    if MMInput != 'done':
                        FloatMMInput = (float(MMInput))
                        print("Total Number of Inches: ",FloatMMInput / 25.4)
                except ValueError:
                    pass

    def Conversion():
            while input != 'exit':
                print(" ")
                print(" ")
                measurement = (input("Enter Unit of Length: "))
                if measurement == 'i':
                    InchesToMillimeter()
                if measurement == 'm':
                    MillimeterToInches()
                if measurement == 'exit':
                    exit()
                if measurement == 'Brian':
                    Brian()
                elif measurement != 'i' or 'm':
                    print("For Inches to Millimeters Type: 'i' \nFor Millimeters to Inches Type: 'm'")

    Conversion()

if __name__ == "__main__":
    main()