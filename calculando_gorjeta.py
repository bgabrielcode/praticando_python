valor_da_conta = float(input("Digite o valor da conta: "))
porcentagem_da_gorjeta = float(input("Digite a porcetagem da gorjeta: "))
gorjeta = (porcentagem_da_gorjeta / 100) * valor_da_conta
total_a_pagar = valor_da_conta + gorjeta
print(f"Valor da gorjeta {gorjeta:.2f}")
print(f"Total a pagar {total_a_pagar:.2f}")