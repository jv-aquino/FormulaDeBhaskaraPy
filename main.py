#Aplicação do Fórmula de Bhaskara(x = -b +- √b² -4.a.c / 2.a) em Equações de Segundo Grau com Python - v1.0.0 João Vitor de Aquino, 27/06/2020
#Disponível em: https://github.com/jv-aquino/FormulaDeBhaskaraPy
#Declarando variáveis da equação(a, b, c) e valores totais(valorFinal1,  valorFinal2) 
#Além de todas as outras variáveis que serão usadas (incognita, incognitaFloat, incognitaInvalida, valorInvalido, valido, erro)
a = b = c = delta = valorFinal1 = valorFinal2 = float
incognita, incognitaFloat, incognitaInvalida, valorInvalido, valido, erro = str, str, 'A incógnita só pode ter 1 caractere, sendo ele não-numérico', 'Valor(es) Inválido(s)', True, '---------------\nUm erro ocorreu'

#Obtendo a letra que represanta a incógnita
incognita = input('Fórmula de Bháskara(x = -b +- √b² -4.a.c / 2.a) em Python v1.0.0 \n-------------------------------------\nQual a letra que representa a incógnita (como X, por exemplo)? \n')

#Tentando transformar a incógnita em float, para depois verificar isso e evitar erros
try:
 incognitaFloat = float(incognita)
 print(incognitaInvalida)
except ValueError:
 None

#Verificando se a incógnita tem só um valor, e se ele não é numérico, se algum dos casos for verdadeiro aparecerá um erro
if (len(incognita)) > 1 or incognitaFloat == float:
 valido = False
 print(incognitaInvalida)
else:
 None

#Obtendo os próximos valores (a, b, c) caso tudo esteja correto
if valido == True:
 a = input('Qual o valor de a na equação (\"' + incognita +'²\", por exemplo, seria igual a \"1\")? \n')
 b = input('Qual o valor de b na equação (\"3' + incognita +'\", por exemplo, seria igual a \"3\")? \n')
 c = input('Qual o valor de c na equação? \n')

#Verificando se todos os valores estão corretos (se são números válidos) 
 try:
  a, b, c = float(a), float(b), float(c)
 except ValueError:
  print(valorInvalido)
  valido = False
else:
 None

#Continuando a conta caso os valores estejam corretos
if valido == True:
 #Calculando o valor de Δ (delta) e printando o mesmo 
 delta = b * b + (-4 * a * c)
 delta = delta**(0.5)
 delta = str(delta)
 print('\n' + 'Δ = ' + delta + ';')
 delta = float(delta)

 #Com o delta em mãos, calculando agora todo o resto, e finalmente, printando o resultado
 valorFinal1, valorFinal2 = (-b + delta) / (2 * a), (-b - delta) / (2 * a)
 valorFinal1, valorFinal2 = str(valorFinal1), str(valorFinal2)
 print(incognita + '₁ = ' + valorFinal1 + '; \n' + incognita + '₂ = ' + valorFinal2 + ';\nS = {' + valorFinal1 + '; ' + valorFinal2 + '}')

#Caso um ou mais valores sejam inválidos, aparecerá uma mensagem de erro
else:
 print(erro)
