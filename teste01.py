

dinheiro = float(input())

if 0 < dinheiro < 1000000.00:
  nota100 = dinheiro // 100
  dinheiro = dinheiro % 100
  nota50 = dinheiro // 50
  dinheiro = dinheiro % 50
  nota20 = dinheiro // 20
  dinheiro = dinheiro % 20
  nota10 = dinheiro // 10
  dinheiro = dinheiro % 10
  nota5 = dinheiro // 5
  dinheiro = dinheiro % 5
  nota2 = dinheiro // 2
  dinheiro = dinheiro % 2
  moeda1 = dinheiro // 1
  dinheiro = dinheiro % 1
  moeda50 = dinheiro // 0.5
  dinheiro = dinheiro % 0.5
  moeda25 = dinheiro // 0.25
  dinheiro = dinheiro % 0.25
  moeda10 = dinheiro // 0.10
  dinheiro = dinheiro % 0.10
  moeda5 = dinheiro // 0.05
  dinheiro = dinheiro % 0.05
  moeda01 = dinheiro // 0.01
  
  print('NOTAS:')
  print('{:.0f} nota(s) de R$ 100.00'.format(nota100))
  print('{:.0f} nota(s) de R$ 50.00'.format(nota50))
  print('{:.0f} nota(s) de R$ 20.00'.format(nota20))
  print('{:.0f} nota(s) de R$ 10.00'.format(nota10))
  print('{:.0f} nota(s) de R$ 5.00'.format(nota5))
  print('{:.0f} nota(s) de R$ 2.00'.format(nota2))

  print('MOEDAS:')
  print('{:.0f} moeda(s) de R$ 1.00'.format(moeda1))
  print('{:.0f} moeda(s) de R$ 0.50'.format(moeda50))
  print('{:.0f} moeda(s) de R$ 0.25'.format(moeda25))
  print('{:.0f} moeda(s) de R$ 0.10'.format(moeda10))
  print('{:.0f} moeda(s) de R$ 0.05'.format(moeda5))
  print('{:.0f} moeda(s) de R$ 0.01'.format(moeda01))
  
else:
  print('Presentation Error')