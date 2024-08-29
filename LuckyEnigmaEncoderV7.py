#LuckyEnigmaEncoderV7
from sys import exit
def calc_total_num(Num1, Num2, Num3, Num4, Num5):
    return (Num1 , Num2 , Num3 , Num4 , Num5)

def total_do_math(Num1, Num2, Num3, Num4, Num5, math_operand):
    return eval(f"{Num1} {math_operand} {Num2} {math_operand} {Num3} {math_operand} {Num4} {math_operand} {Num5}")

def num_do_stuff1(Num1, Num2, Num3, Num4, Num5, math_opperand):

    Num1_Num1_Do_Stuff = eval(f"{Num1} {math_opperand} {Num1}")
    Num1_Num2_Do_Stuff = eval(f"{Num1} {math_opperand} {Num2}")
    Num1_Num3_Do_Stuff = eval(f"{Num1} {math_opperand} {Num3}")
    Num1_Num4_Do_Stuff = eval(f"{Num1} {math_opperand} {Num4}")
    Num1_Num5_Do_Stuff = eval(f"{Num1} {math_opperand} {Num5}")
    return Num1_Num1_Do_Stuff , Num1_Num2_Do_Stuff , Num1_Num3_Do_Stuff , Num1_Num4_Do_Stuff , Num1_Num5_Do_Stuff

def num_do_stuff2(Num1, Num2, Num3, Num4, Num5, math_opperand):

    Num2_Num1_Do_Stuff = eval(f"{Num2} {math_opperand} {Num1}")
    Num2_Num2_Do_Stuff = eval(f"{Num2} {math_opperand} {Num2}")
    Num2_Num3_Do_Stuff = eval(f"{Num2} {math_opperand} {Num3}")
    Num2_Num4_Do_Stuff = eval(f"{Num2} {math_opperand} {Num4}")
    Num2_Num5_Do_Stuff = eval(f"{Num2} {math_opperand} {Num5}")
    return Num2_Num1_Do_Stuff , Num2_Num2_Do_Stuff , Num2_Num3_Do_Stuff , Num2_Num4_Do_Stuff , Num2_Num5_Do_Stuff

def num_do_stuff3(Num1, Num2, Num3, Num4, Num5, math_opperand):

    Num3_Num1_Do_Stuff = eval(f"{Num3} {math_opperand} {Num1}")
    Num3_Num2_Do_Stuff = eval(f"{Num3} {math_opperand} {Num2}")
    Num3_Num3_Do_Stuff = eval(f"{Num3} {math_opperand} {Num3}")
    Num3_Num4_Do_Stuff = eval(f"{Num3} {math_opperand} {Num4}")
    Num3_Num5_Do_Stuff = eval(f"{Num3} {math_opperand} {Num5}")
    return Num3_Num1_Do_Stuff , Num3_Num2_Do_Stuff , Num3_Num3_Do_Stuff , Num3_Num4_Do_Stuff , Num3_Num5_Do_Stuff

def num_do_stuff4(Num1, Num2, Num3, Num4, Num5, math_opperand):

    Num4_Num1_Do_Stuff = eval(f"{Num4} {math_opperand} {Num1}")
    Num4_Num2_Do_Stuff = eval(f"{Num4} {math_opperand} {Num2}")
    Num4_Num3_Do_Stuff = eval(f"{Num4} {math_opperand} {Num3}")
    Num4_Num4_Do_Stuff = eval(f"{Num4} {math_opperand} {Num4}")
    Num4_Num5_Do_Stuff = eval(f"{Num4} {math_opperand} {Num5}")
    return Num4_Num1_Do_Stuff , Num4_Num2_Do_Stuff , Num4_Num3_Do_Stuff , Num4_Num4_Do_Stuff , Num4_Num5_Do_Stuff

def num_do_stuff5(Num1, Num2, Num3, Num4, Num5, math_opperand):

    Num5_Num1_Do_Stuff = eval(f"{Num5} {math_opperand} {Num1}")
    Num5_Num2_Do_Stuff = eval(f"{Num5} {math_opperand} {Num2}")
    Num5_Num3_Do_Stuff = eval(f"{Num5} {math_opperand} {Num3}")
    Num5_Num4_Do_Stuff = eval(f"{Num5} {math_opperand} {Num4}")
    Num5_Num5_Do_Stuff = eval(f"{Num5} {math_opperand} {Num5}")
    return Num5_Num1_Do_Stuff , Num5_Num2_Do_Stuff , Num5_Num3_Do_Stuff , Num5_Num4_Do_Stuff , Num5_Num5_Do_Stuff

def get_int(prompt):
    #This part of the program allows the user to enter 5 intigers
    while True:
        try:
            Num = (int(input(prompt)))
            return Num
        except ValueError:
            print("Invalid integer!")

def is_correct_msg(Secret_Message):
    print("Your Secret Message Says: "+Secret_Message)
    print("Is this correct?")
    Secret_Message_Yes_No = input("yes or no: ")
    if Secret_Message_Yes_No == 'yes':
        return True
    if Secret_Message_Yes_No != 'yes':
        return False
    
def is_correct_msg(Code_Word):
    print("Your Code Word Says: "+Code_Word)
    print("Is this correct?")
    Secret_Message_Yes_No = input("yes or no: ")
    if Secret_Message_Yes_No == 'yes':
        return True
    if Secret_Message_Yes_No != 'yes':
        return False
    
def getsecret_message():
    #This is the first step of the program
    #This is where the user enters their secret message

    while True:
        Secret_Message = input("Enter Your Secret Message: ")
        true_false = is_correct_msg(Secret_Message)
        if true_false == False:
            continue
        else:
            return Secret_Message

def welcome_msg():
    print("Hello and welcome to Lucky Enigma Encoder!")
    print("This program is written to encript data before being sent over the wire.")
    print(" ")

def getcode_word():
    #This part of the program is used to get the users code word

    while True:
        Code_Word = input("Enter Your Code Word: ")
        true_false = is_correct_msg(Code_Word)
        if true_false == False:
            continue
        else:
            return Code_Word
        

def main():
    welcome_msg()

    Secret_Message = getsecret_message()

    Num1 = get_int("Enter your First integer: ")
    Num2 = get_int("Enter your Second integer: ")
    Num3 = get_int("Enter your Third integer: ")
    Num4 = get_int("Enter your Forth integer: ")
    Num5 = get_int("Enter your Fifth integer: ")

    Code_Word = getcode_word()

    TotalNum = (Num1, Num2, Num3, Num4, Num5)

    TotalNumAdd = total_do_math(Num1, Num2, Num3, Num4, Num5, "+") #Finds the total of all Numbers Added
    TotalNumSub = total_do_math(Num1, Num2, Num3, Num4, Num5, "-") #Finds the total of all Numbers Subtracted
    TotalNumMult = total_do_math(Num1, Num2, Num3, Num4, Num5, "*") #Finds the total of all Numbers Multiplied
    TotalNumDivi = total_do_math(Num1, Num2, Num3, Num4, Num5, "/") #Finds the total of all Numbers Divided

    Num1_Add_List = [Num1_Num1_Add, Num1_Num2_Add, Num1_Num3_Add, Num1_Num4_Add, Num1_Num5_Add] = num_do_stuff1(Num1, Num2, Num3, Num4, Num5, "+")
    Num1_Sub_List = [Num1_Num1_Sub, Num1_Num2_Sub, Num1_Num3_Sub, Num1_Num4_Sub, Num1_Num5_Sub] = num_do_stuff1(Num1, Num2, Num3, Num4, Num5, "-")
    Num1_Mult_List = [Num1_Num1_Mult, Num1_Num2_Mult, Num1_Num3_Mult, Num1_Num4_Mult, Num1_Num5_Mult] = num_do_stuff1(Num1, Num2, Num3, Num4, Num5, "*")
    Num1_Div_List = [Num1_Num1_Div, Num1_Num2_Div, Num1_Num3_Div, Num1_Num4_Div, Num1_Num5_Div] = num_do_stuff1(Num1, Num2, Num3, Num4, Num5, "/")

    Num2_Add_List = [Num2_Num1_Add, Num2_Num2_Add, Num2_Num3_Add, Num2_Num4_Add, Num2_Num5_Add] = num_do_stuff2(Num1, Num2, Num3, Num4, Num5, "+")
    Num2_Sub_List = [Num2_Num1_Sub, Num2_Num2_Sub, Num2_Num3_Sub, Num2_Num4_Sub, Num2_Num5_Sub] = num_do_stuff2(Num1, Num2, Num3, Num4, Num5, "-")
    Num2_Mult_List = [Num2_Num1_Mult, Num2_Num2_Mult, Num2_Num3_Mult, Num2_Num4_Mult, Num2_Num5_Mult] = num_do_stuff2(Num1, Num2, Num3, Num4, Num5, "*")
    Num2_Div_List = [Num2_Num1_Div, Num2_Num2_Div, Num2_Num3_Div, Num2_Num4_Div, Num2_Num5_Div] = num_do_stuff2(Num1, Num2, Num3, Num4, Num5, "/")

    Num3_Add_List = [Num3_Num1_Add, Num3_Num2_Add, Num3_Num3_Add, Num3_Num4_Add, Num3_Num5_Add] = num_do_stuff3(Num1, Num2, Num3, Num4, Num5, "+")
    Num3_Sub_List = [Num3_Num1_Sub, Num3_Num2_Sub, Num3_Num3_Sub, Num3_Num4_Sub, Num3_Num5_Sub] = num_do_stuff3(Num1, Num2, Num3, Num4, Num5, "-")
    Num3_Mult_List = [Num3_Num1_Mult, Num3_Num2_Mult, Num3_Num3_Mult, Num3_Num4_Mult, Num3_Numb5_Mult] = num_do_stuff3(Num1, Num2, Num3, Num4, Num5, "*")
    Num3_Div_List = [Num3_Num1_Div, Num3_Num2_Div, Num3_Num3_Div, Num3_Num4_Div, Num3_Num5_Div] = num_do_stuff3(Num1, Num2, Num3, Num4, Num5, "/")

    Num4_Add_List = [Num4_Num1_Add, Num4_Num2_Add, Num4_Num3_Add, Num4_Num4_Add, Num4_Num5_Add] = num_do_stuff4(Num1, Num2, Num3, Num4, Num5, "+")
    Num4_Sub_List = [Num4_Num1_Sub, Num4_Num2_Sub, Num4_Num3_Sub, Num4_Num4_Sub, Num4_Num5_Sub] = num_do_stuff4(Num1, Num2, Num3, Num4, Num5, "-")
    Num4_Mult_List = [Num4_Num1_Mult, Num4_Num2_Mult, Num4_Num3_Mult, Num4_Num4_Mult, Num4_Num5_Mult] = num_do_stuff4(Num1, Num2, Num3, Num4, Num5, "*")
    Num4_Div_List = [Num4_Num1_Div, Num4_Num2_Div, Num4_Num3_Div, Num4_Num4_Div, Num4_Num5_Div] = num_do_stuff4(Num1, Num2, Num3, Num4, Num5, "/")

    Num5_Add_List = [Num5_Num1_Add, Num5_Num2_Add, Num5_3_Add, Num5_Num4_Add, Num5_Num5_Add] = num_do_stuff5(Num1, Num2, Num3, Num4, Num5, "+")
    Num5_Sub_List = [Num5_Num1_Sub, Num5_Num2_Sub, Num__Num3_Sub, Num4_Num4_Sub, Num5_Num5_Sub] = num_do_stuff5(Num1, Num2, Num3, Num4, Num5, "-")
    Num5_Mult_List = [Num5_Num1_Mult, Num5_Num2_Mult, Num5_Num3_Mult, Num5_Num4_Mult, Num5_Num5_Mult] = num_do_stuff5(Num1, Num2, Num3, Num4, Num5, "*")
    Num5_Div_List = [Num5_Num1_Div, Num5_Num2_Div, Num5_Num3_Div, Num5_Num4_Div, Num5_Num5_Div] = num_do_stuff5(Num1,Num2, Num3, Num4, Num5, "/")

    print(" ")#Space
    
    #Calculates a list of all number lists
    Num1_Calc_List = (Num1_Add_List + Num1_Sub_List + Num1_Mult_List + Num1_Div_List)
    Num2_Calc_List = (Num2_Add_List + Num2_Sub_List + Num2_Mult_List + Num2_Div_List)
    Num3_Calc_List = (Num3_Add_List + Num3_Sub_List + Num3_Mult_List + Num3_Div_List)
    Num4_Calc_List = (Num4_Add_List + Num4_Sub_List + Num4_Mult_List + Num4_Div_List)
    Num5_Calc_List = (Num5_Add_List + Num5_Sub_List + Num5_Mult_List + Num5_Div_List)

    Total_Calc_List = (Num1_Calc_List + Num2_Calc_List + Num3_Calc_List + Num4_Calc_List + Num5_Calc_List)
    Total_Calc_List_Length = len(Total_Calc_List)

    #This part of the program is used to perform calculations on the code word. 

    #Setting Number Values to 0
    AA = 0
    aa = 0
    BB = 0
    bb = 0
    CC = 0
    cc = 0
    DD = 0
    dd = 0
    EE = 0
    ee = 0
    FF = 0
    ff = 0
    GG = 0
    gg = 0
    HH = 0
    hh = 0
    II = 0
    ii = 0
    JJ = 0
    jj = 0
    KK = 0
    kk = 0
    LL = 0
    ll = 0
    MM = 0
    mm = 0
    NN = 0
    nn = 0
    OO = 0
    oo = 0
    PP = 0
    pp = 0
    QQ = 0
    qq = 0
    RR = 0
    rr = 0
    SS = 0
    ss = 0
    TT = 0
    tt = 0
    UU = 0
    uu = 0
    VV = 0
    vv = 0
    WW = 0
    ww = 0
    XX = 0 
    xx = 0
    YY = 0
    yy = 0
    ZZ = 0
    zz = 0

    for i in Code_Word:
        if i == "A":
            AA += 52
        if i == "a":
            aa += 51
        if i == "B":
            BB += 50
        if i == "b":
            bb += 49
        if i == "C":
            CC += 48
        if i == "c":
            cc += 47
        if i == "D":
            DD += 46
        if i == "d":
            dd += 45
        if i == "E":
            EE += 44
        if i == "e":
            ee += 43
        if i == "F":
            FF += 42
        if i == "f":
            ff += 41
        if i == "G":
            GG += 40
        if i == "g":
            gg += 39
        if i == "H":
            HH += 38
        if i == "h":
            hh += 37
        if i == "I":
            II += 36
        if i == "i":
            ii += 35
        if i == "J":
            JJ += 34
        if i == "j":
            jj += 33
        if i == "K":
            KK += 32
        if i == "k":
            kk += 31
        if i == "L":
            LL += 30
        if i == "l":
            ll += 29
        if i == "M":
            MM += 28
        if i == "m":
            mm += 27
        if i == "N":
            NN += 26
        if i == "n":
            nn += 25
        if i == "O":
            OO += 24
        if i == "o":
            oo += 23
        if i == "P":
            PP += 22
        if i == "p":
            pp += 21
        if i == "Q":
            QQ += 20
        if i == "q":
            qq += 19
        if i == "R":
            RR += 18
        if i == "r":
            rr += 17
        if i == "S":
            SS = 16
        if i == "s":
            ss += 15
        if i == "T":
            TT += 14
        if i == "t":
            tt += 13
        if i == "U":
            UU += 12
        if i == "u":
            uu += 11
        if i == "V":
            VV += 10
        if i == "v":
            vv += 9
        if i == "W":
            WW += 8
        if i == "w":
            ww += 7
        if i == "X":
            XX += 6
        if i == "x":
            xx += 5
        if i == "Y":
            YY += 4
        if i == "y":
            yy += 3
        if i == "Z":
            ZZ += 2
        if i == "z":
            zz += 1

    #This part of the program calculates Aa, Bb, Cc, Dd, Ee, Ff, Gg, Hh, Ii, Jj, Kk, Ll, Mm, Nn, Oo, Pp, Qq, Rr, Ss, Tt, Uu, Vv, Ww, Xx, Yy, Zz
    
    a1 = 0
    b1 = 0
    c1 = 0
    d1 = 0
    e1 = 0
    f1 = 0
    g1 = 0
    h1 = 0
    i1 = 0
    j1 = 0
    k1 = 0
    l1 = 0
    m1 = 0
    n1 = 0
    o1 = 0
    p1 = 0
    q1 = 0
    r1 = 0
    s1 = 0
    t1 = 0
    u1 = 0
    v1 = 0
    w1 = 0
    x1 = 0
    y1 = 0
    z1 = 0
            
    for i in Code_Word:
        if i == "A" or i == "a":
            a1 += 1
        if i == "B" or i == "b":
            b1 += 2
        if i == "C" or i == "c":
            c1 += 3
        if i == "D" or i == "d":
            d1 += 4
        if i == "E" or i == "e":
            e1 += 5
        if i == "F" or i == "f":
            f1 += 6
        if i == "G" or i == "g":
            g1 += 7
        if i == "H" or i == "h":
            h1 += 8
        if i == "I" or i == "i":
            i1 += 9
        if i == "J" or i == "j":
            j1 += 10
        if i == "K" or i == "k":
            k1 += 11
        if i == "L" or i == "l":
            l1 += 12
        if i == "M" or i == "m":
            m1 += 13
        if i == "N" or i == "n":
            n1 += 14
        if i == "O" or i == "o":
            o1 += 15
        if i == "P" or i == "p":
            p1 += 16
        if i == "Q" or i == "q":
            q1 += 17
        if i == "R" or i == "r":
            r1 += 18
        if i == "S" or i == "s":
            s1 += 19
        if i == "T" or i == "t":
            t1 += 20
        if i == "U" or i == "u":
            u1 += 21
        if i == "V" or i == "v":
            v1 += 22
        if i == "W" or i == "w":
            w1 += 23
        if i == "X" or i == "x":
            x1 += 24
        if i == "Y" or i == "y":
            y1 += 25
        if i == "Z" or i == "z":
            z1 += 26
    
    #Shows a list for CWD_EC and CWD_EL

    CWD_EC = [AA, aa, BB, bb, CC, cc, DD, dd, EE, ee, FF, ff, GG, gg, HH, hh, II, ii, JJ, jj, KK, kk, LL, ll, MM, mm, NN, nn, OO, oo, PP, pp, QQ, qq, RR, rr, SS, ss, TT, tt, UU, uu, VV, vv, WW, ww, XX, xx, YY, yy, ZZ, zz]
    print(" ")
    CWD_EL = [a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1, q1, r1, s1, t1, u1, v1, w1, x1, y1, z1]
    
    SML = list(Secret_Message)
    print("Secret Message List: ",SML)
    print(" ")

    CWL = list(Code_Word)
    print("Code Word List: ",CWL)
    print(" ")
    #Turns the String and Code word into a list
    print("Code Word Upper Lower Number List: ",CWD_EC)
    print("Code Word Number List: ",CWD_EL)
    print(" ")
    CWD_EDL = []
    for i in CWD_EC:
        if i > 0:
            CWD_EDL += [i] 
    print("Code Word A&a Number List: ",CWD_EDL)
    print(" ")
    CWD_ELL = []
    for i in CWD_EL:
        if i > 0:
            CWD_ELL += [i]
    print("Code Word AA Number List: ", CWD_ELL)
    print(" ")
        
    #Prints the calculations for numbers
    #Variables are N1CL, N2CL, N3CL, N4CL, and N5CL
    TNL = list(TotalNum)
    print("List of numbers: ", TNL)
    print(" ")

    N1CL = list(Num1_Calc_List)
    N2CL = list(Num2_Calc_List)
    N3CL = list(Num3_Calc_List)
    N4CL = list(Num4_Calc_List)
    N5CL = list(Num5_Calc_List)

    print("Num1 calculations: ", N1CL)
    print("Num2 calculations: ", N2CL)
    print("Num3 calculations: ", N3CL)
    print("Num4 calculations: ", N4CL)
    print("Num5 calculations: ", N5CL)
    print(" ")

    #This part of the program is written to manipulte Num1, Num2, Num3, Num4, and Num5 calculations with the Code_Word calculations.
        #Variables are CWD_EDL and CWD_ELL
    #This step involves Add, Sub, Mult, and Divi
    #print(N1CL[15])
    #print(N2CL[15])
    #print(N3CL[15])
    #print(N4CL[15])
    #print(N5CL[15])
    print(" ")


    #This part of the porgram is used to change how to double elimination sequence takes place.
    #For example if there are 4 even then do this sequence. If there are 3 Even then do this sequence, and so on...
    #Even V.S. Odd in Number List

    print("Even V.S. Odd NUM calculations, used for chaning the double elimination sequence.")
    print(" ")
    
    TOC = 0
    TEC = 0
    
    NumOneCount = 0
    if Num1 % 2 == 0:
        NumOneCount += 1
    print(" ")

    if NumOneCount == 1:
        TEC += 1
        print("The First Number Entered is Even")
    elif NumOneCount != 1:
        TOC += 1
        print("The First Number Entered is Odd")

    #Even or Odd for Num2
    NumTwoCount = 0
    if Num2 % 2 == 0:
        NumTwoCount += 1
    print(" ")

    if NumTwoCount == 1:
        TEC += 1
        print("The Second Number Entered is Even")
    elif NumTwoCount != 1:
        TOC += 1
        print("The Second Number Entered is Odd")

    #Even or Odd for Num3
    NumThreeCount = 0
    if Num3 % 2 == 0:
        NumThreeCount += 1
    print(" ")

    if NumThreeCount == 1:
        TEC += 1
        print("The Thrid Number Entered is Even")
    elif NumThreeCount != 1:
        TOC += 1
        print("The Third Number Entered is Odd")

    #Even or Odd for Num4
    NumFourCount = 0
    if Num4 % 2 == 0:
        NumFourCount += 1
    print(" ")

    if NumFourCount == 1:
        TEC += 1
        print("The Fourth Number Entered is Even")
    elif NumFourCount != 1:
        TOC += 1
        print("The Fourth Number Entered is Odd")

    #Even or Odd for Num5
    NumFiveCount = 0
    if Num5 % 2 == 0:
        NumFiveCount += 1
        
    print(" ")#Space

    if NumFiveCount == 1:
        TEC += 1
        print("The Fith Number Entered is Even")
    elif NumFiveCount != 1:
        TOC += 1
        print("The Fith Number Entered is Odd")

    #How many even vs how many odd
        
    print(" ")#Space
        
    EvenVSOddNum = (NumOneCount + NumTwoCount + NumThreeCount + NumFourCount + NumFiveCount)
    print("The number of even user entered numbers is: ",EvenVSOddNum)

    print(" ")
    print("The total odd is:", TOC)
    print("The total even is:", TEC)
    print(" ")

    #Even V.S. Odd in Code Word
    CWD_EL_EV = 0
    CWD_EL_OD = 0

    CWD_EC_EV = 0
    CWD_EC_OD = 0

    
    for i in CWD_EDL:
        if CWD_EDL == 1:
            CWD_EL_EV += 1

    print(CWD_EL_EV)

    for i in CWD_EDL:
        if i % 2 == 0:
            print(f"Even:{i}")

    print(" ")#Space

    #Finds Odd Numbers in Total_Calc_List
    for i in CWD_EDL:
        if i % 2 == 1:
            CWD_EL_OD += 1
    print("Total Number of ODD in Code Word Aa:", CWD_EL_OD)

    for i in CWD_EDL:
        if i % 2 == 0:
            CWD_EL_EV += 1
    print("Total Number of EVEN in Code Word Aa:", CWD_EL_EV)

    print(" ")

    for i in CWD_ELL:
        if i % 2 == 1:
            CWD_EC_OD += 1
    print("The total Number of ODD in Code Word AA: ", CWD_EC_OD)

    for i in CWD_ELL:
        if i % 2 == 0:
            CWD_EC_EV += 1
    print("Total Number of Even in Number List AA:", CWD_EC_EV)

    print(" ")


    # These EVEN and ODD within the Code word will be used to create different Number arangements for the double elimination sequence. 
    
    #Number1 Even VS ODD Numbers
    N1CL_EV = []
    N1CL_OD = []

    for i in N1CL:
        if i % 2 == 0:
            N1CL_EV += [i]
    print("Even Numbers in Num1 list: ", N1CL_EV)

    for i in N1CL:
        if i % 2 == 1:
            N1CL_OD += [i]
    print("Odd Numbers in Num1 list:", N1CL_OD)

    print(" ")#space

    #Number2 Even VS ODD Numbers

    N2CL_EV = []
    N2CL_OD = []

    for i in N2CL:
        if i % 2 == 0:
            N2CL_EV += [i]
    print("Even Numbers in Num2 list: ", N2CL_EV)

    for i in N2CL:
        if i % 2 == 1:
            N2CL_OD += [i]
    print("Odd Numbers in Num2 list:", N2CL_OD)

    print(" ")#Space

    #Number3 Even VS ODD Numbers

    N3CL_EV = []
    N3CL_OD = []

    for i in N3CL:
        if i % 2 == 0:
            N3CL_EV += [i]

    print("Even Numbers in Num3 list:", N3CL_EV)

    for i in N3CL:
        if i % 2 == 1:
            N3CL_OD += [i]
    print("Odd Numbers in Num3 list: ", N3CL_OD)

    print(" ")#Space

    #Number4 Even VS ODD Numbers
    N4CL_EV = []
    N4CL_OD = []

    for i in N4CL:
        if i % 2 == 0:
            N4CL_EV += [i]

    print("Even Numbers in Num4 list:", N4CL_EV)

    for i in N4CL:
        if i % 2 == 1:
            N4CL_OD += [i]
    print("Odd Numbers in Num4 list: ", N4CL_OD)

    print(" ")#Space

    #Number5 Even VS ODD Numbers

    N5CL_EV = []
    N5CL_OD = []

    for i in N5CL:
        if i % 2 == 0:
            N5CL_EV += [i]

    print("Even Numbers in Num5 list:", N5CL_EV)

    for i in N5CL:
        if i % 2 == 1:
            N5CL_OD += [i]
    print("Odd Numbers in Num5 list: ", N5CL_OD)

    print(" ")#Space

    #Multiply A & a Numbers within the Code Word by the Even and Odd numbers in Num calculations

    print("Multiplied A & a Numbers within the Code Word by the Even and Odd numbers in Num calculations.")
    print(" ")#Space

    Num1_CWD_EL_OD = [i * CWD_EL_OD for i in N1CL_OD]
    Num1_CWD_EL_EV = [i * CWD_EL_EV for i in N1CL_EV]
    
    #print(" ")#Space
    #print(CWD_EL_EV)
    #print(Num1_CWD_EL_EV)
    #print(CWD_EL_OD)
    #print(Num1_CWD_EL_OD)
    #print(" ")#Space

    Num2_CWD_EL_OD = [i * CWD_EL_OD for i in N2CL_OD]
    Num2_CWD_EL_EV = [i * CWD_EL_EV for i in N2CL_EV]
    print(Num2_CWD_EL_EV)
    print(" ")#Space
    print(Num2_CWD_EL_OD)
    print(" ")#Space

    Num3_CWD_EL_OD = [i * CWD_EL_OD for i in N3CL_OD]
    Num3_CWD_EL_EV = [i * CWD_EL_EV for i in N3CL_EV]
    print(Num3_CWD_EL_EV)
    print(" ")#Space
    print(Num3_CWD_EL_OD)
    print(" ")#Space

    Num4_CWD_EL_OD = [i * CWD_EL_OD for i in N4CL_OD]
    Num4_CWD_EL_EV = [i * CWD_EL_EV for i in N4CL_EV]
    print(Num4_CWD_EL_EV)
    print(" ")#Space
    print(Num4_CWD_EL_OD)
    print(" ")#Space

    Num5_CWD_EL_OD = [i * CWD_EL_OD for i in N5CL_OD]
    Num5_CWD_EL_EV = [i * CWD_EL_EV for i in N5CL_EV]
    print(Num5_CWD_EL_EV)
    print(" ")#Space
    print(Num5_CWD_EL_OD)
    print(" ")#Space
    print(" ")#Space

    #Divide AA Numbers within the code word by the Even and Odd numbers in Num calculation

    print("Divided AA Numbers within the code word by the Even and Odd numbers in Num calculation.")
    print(" ")#Space

    #Num1 
    Num1_CWD_EC_OD = [i + CWD_EC_OD for i in Num1_CWD_EL_OD]
    print(Num1_CWD_EC_OD) 
    print(" ")#Space
    Num1_CWD_EC_EV = [i + CWD_EC_EV for i in Num1_CWD_EL_EV]
    print(Num1_CWD_EC_EV)
    print(" ")#Space

    #Num2
    
    Num2_CWD_EC_OD = [i + CWD_EC_OD for i in Num2_CWD_EL_OD]
    print(Num2_CWD_EC_OD)
    print(" ")#Space
    Num2_CWD_EC_EV = [i + CWD_EC_EV for i in Num2_CWD_EL_EV]
    print(Num2_CWD_EC_EV)
    print(" ")#Space

    #Num3 
    Num3_CWD_EC_OD = [i + CWD_EC_OD for i in Num3_CWD_EL_OD]
    print(Num3_CWD_EC_OD)
    print(" ")#Space
    Num3_CWD_EC_EV = [i + CWD_EC_EV for i in Num3_CWD_EL_EV]
    print(Num3_CWD_EC_EV)
    print(" ")#Space

    #Num4
    Num4_CWD_EC_OD = [i + CWD_EC_OD for i in Num4_CWD_EL_OD]
    print(Num4_CWD_EC_OD)
    print(" ")#Space
    Num4_CWD_EC_EV = [i + CWD_EC_EV for i in Num4_CWD_EL_EV]
    print(Num4_CWD_EC_EV)
    print(" ")#Space

    #Num5
    Num5_CWD_EC_OD = [i + CWD_EC_OD for i in Num5_CWD_EL_OD]
    print(Num5_CWD_EC_OD)
    print(" ")#Space
    Num5_CWD_EC_EV = [i + CWD_EC_EV for i in Num5_CWD_EL_EV]
    print(Num5_CWD_EC_EV)
    print(" ")#Space
    
    #The next involves adding 
    
        



#Must make sure Code Word is at least 5 characters
if __name__ == '__main__':
    main()