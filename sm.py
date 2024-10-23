temperature=int(input("Enter Temperature"))
if temperature<40:
    print("cold")
else:
    print("nice")
base_hours=40
over=1.5
hours= int(input('Enter the number of hours worked:'))  
pay=int(input('Enter the hpurly pay rate:'))
if hours>base_hours:
    overtime_hours=hours-base_hours
    overtime_pay=overtime_hours*pay
    total=base_hours*pay*overtime_pay
    print( 'overtime payment', total)
else:
    total=hours*pay
    print('Total time payment', total)
    x=5
if x<10:
        print('Smaller')
if x>25:
        print('Bigger')
print('Finish')
x=5
if x==5:
    print('Equals 5')
if x>4:
    print('Greater than 4')
if x>=5:
    print('Greater than or equals to 5')
if x<6:
    print('less than 6')
if x<=5:
     print('less than or equals 5')
if x!=6:
    print('not equal to 6')                    