def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nwdh = 10

if nwdh <= 0:
   print("Einen positiven Integer eingeben!")
else:
   print("Fibonacci Reihenfolge:")
   for i in range(nwdh):
       print(recur_fibo(i))