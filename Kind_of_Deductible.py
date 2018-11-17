# /////////Imports////////#

from fractions import Fraction
from  termcolor  import colored

#////INPUTS////#
print (colored("Powered",'yellow'),colored("By",'blue'),colored("@@",'red'))
print ("Code_map")
print (colored("Inputs", color='blue'))
print (colored("special", color='red'))
print (colored("error", color='red', attrs=['reverse']))
print (colored("output", color='cyan', attrs=['reverse']))

print ("")

Enter_numerator = input(colored("Enter numerator : ",'blue'))
Enter_numerator = int(Enter_numerator)

Enter_Denominator = input(colored("Enter Denominator : ",'blue'))
Enter_Denominator = int(Enter_Denominator)

#////Error////#

if Enter_Denominator == 0 or Enter_numerator == 0 :
    print (colored("Syntax error",'red',attrs=['reverse']))
    quit ()
if Enter_Denominator % Enter_numerator == 0 or Enter_numerator % Enter_Denominator == 0 :
    print (colored(Enter_numerator/Enter_Denominator,'red'))
    print (colored(" مختوم : kind",color='cyan',attrs=['reverse']))#,on_color='red'))
    quit ()

elif Enter_Denominator is 1:
    print (colored(Enter_numerator,'red'))
    quit ()

elif Enter_Denominator == Enter_numerator:
    print (colored('1','red'))
    quit ()

#////Simplified deduction////#

Variable_Simplified = Fraction (numerator=Enter_numerator, denominator=Enter_Denominator)

Simplified = Variable_Simplified.denominator

print(colored("Definition denominator after fractional decomposition(makhrejkasr pas az tajziee kasr) : ",color='green',attrs=['reverse']),colored(Simplified,'blue'))

#////Variable////#

primfac = []
d = 2

Rate = 0
scroll = 0
Rate = int (Rate)
scroll = int (scroll)

#////calcute primfac ////#
while d*d <= Enter_Denominator :
    while (Enter_Denominator % d) == 0:
        primfac.append(d)
        Enter_Denominator //= d
    d += 1

if Enter_Denominator > 1:
    primfac.append(Enter_Denominator)

print (colored("Parsing(Tagzieh) :",color='yellow',attrs=['reverse']),colored(primfac,'blue'))

#///////Detection is closed or uncoded//////#

for i in range(len(primfac)) :
    i = primfac[scroll]
    i = int(i)
    if i==2 :
      Rate = Rate+1
    elif i==5 :
        Rate = Rate + 1
    else :
        Rate = Rate + 0
    scroll = scroll+1

# print(Rate)
if Rate == len(primfac):
    print (colored(" مختوم : kind",color='cyan',attrs=['reverse']))#,on_color='red'))
    print (colored(Enter_numerator/Enter_Denominator,color='cyan',attrs=['reverse']))
    quit ()
elif Rate > 0 :
    print (colored(" نامختوم متناوب مرکب : kind",color='cyan',attrs=['reverse']))#,on_color='red'))
    print (colored(Enter_numerator/Enter_Denominator,color='cyan',attrs=['reverse']))
    quit ()
elif Rate == 0:
    print (colored(" نامختوم متناوب ساده : kind", color='cyan', attrs=['reverse']))  # ,on_color='red'))
    print (colored(Enter_numerator/Enter_Denominator,color='cyan',attrs=['reverse']))
    quit ()
#Line 37
#Line 59
#Line 74