while True:
 print('menu')
 print('enter "add"to add')
 print('enter "sub"to subtract')
 print('enter "end" to end calculations')
 user_input=input(':')
 if user_input=="end":
  break 
 elif user_input=="add":
    num1=float(input('enter the 1st number:')) 
    num2=float(input('enter 2nd number:'))
    result=str(num1+num2)
    print('answer is'+ result)
 elif user_input=="sub":
    num1=float(input('enter the 1st number:'))
    num2=float(input('enter 2nd number:'))
    result=str(num1-num2)
    print('answer is'+ result)
