#Loan calculator app
def loan_info():
    """Get information about the loan and store in a dictionary"""
    loan = {}
    loan['principle'] = float(input('\nEnter the loan amount: '))
    loan['rate'] = float(input('Enter the interest rate: '))/100
    loan['monthly payment'] = float(input('Enter the desired monthly payment amount: '))
    loan['money paid'] = 0
    return loan

def show_loan_info(loan, number):
    """Show the present loan information"""
    print('\n-----------Loan information after ' + str(number) + ' months-----------')
    for key, value in loan.items():
        print(key.title() + ':' + str(value))

def pay_interest(loan):
    # to collect interest on principal and have it added to the previous princple every month
    loan['principle'] = loan['principle'] + loan['principle']*loan['rate']/12

def aggr_money_paid(loan):
    #get the money paid monthly
    loan['principle'] = loan['principle']- loan['monthly payment']
    # to ensure when the loan has been paid fully or not
    if loan['principle']>0:
        loan['money paid']+= loan['monthly payment']
    else:
        #this is to catch when principle is less than or equal to zero
        loan['money paid'] += loan['principle']+ loan['monthly payment']
        loan['principle'] =0

def summarise_loan(initial_amount, number, loan):
    # summary of amount spent to pay off loan
    print('Congratulations! You paid off your loan in ' + str(number) + ' months!')
    print('Your initial loan was $' + str(initial_amount) + ' at a rate of ' + str(loan['rate']*100) + '%.')
    print('Your monthly payment was $' + str(loan['monthly payment']) + '.')
    print('You spent $' + str(loan['money paid']) + ' in total.')
    interest_paid = loan['money paid']- initial_amount
    print('You spent $' + str(round(interest_paid, 4)) + ' on interest.')

#def establish_graph():

print('Welcome to the Loan Calculator App')

# setting variables to their initial value
l_info = loan_info()
initial_amount = l_info['principle']
number = 0
#showingaa       the starting loan information
show_loan= show_loan_info(l_info, number)
input('Press "Enter" to begin paying for loan.')
while l_info['principle']> 0:
    #initerate the number of months
    number += 1
    #instantiate the function to calculate interest and money to be paid per month
    if l_info['principle'] > initial_amount:
        #if after the first month of paying loan, your principle is greater than initial amount,
        #then, you won't ever pay the loan
        print('You will NEVER pay off your loan')
        print('You cannot get ahead of the interest')
        break

    #instantiate the function to calculate interest and money to be paid per month
    pay_interest(l_info)
    aggr_money_paid(l_info)
    show_loan_info(l_info, number)
if l_info['principle'] <= 0:
    summarise_loan(initial_amount, number, l_info)
