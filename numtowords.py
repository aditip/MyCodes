#To display a number into words upto 4 digits

index=0
unit_place=0
tens_place=0
hundreds_place=0

while(True):
  num = int(input("Enter a number :"))
  if num>=0:
    break

def unitDigit(no):

  unit_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
  print(unit_list[no])

if num>=1 and num<=9:
  unitDigit(num)

if num>=10 and num<=19:

  tens_list = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
  index=num%10
  print(tens_list[index])

def tensDigit(no):
  extended_tens_list = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
  index=(no//10)-2
  unit_place=no%10

  if unit_place==0:
    print(extended_tens_list[index], end='\t')

  else:
    print(extended_tens_list[index], end='\t')
    unitDigit(unit_place)

if num>=20 and num<=99:
  tensDigit(num)

def hundredsDigit(no):

  hundreds_list = ['One hundred','Two hundred','Three hundred','Four hundred','Five hundred','Six hundred','Seven hundred','Eight hundred','Nine hundred']

  index=(no//100)-1

  if no%100 !=0:
    print(hundreds_list[index], end='\t')

    tens_place=no%100
    unit_place=no%10

    if tens_place>=1 and tens_place<=9:
      print("and", end='\t')
      unitDigit(unit_place)

    else:
      tensDigit(tens_place)

  else:
    print(hundreds_list[index], end='\t')

if num>=100 and num<=999:
  hundredsDigit(num)

if num>=1000 and num<=9999:

  thousands_list = ['One Thousand','Two Thousand','Three Thousand','Four Thousand','Five Thousand','Six Thousand','Seven Thousand','Eight Thousand','Nine Thousand']

  index=(num//1000)-1

  if num%1000 !=0:
    print(thousands_list[index], end='\t')

    hundreds_place=num%1000
    tens_place=num%100

    if hundreds_place>=1 and hundreds_place<100:
      print("and", end='\t')
      tensDigit(tens_place)

    else:
      hundredsDigit(hundreds_place)

  else:
    print(thousands_list[index], end='\t')
