# func fatorial
def calc_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calc_fatorial(n-1)

print("1 - Calcular Fatorial")
print("2 - Sair do Programa")

#Programa Principal
if __name__ == "__main__":
    while True:
        opcoes = input("Escolha uma Opção: ")
        match opcoes:
            case "1":
                try:
                    n = int(input("Informe um número inteiro positivo: "))

                    if n >= 0:
                        print(f" O valor de {n} é {calc_fatorial(n)}.")
                        
                    else:
                        print(f"Não existe fatorial de {n}.")
                        
                except:
                    print("Não foi possivel calcular o fatorial. ")
                    
            case "2":
                print("Saindo do Programa...")
                break
            case _:
                print("Opção Inválida")
