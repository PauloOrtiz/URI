salario = float(input())

if(salario <= 2000.00):
  print("Isento")
elif(2000.01 <= salario <= 3000):
  salario -= 2000.00
  imposto = salario * 0.08
  print("R$ {:.2f}".format(imposto))
elif(3000.01 <= salario <= 4500):
  salario -= 2000.00
  imposto8 =  1000*0.08
  imposto18 = (salario - 1000) * 0.18 
  imposto_final = imposto8 + imposto18   
  print("R$ {:.2f}".format(imposto_final))
elif(4500.01 <= salario):
  salario -= 2000.00
  imposto8 = 1000*0.08
  imposto18 = 1500*0.18
  imposto28 = (salario - 2500) * 0.28 
  imposto_final = imposto8 + imposto18 + imposto28  
  print("R$ {:.2f}".format(imposto_final))