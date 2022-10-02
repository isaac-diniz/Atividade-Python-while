#o comando print("="*62) é usado somente para criar uma organanização visual

#declaração de variáveis
qnt = 0
man = 0
woman = 0

#entradada de dados
nome = input("Digite seu nome: ")
print("="*62)
print("Enquanto o sexo digitado for feminino o programa será repetido")
sex = input("Digite seu sexo (M-F): ").upper()
print("="*62)

#processamento de dados
if sex == "M":
    man = man + 1
else:
    woman = woman + 1

while sex != "M":
    qnt = qnt + 1
    nome = input("Digite seu nome: ")
    print("="*62)
    print("Enquanto o sexo digittado for masculino o programa será repetido")
    sex = input("Digite seu sexo (M-F): ") .upper()
    print("="*62)
    if sex == "M":
        man = man + 1
    else:
        woman = woman + 1

#saída de dados
print(f"A quantidade de vezes que o código foi repetido é: {qnt}")
print(f"A quantidade de vezes que o usuário respondeu que seu sexo é musculino foi: {man}")
print(f"A quantidade de vezes que o usuário respondeu que seu sexo é feminino foi: {woman}")