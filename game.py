from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nivel de dificuldade, 1 2 3 ou 4: '))

    calc: Calcular = Calcular(dificuldade)

    print('informe o resultado para a seguinte operacao: ')
    calc.mostrar_operacao()

    resultado : int = int(input())
    
    if calc.checar_resultado(resultado):
        pontos += 1
        print (f'Voce tem {pontos} pontos(s).')

    continuar: int = int(input('Deseja continuar no jogo?  1- sim  2- nao  '))

    if continuar:
        jogar(pontos)
    else:
        print(f'finalizou ate {pontos} pontos(s)')

if __name__ == '__main__':
    main()
