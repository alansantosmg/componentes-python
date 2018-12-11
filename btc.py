def readme():
        print('\033[H\033[J')
        print('''Módulo btc.py
Autor: Alan Santos - alansantosmg@gmail.com
Conteúdo: Conjunto de funções para entrada e validação de dados via console. 

Entrada: Parâmetro prompt: Texto com instruções para usuário.
Validação: Se usuário entrar tipo incorreto, continua solicitando entrada. 
Retorno: Tipo de dado entrado.

read_text(prompt)
read_int(prompt)
read_float(prompt)
read_range_int(prompt)
read_range_float(prompt)

Exemplos de chamada de função:

x = read_text('Digite algum texto: ' )
x = read_float('Digite um número decimal: ')
x = read_int('Digite um número inteiro: ' )
x = read_range_int('Digite um numero de 1 a 5: ',1,5) 
x = read_range_int(prompt='Digite nr de 1 a 5: ',min_value=1, max_value=5)
x = read_range_float('Entre decimal de 1.5 a 10.5: ', 1.5, 10.5)
x = read_range_float(prompt='Entre nr 1.5 a 9.7:',min_value=1.5,max_value=9.5)                       
''')


def read_text(prompt):
        '''
        Mostra um prompt que lê uma string de 
        texto e valida se o usuário não está
        usando sequencias de escape para abortar
        '''
        while True: 
                try:
                        result = input(prompt) 
                        break
                except KeyboardInterrupt:
                        print('Entre com o texto')
        return result




def read_int(prompt):
        ''' 
        Roda em conjunto com funçao de entrada de texto. 
        Se entrada for numero, verifica se é int
        se não for int gera excecao e solicita nova entrada
        '''

        while True:
                try:
                        entrada_numero = read_text(prompt)
                        result = int(entrada_numero)
                        break
                except ValueError:
                        print('\nEntre com valor numérico.\n')
        return result




def read_float(prompt):
        ''' 
        Roda em conjunto com funçao de entrada de texto. 
        Se entrada for numero, verifica se é float
        se não for float gera excecao e solicita nova entrada
        '''

        while True:
                try:
                        entrada_numero = read_text(prompt)
                        result = float(entrada_numero)
                        break
                except ValueError:
                        print('Entre com numero')
        return result



def read_range_int(prompt, min_value, max_value):
    '''
    Verifica se entrada de numero está dentro
    do range especificado nos parametros
    Caso não esteja, solicita nova entrada
    '''
    while True:
        entrada_range = read_int(prompt)
             
        if min_value > max_value:  #Detecta inversao de parametros
            raise Exception('Minimo é maior do maximo. Corrija')
           
        if entrada_range < min_value:
            print('Valor muito baixo.')
            continue
        elif entrada_range > max_value:
            print('Valor muito alto.')
            continue
        break  
    return entrada_range



def read_range_float(prompt, min_value, max_value):
    '''
    Verifica se entrada de numero está dentro
    do range especificado nos parametros
    Caso não esteja, solicita nova entrada
    '''
    while True:
        entrada_range = read_float(prompt)
             
        if min_value > max_value:  #Detecta inversao de parametros
            raise Exception('Minimo é maior do maximo. Corrija')
           
        if entrada_range < min_value:
            print('Valor muito baixo.')
            continue
        elif entrada_range > max_value:
            print('Valor muito alto.')
            continue
        break  
    return entrada_range

if __name__ == "__main__":
    # Mostra instruções de utilização do módulo.     
    readme()


