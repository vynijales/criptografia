print('--------- Criptograia função 1 grau ---------')
# Função 1º - ax + b

verficacao1 = []
valor_cripM1 = []
def criptografar(texto, a, b):
    texto_criptografado = ''
    for letra in texto:
        valor = ord(letra)
        valor_criptografado = a * valor + b
        if valor_criptografado > 127:
            valor_cripM1.append(valor_criptografado)
            valor_criptografado = ((valor + valor_criptografado) % 127)
            verficacao1.append(1)
        else:
            verficacao1.append(0)
            valor_cripM1.append(0)
        letra_criptografada = chr(valor_criptografado)
        texto_criptografado += letra_criptografada

    return texto_criptografado

def descriptografar(texto, a, b):
    texto_descriptografado = ''
    i = 0
    for letra in texto:
        valor_criptografado = ord(letra)
        if verficacao1[i] == 1:
            valor = ((valor_criptografado - valor_cripM1[i]) % 127)
        else:
            valor = (valor_criptografado - b) / a
        letra_descriptografada = chr(int(valor))
        texto_descriptografado += letra_descriptografada
        i += 1

    return texto_descriptografado

print('Entre com os valores de a e b para a função ax + b')
a = int(input('a: '))
b = int(input('b: '))
texto = str(input('Qual mensagem deseja criptografar: '))
texto_criptografado = criptografar(texto, a, b)
print(texto_criptografado)
texto_descriptografado = descriptografar(texto_criptografado, a, b)
print(texto_descriptografado)

print()

print('--------- Criptograia função 2 grau ---------')
# Função 2º - ax² + bx + c

verficacao2 = []
valor_cripM2 = []
def criptografar(texto, a, b, c):
    texto_criptografado = ''
    for letra in texto:
        valor = ord(letra)
        valor_criptografado = a * valor ** 2 + b * valor + c
        if valor_criptografado > 127:
            valor_cripM2.append(valor_criptografado)
            valor_criptografado = ((valor + valor_criptografado) % 127)
            verficacao2.append(1)
        else:
            verficacao2.append(0)
            valor_cripM2.append(0)
        letra_criptografada = chr(valor_criptografado)
        texto_criptografado += letra_criptografada

    return texto_criptografado

def descriptografar(texto, a, b, c):
    texto_descriptografado = ''
    yv = imagemFuncao(a, b, c)
    i = 0
    for letra in texto:
        valor_criptografado = ord(letra)
        delta = b ** 2 - 4 * a * (c - valor_criptografado)
        valor1 = (-b + delta ** 0.5) / (2 * a)
        valor2 = (-b - delta ** 0.5) / (2 * a)
        if verficacao2[i] == 1:
            valor = ((valor_criptografado - valor_cripM2[i]) % 127)
        else:
            if valor2 < yv:
                valor = valor1
            else:
                valor = valor2
        letra_descriptografada = chr(int(valor))
        texto_descriptografado += letra_descriptografada
        i += 1

    return texto_descriptografado

def imagemFuncao(a, b, c):
    delta = b ** 2 - 4 * a * c
    yv = -delta / (4 * a)
    return yv

print('Entre com os valores de a e b para a função ax² + bx + c:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
texto = str(input('Qual mensagem deseja criptografar: '))
texto_criptografado = criptografar(texto, a, b, c)
print(texto_criptografado)
texto_descriptografado = descriptografar(texto_criptografado, a, b, c)
print(texto_descriptografado)

print()

print('--------- Criptograia função 3 grau ---------')
# Função 3º - x³ + x² + 1

verficacao3 = []
valor_cripM3 = []
def criptografar(texto):
    texto_criptografado = ''
    for letra in texto:
        valor = ord(letra)
        valor_criptografado = valor ** 3 + valor ** 2 + 1
        if valor_criptografado > 127:
            valor_cripM3.append(valor_criptografado)
            valor_criptografado = ((valor + valor_criptografado) % 127)
            verficacao3.append(1)
        else:
            verficacao3.append(0)
            valor_cripM3.append(0)
        letra_criptografada = chr(valor_criptografado)
        texto_criptografado += letra_criptografada

    return texto_criptografado

def descriptografar(texto):
    texto_descriptografado = ''
    i = 0
    for letra in texto:
        valor_criptografado = ord(letra)
        if verficacao3[i] == 1:
            valor = ((valor_criptografado - valor_cripM3[i]) % 127)
        else:
            valor = valor_criptografado ** (1/3)
        letra_descriptografada = chr(int(valor))
        texto_descriptografado += letra_descriptografada
        i += 1

    return texto_descriptografado

texto = str(input('Qual mensagem deseja criptografar: '))
texto_criptografado = criptografar(texto)
print(texto_criptografado)
texto_descriptografado = descriptografar(texto_criptografado)
print(texto_descriptografado)
