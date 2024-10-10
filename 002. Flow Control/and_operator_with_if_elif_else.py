# Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. 
# In these cases, you can build larger boolean expressions using boolean operators. 
# These operators (also known as logical operators) combine smaller boolean expressions into larger boolean expressions.

credits = 100
gpa = 4.0

if credits < 120 and gpa < 2.0:
    print('Your credits and gpa are below minmum acceptable. You cannot graduate this year')
    
elif credits < 120 and gpa >= 2.0:
    print('You cannot graduate this year. Your gpa is fine but your credits are below 120')    
    
elif credits >= 120 and gpa < 2.0:
    print('You cannot graduate this year. Your credits are fine but your gpa is below 2.0')      
    
elif  credits >= 190 and gpa >= 4.0:    
    print('You have an exceptional credit and gpa score. You have qualified to received the "Graduate with Distinction" award')      

elif credits >= 120 and gpa > 3.5:
    print('You will graduate with honors')
  
elif credits >= 120 and gpa >= 3.0:
    print('You have excelled and can gradute')  
    
elif credits >= 120 and gpa >= 2.0:
    print("You meet the requirements to graduate!") 

else: 
    print('Sorry but your gpa is not high enough. You cannot graduate this year')