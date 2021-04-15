def favBank():

    print('Options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')

    selectedOption = int(input('Please select an option:'))
            
    if(selectedOption == 1):
        print('you selected %s' % selectedOption)
        
    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
                
    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)
                
    else:
        print('Invalid Option selected, please try again')

def withdrawal():
    
    amount = float(input("Enter Amount")
    print('processing..., please wait')
    print('take your cash')               
    
    
                   

name = input("Your name \n")

allowedUserDictionary = {
    'Tony':'passwordTony',
    'Kess':'passwordKess',
    'Tess':'passwordTess'
    }

if(name in allowedUserDictionary):
    password = input("Your password? \n")    

    if(password == allowedUserDictionary[name]):
        
        print('Welcome %s' % name)
        favBank()    
        
        
    else:
        print('Stealing is bad, please try again')

else:

    print('Are you a Thief?, please try again')







