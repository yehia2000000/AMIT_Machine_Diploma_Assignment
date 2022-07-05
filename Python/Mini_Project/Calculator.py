####################################################################################################################
####################################################################################################################
##########################################Author : yehia shahin ####################################################
##########################################Date : 1/7/2022###########################################################
##########################################Version : 1###############################################################
####################################################################################################################
####################################################################################################################



def Sum (Num1 , Num2):
    return Num1+Num2

def Division (Num1 , Num2) :
    return Num1/Num2

def Subtract (Num1 , Num2):
    return Num1 - Num2 

def Mulitiplication (Num1 , Num2):
    return Num1*Num2


if __name__ == '__main__': 
    
    while True : 
        Operation = input ("Please enter the Operator : ")
        if (Operation =='exit'):
            break
        Num1 = input ("Please enter the first number :")
        Num2 = input ("Please enter the Second number :")
        try : 
            Num1 = int(Num1 )
        except : 
            print ("Please enter the Num1 as Number")
        
        try : 
            Num2= int(Num2 )
        except : 
            print ("Please enter the Num2 as Number")
        
        if Operation == "add":
            print(f"The Summation of Two Numbers : {Sum(Num1, Num2)}")
        elif Operation == "sub":
            print(f"The subtraction of Two Numbers {Subtract(Num1, Num2)}")
        elif Operation == "div":
            print (f"The Division of Two Numbers {Division(Num1, Num2)}")
        elif Operation == "mult" :
            print (f"The Multiplication of two Numbers : {Mulitiplication(Num1, Num2)}")
        else : 
            print ("PLease Enter true Operation and return put your inputs Number")      