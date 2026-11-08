'''
💻 DESAFIO #06 — VALIDADOR DE SENHA FORTE

Criar um algoritmo/função que receba uma senha (string) e valide se ela atende aos critérios 
de segurança recomendados, informando detalhadamente os erros caso não seja válida.

✅ Critérios
Para a senha ser considerada Forte / Válida, ela DEVE atender a todas as condições simultaneamente:
Comprimento: no mínimo 8 caracteres.
Letra maiúscula: pelo menos uma (A-Z).
Letra minúscula: pelo menos uma (a-z).
Número: pelo menos um (0-9).
Caractere especial: pelo menos um (ex.: @, #, $, %, &, !, *).

🧪 Casos de teste
Caso 1
Entrada: "Senha123"
Saída: "INVALIDA -> Motivo: Não contém caractere especial."

Caso 2
Entrada: "techsisters"
Saída: "INVALIDA -> Motivo: Faltam caracteres maiúsculos, números e caracteres especiais."

Caso 3
Entrada: "Code#2026"
Saída: "VALIDA -> A senha atende a todos os requisitos de segurança!"

__________________________________
TECH SISTERS • DESAFIO DO CÓDIGO
'''

while True:
    senha = input('Digite uma senha: ')

    maiuscula = False
    minuscula = False
    numero = False
    especial = False

    # Percorre cada caractere da senha
    for letra in senha:
        if letra.isupper():
            maiuscula = True

        if letra.islower():
            minuscula = True

        if letra.isdigit():
            numero = True

        if letra in '@#$%&!*':
            especial = True

    # Verifica os requisitos
    if len(senha) < 8:
        print('Erro: a senha precisa ter no mínimo 8 caracteres.')

    if not maiuscula:
        print('Erro: falta uma letra maiúscula.')

    if not minuscula:
        print('Erro: falta uma letra minúscula.')

    if not numero:
        print('Erro: falta um número.')

    if not especial:
        print('Erro: falta um caractere especial.')

    # Resultado final
    if len(senha) >= 8 and maiuscula and minuscula and numero and especial:
        print('Senha cadastrada com sucesso!')
        break
    else:
        print('Senha inválida!')