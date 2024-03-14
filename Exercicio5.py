a = int(input("informe o valor de a: "))
b = int(input("informe o valor de b: "))
c = int(input("informe o valor de c: "))

delta = b**2 - 4*a*c

x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)

print(" a primeira raiz é: ", x1)
print(" a segunda raiz é: ", x2)