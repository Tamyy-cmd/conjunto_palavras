def titulo(msg):
    tam = 80
    print('-' * tam)
    print(msg.center(tam))
    print('-' * tam)

def leia_int(numero):
    while True:
        try:
            num = int(input(numero))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[32mUsuário preferiu não digitar este número\033[m')
            return 0
        else:
            return num

def criar_conjunto(num, nome='C'):
    conj = []
    for j in range(1, num + 1):
        while True:
            palavra = input(f'  Insira a {j}º palavra: ').strip()
            if not palavra:
                print('\033[31mDigite uma palavra válida.\033[m')
                continue
            if not palavra.isalpha():
                print('\033[31mDigite apenas letras.\033[m')
                continue
            break
        conj.append(palavra)
    print(f"\n\033[35m{nome} = {{{', '.join(conj)}}}\033[m")
    return conj

titulo('\033[32mCONJUNTOS DE PALAVRAS\033[m')
num_a = leia_int('-> Quantas palavras deseja para o conjunto A?: ')
A = criar_conjunto(num_a, 'A')
num_b = leia_int('\n-> Quantas palavras deseja para o conjunto B?: ')
B = criar_conjunto(num_b, 'B')

titulo('\033[32mMENU\033[m')
print("""1 --> União
2 --> Interseção
3 --> Diferença (A - B)
4 --> Diferença (B - A)""")
print('-' * 80)

while True:
    escolha = leia_int('\n-> Digite o número da sua escolha (0 para sair): ')
    if escolha == 1:
        print('\nUnião entre A e B:')
        u = set(A) | set(B)
        print(f"\033[35mA ∪ B = {{{', '.join(u)}}}\033[m")

    elif escolha == 2:
        print('\nInterseção entre A e B:')
        i = set(A) & set(B)
        print(f"\033[35mA ∩ B = {{{', '.join(i)}}}\033[m")

    elif escolha == 3:
        print('\nDiferença entre A e B:')
        d1 = set(A) - set(B)
        print(f"\033[35mA - B = {{{', '.join(d1)}}}\033[m")

    elif escolha == 4:
        print('\nDiferença entre B e A:')
        d2 = set(B) - set(A)
        print(f"\033[35mB - A = {{{', '.join(d2)}}}\033[m")

    elif escolha >= 5:
        print('\033[31mEscolha inválida!\033[m')
        continue
    else:
        titulo('FIM')
        break
