x = 0.3
print(x)
y = 0.1 + 0.2
print(y) 
print(x==y)#False

#Primera forma
y = float(format(y, ".2g"))
print(y)
print(x==y)#True

#Segunda forma
y = 0.1 + 0.2
tolerance = 0.0000001
print(abs(x-y)<tolerance)

#Tercera forma
y = 0.1 + 0.2
decimales = 1
y = float(format(y, f".{decimales}f"))
print(y)#0.3
print(x==y)#True
