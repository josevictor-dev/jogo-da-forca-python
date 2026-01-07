import getpass

palavra = getpass.getpass('Digite a palavra secreta: ').lower()

tentativas = 0
letras_armazenadas = ''

while True:
    letradigitada = input('letra: ')
    letras_finais = ''

    if len(letradigitada) != 1:
        print('Digite apenas uma letra')
        continue

    if letradigitada in letras_armazenadas:
            print('Essa letra ja foi')
            continue

    if len(letradigitada) != 1:
        print('Digite apenas uma letra: ')
        
    if letradigitada in palavra:
        letras_armazenadas += letradigitada

    for percorrer in palavra:
        if percorrer in letras_armazenadas:
            letras_finais += percorrer
        else:
            letras_finais += '*'

    tentativas += 1

    print(f'{letras_finais} , Tentativas: {tentativas}')
   

    if letras_finais == palavra:
        print(f'Parabéns você acertou a palavra: {palavra}')
        break
