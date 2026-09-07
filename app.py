print("=== CALCULADORA DE CONSUMO ELÉTRICO ===")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (horas): "))

consumo_mensal = (potencia * horas_dia * 30) / 1000

print()
print("=== RESULTADO ===")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")