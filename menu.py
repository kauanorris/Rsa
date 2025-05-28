from encode import gerar_chaves, codificar, decodificar

def mostrar_menu():
    chave_publica, chave_privada = gerar_chaves()
    
    while True:
        print("\n=================")
        print("1. Codificar a palavra")
        print("2. Decodificar a palavra")
        print("3. Sair")
        
        try:
            op = int(input("Opção: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue

        if op == 1:
            print("=================") 
            mensagem = input("Digite a mensagem para codificar: ")
            mensagem_cifrada = codificar(mensagem, chave_publica)
            print("Mensagem codificada:", mensagem_cifrada)
            
        elif(op == 2):
            print("Cole a mensagem codificada (ex: [123, 456, 789]):")
            entrada = input("> ").strip()
        
            try:
                # Processamento seguro da entrada
                entrada = entrada.replace('[','').replace(']','')
                numeros = [num.strip() for num in entrada.split(',') if num.strip()]
                
                if not all(num.isdigit() for num in numeros):
                    raise ValueError("Contém caracteres não numéricos")
                    
                mensagem_cifrada = [int(num) for num in numeros]
                mensagem_decifrada = decodificar(mensagem_cifrada, chave_privada)
                print("Mensagem decodificada:", mensagem_decifrada)
                
            except Exception as e:
                print(f"Erro: {str(e)}")
                print("Formato esperado: [número1, número2, número3]")
                
        elif op == 3:
            break
        else:
            print("Opção inválida!")