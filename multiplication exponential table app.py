print('Welcome to the Multiplication/Exponent Table App')
name= input('Hello, what is your name: ')
number=float(input('What number would you like to work with: '))
print('Multiplication table for ' + str(number))
for i in range(1,10):
    output= i*number
    output= round(output, 2)
    print('\t' + str(float(i)) + ' ' + '*' + ' ' + str(number) + '=' + ' ' + str(output))


print('\nExponent table for ' + str(number))
for i in range(1,10):
    output= i**number
    output= round(output, 2)
    print('\t' + str(number) + '^' + str(i) + '=' + ' ' + str(output))

print('\n' + name.title() + ' ' + ', Math is cool!')