nwdh = int(input("Wieviele Wiederholungen? "))

n1, n2 = 0, 1
count = 0

if nwdh <= 0:
   print("Einen positiven Integer eingeben")
elif nwdh == 1:
   print("Fibonacci Reihenfolge bis",nwdh,":")
   print(n1)
else:
   print("Fibonacci Reihenfolge:")
   while count < nwdh:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1