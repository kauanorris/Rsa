def mdc(a, b):
    # Algoritmo de Euclides para MDC
    while b != 0:
        a, b = b, a % b
    return a

def euclides_estendido(a, b):
    # Algoritmo estendido de Euclides 
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = euclides_estendido(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    # Inverso modular usando o algoritmo estendido de Euclides - Versão Corrigida 
    g, x, y = euclides_estendido(a, m)
    if g != 1:
        return None  # Não existe inverso se a e m não são coprimos
    return x % m  # Corrigido: removido o return extra que causava o erro

def gerar_chaves():
    # Gerar par de chaves pública e privada RSA - Versão Melhorada 
    # Passo 1: Escolher dois primos (fixos para exemplo)
    p = 61
    q = 53
    
    # Passo 2: Calcular n = p * q
    n = p * q
    
    # Passo 3: Calcular a função totiente φ(n) = (p-1)(q-1)
    phi = (p - 1) * (q - 1)
    
    # Passo 4: Escolher e que seja coprimo com φ(n)
    e = 17  
    
    # Passo 5: Calcular d, o inverso multiplicativo de e módulo φ(n)
    d = modinv(e, phi)
    
    if d is None:
        raise ValueError("Não foi possível encontrar inverso modular. Escolha outro valor para e.")
    
    # Chave pública (e, n), chave privada (d, n)
    return ((e, n), (d, n))

def codificar(mensagem, chave_publica):
    # Codificar mensagem usando a chave pública 
    e, n = chave_publica
    # Verificar se n é grande o suficiente para a mensagem
    if any(ord(char) >= n for char in mensagem):
        raise ValueError("Mensagem contém caracteres que excedem o limite de n")
    return [pow(ord(char), e, n) for char in mensagem]

def decodificar(mensagem_cifrada, chave_privada):
    # Decodificar mensagem usando a chave privada - Versão com Tratamento de Erros
    d, n = chave_privada
    
    # Verificar se a chave privada é válida
    if None in chave_privada:
        raise ValueError("Chave privada inválida")
    
    try:
        return ''.join([chr(pow(bloco, d, n)) for bloco in mensagem_cifrada])
    except TypeError:
        raise ValueError("Mensagem cifrada deve conter apenas números inteiros")
    except ValueError as e:
        raise ValueError(f"Valor decodificado inválido: {str(e)}")
