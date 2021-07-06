#Codigos que se deben usar. BCD, Gray, Excess of 3, Johnson, Paridad, PentaBit, Hamming.
#Se aceptan de la forma  bcd, gry, ed3, jsn, par, pbt, ham
#Base cualquiera a decimal, decimal a binario.

codigos = ["bcd","gry","ed3","jsn","par","pbt","ham"]  #Solo lo usaremos para revisar casos!
bases_posibles = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+?")

#Funcion que revisa si es binario o no
def es_binario(valor):
    for i in str(valor):
        if i in "10":
            bin = True
        else:
            bin=False
            break
    if bin==True:
        return True
    else:
        return False

#Función que pasa cualquier decimal a numero binario
def dec_to_binary(valor):
    valor=int(valor)
    binario = ''
    while valor // 2 != 0:
        binario = str(valor % 2) + binario
        valor = valor // 2
    return str(valor) + binario

#Funcion que pasa cualquier valor en cualquier base a decimal.
def cualquier_base_to_dec(valor,b):
    list = []
    pos = 0
    decimal =0
    #Revisamos caso donde sea unario o igual a 10:
    if b==1:
        return (len(valor))
    elif b == 10:
        return valor
    else:
        for i in str(valor):
            list.append(i)
        for i in range(len(list)):
            if list[i] in bases_posibles:
                a = bases_posibles.index(list[i])
                list.pop(pos)
                list.insert(pos,a)
                pos = pos + 1
        list.reverse()
    pos = 0
    for i in list:
        decimal += int(list[pos])*(b**pos)
        pos+=1
    return decimal

#Funcion que pasa de un decimal a cualquier base numerica ( 1<n<64)
def dec_to_cualquier_base(n, b):
    n = int(n)
    new_number = []
    base_nueva = ""
    if b == 1:
        base_nueva += "1" * n #Caso que sea unario!!
    else:
        while(n != 0): #Si es 0, ya no hay numero al que buscar resto
            new_number.append(str(n % b))
            n = n // b
        new_number.reverse() #Lo ordenamos de atrás hacia adelante
        for pos in range(len(new_number)): #Buscamos el valor en la posicion correspondiente.
            base_nueva += bases_posibles[int(new_number[pos])]
    return base_nueva
    #Si retorno base_nueva, me trae el valor directamente basado en la lista de bases posibles. ej(1e23d)


#Función que pasa un decimal a bcd
def dec_to_bcd(n):
    n = int(n)
    if (n == 0):  # Caso borde donde n es igual a 0
        print("0000")
        return
    rev = 0  # Guardaremos aquí, el reverse de los valores que obtengamos.
    while (n > 0):
        rev = rev * 10 + (n % 10)
        n = n // 10
  # Iteramos los valores en el reverse.
    a=""
    while (rev > 0):
    # Se busca el binario para cada dígito usando bitset
        b = str(rev % 10)

    # Se imprime la conversión a binario para el digito correspondiente
        a = a + "{0:04b}".format(int(b, 16))
    # Se divide en 10, para usar el proximo dígito.
        rev = rev // 10
    return a

#Función que pasa un decimal a exceso de 3
def dec_to_ed3(valor):  #Aumento de 3!
    valor = str(valor)
    ed3 = 0
    for i in valor:
        d = int(i)+3  #A cada valor se le suma 3, y se pasa a binario.
        ed3 = ed3 + int(dec_to_binary(d))
    return ed3

def xor_c(a, b): #Función para concatenar
    return '0' if (a == b) else '1'

def get_gray(n): #Lista con los valores de la tabla de gray, acorde al largo n del valor que se inserta.
    if n == 0:
        return ['']
    first_half = get_gray(n - 1)
    second_half = first_half.copy()

    first_half = ['0' + code for code in first_half]
    second_half = ['1' + code for code in reversed(second_half)]

    return first_half + second_half

#Función que recibe un binario y lo retorna en codigo johnson
def johnson(valor):
    list = []
    lista2 = []
    a = cualquier_base_to_dec(valor,2)
    for i in range(10000): #Un rango muy largo solo para buscar el numero.
        if int(a)<2**i:
            break
    flag=True
    while flag:
        if len(list)==2**i:
            flag=False
        else:
            if list == []:
                b = "0" * ((2**i)//2)
                list.append(b)
            elif "1"* ((2**i)//2) not in list: #Mitad de la tabla, caso cuando son todos los valores equivalente a 1 (1111 o 11111111)
                b = b.replace("0", "1", 1) #Reemplazamos por 1 primero
                c = b[::-1]
                lista2.append(c)
                list.append(lista2[0])
                lista2 = []
            else:
                b = b.replace("1", "0", 1) #Se reemplazan por 0.
                c = b[::-1]
                lista2.append(c)
                list.append(lista2[0])
                lista2 = []
    return list[int(a)]

def paridad(valor):  #Caso cuando t es igual a par!
    valor = str(valor)
    a=0
    list=[]
    for i in valor:
        list.append(int(i))
    if list.count(1) % 2 ==0: #Si hay cantidad par de 1's, se debe retornar un 0. Si es impar, retornamos 1.
        return a+1
    else:
        return a

def pentaBit (valor):  #Caso cuando t es igual a pentabit!
    valor = str(valor)
    a = len(valor)
    if a % 5 ==0:
        return 1
    else:
        return 0

#Funcion que recibe un binario, y nos dice si tiene algun error o no.
def hamming(n):
    n = str(n)
    d = n
    data = list(d)
    data.reverse()
    c, ch, j, r, error, h, parity_list, h_copy = 0, 0, 0, 0, 0, [], [], []
    for k in range(0, len(data)): #Calcular los bits no redundantes
        p = (2 ** c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if (p == (k + 1)):
            c = c + 1
    for parity in range(0, (len(h))): #Determinar los bits de paridad
        ph = (2 ** ch)
        if (ph == (parity + 1)):
            startIndex = ph - 1
            i = startIndex
            toXor = []
            while (i < len(h)):
                block = h[i:i + ph]
                toXor.extend(block) #A la lista toXor le agrega la lista block
                i += 2 * ph
            for z in range(1, len(toXor)):
                h[startIndex] = h[startIndex] ^ toXor[z]
            parity_list.append(h[parity])
            ch += 1
    parity_list.reverse() #Lista con la paridad ordenada
    error = sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
    if ((error) >= len(h_copy)): #Se comparan los valores de error con h.copy, si error es más grande, no se sabe donde esta el error.
        return 0    #No se detecta el error
    else: #Si h_copy es más grande que error, podemos buscar donde está el error y cambiarlo.
        if (h_copy[error - 1] == '0'):
            h_copy[error - 1] = '1'

        elif (h_copy[error - 1] == '1'):
            h_copy[error - 1] = '0'
        h_copy.reverse()
        return (int(''.join(map(str, h_copy))))

while True:  #Debemos revisar todas las entradas, es requisito. Si sale un "-", se acaba el programa! Si la entrada es inválida, el programa se acaba.
    entrada = input("")
    if entrada=="-":
        print("Fin del programa")
        break
    entrada = entrada.split()  #Si entra al while, aplicamos split para separarlo en una lista de strings correspondientes. ["n", "b", "t"]

  #Revisar casos! Si b es numero o codigo
    #caso de entrada de b

    if entrada[1].isnumeric():  #.isnumeric() nos revisa si el string ingresado tiene valores numericos.
        if int(entrada[1])>=1 and int(entrada[1])<=64:   # Revisar si el valor de t es numerico (cumplir 1<=b<= 64)
            b = int(entrada[1])  #Se deja como entero porque es un numero
        else:
            print("Entrada inválida") #Se printea entrada invalida y vuelve a empezar el while. (Continue hace esto!)
            continue
    else:
        if entrada[1] in codigos:
            b = entrada[1]
        else:
            print("Entrada inválida")  #Se printea entrada invalida y vuelve a empezar el while. (Continue hace esto!)
            continue
    #Caso de entrada de t
    if entrada[2].isnumeric():
        if int(entrada[2]) >= 1 and int(entrada[2]) <= 64:
            t= int(entrada[2])
        else:
            print("Entrada inválida") #Se printea entrada invalida y vuelve a empezar el while. (Continue hace esto!)
            continue
    else:
        if entrada[2] in codigos:  # Revisar si el valor de t es numerico (cumplir 1<=t<= 64) o si está en códigos.
            t = entrada[2]
        else:
            print("Entrada inválida") #Se printea entrada invalida y vuelve a empezar el while. (Continue hace esto!)
            continue
    #Ya sabemos b, ahora podemos revisar n
    if str(b).isnumeric(): #Si es un valor númerico
        if entrada[0].isnumeric():
            if int(cualquier_base_to_dec(entrada[0],b)) >=1 and int(cualquier_base_to_dec(entrada[0],b)) <= 1000:  #Tiene que estar en base 10 y 1<=n<=1000.
                n = int(entrada[0])
            else:
                print("Entrada inválida")  # Se printea entrada invalida y vuelve a empezar el while. (Continue hace esto!)
                continue
        elif cualquier_base_to_dec(entrada[0],b) >=1 and cualquier_base_to_dec(entrada[0],b) <= 1000:
            n= entrada[0]
        else:
            print("Entrada inválida") #Se printea entrada invalida y vuelve a empezar el while. (Continue hace esto!)
            continue
    else: #Si b es codigo, dejaremos la base = 2. (Binaria)
        if es_binario(entrada[0]):
            b = 2
            if cualquier_base_to_dec(entrada[0], b) >= 1 and cualquier_base_to_dec(entrada[0],b) <= 1000:  # Tiene que estar en base 10 y 1<=n<=1000.
                n = entrada[0]
        else:
            print("Entrada inválida")  # Se printea entrada invalida y vuelve a empezar el while. (Continue hace esto!)
            continue

  #Si pasamos lo anterior, se tienen los valores de n, b y t.
    if b==t:
        if str(b).isnumeric():
            print("Base",b,":",n)
        else:
            print("Codigo", b, ":", n)
    elif str(b).isnumeric() and str(t).isnumeric():
        n = cualquier_base_to_dec(n,b)
        n = dec_to_cualquier_base(n,t)
        print("Base",t,":",n)
    elif t=="bcd":
        n = cualquier_base_to_dec(n,b)
        n = dec_to_bcd(n)
        print("Codigo BCD:",n)
    elif t == "gry":
        if es_binario(n):
            codes = get_gray(len(str(n)))
            print("Codigo Gray:",dec_to_binary(codes.index(str(n))))
        else:
            num = n
            num = cualquier_base_to_dec(n,b)
            num = dec_to_binary(num)
            codes = get_gray(len(num))
            print("Codigo Gray:", dec_to_binary(codes.index(num)))
    elif t=="ed3":
        n = cualquier_base_to_dec(n,b)
        print("Codigo Exceso de 3:", dec_to_ed3(n))
    elif t=="jsn":
        if es_binario(n):
            print("Codigo Johnson:",johnson(n))
        else:
            n= cualquier_base_to_dec(n,b)
            n= dec_to_binary(n)
            print("Codigo Johnson:",johnson(n))
    elif t =="par":
        if es_binario(n):
            print("Codigo Paridad:",paridad(n))
        else:
            n = cualquier_base_to_dec(n,b)
            n = dec_to_binary(n)
            print("Codigo Paridad:", paridad(n))
    elif t =="pbt":
        if es_binario(n):
            print("Código Pentabit:", pentaBit(n))
        else:
            n = cualquier_base_to_dec(n,b)
            n=dec_to_binary(n)
            print("Código Pentabit:", pentaBit(n))
    else:
        if es_binario(n):
            print("Codigo Hamming:",hamming(n))
        else:
            n = cualquier_base_to_dec(n, b)
            n = dec_to_binary(n)
            print("Codigo Hamming:", hamming(n))