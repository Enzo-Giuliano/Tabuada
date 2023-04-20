ope = None
num1 = None
num2 = None

print("Bem-Vindo a Tabuada Online de Adição e Multiplicação!\n") 
ope = int(input("Insira 1 para Adição ou 2 para Multiplicação.\n"))
num1 = int(input("Insira o número em que deseja saber a tabuada.\n"))

if ope == 1:
  print("Aqui está a tabuada solicitada:\n")
  for num2 in range(1, 11):
    print(num1,"+",num2,"=",num1+num2)
  
if ope == 2:
  print("Aqui está a tabuada solicitada:\n")
  for num2 in range(1, 11):
    print(num1,"*",num2,"=",num1*num2)
