import re
from typing_extensions import runtime_checkable

#parte grafica es obligatoria?


#TENER LISTO:
#LOGICA Y LEXICO
#Compilador, Lexico, Semantico, Grafico, Manual
#convertir tokens a objetos en si
#mostrar fila y columna de error

class node:#data,type,next,under,upper
    def __init__(self,data=None, type=None, next=None, under=None, upper=None):
        self.data = data
        self.type = type
        self.next = next
        self.under = under
        self.upper = upper
class vari:#type, next, data, data2
    def __init__(self, type=None, next=None, data=None, data2=None):
        self.type = str(type)
        self.next = next
        self.data = data
        self.data2 = data2
class list:
    def __init__(self, command = None):
        self.head = None
        self.command = command

    def head(self):
        return self.head

    def append(self, data, dire):
        if self.head == None:
            self.head = node(data)
        else:
            new_node = node(data)
            cur = self.head
            while cur.next != None and cur.under != None and cur.upper != None:
                if cur.next != None:
                    cur = cur.next
                if cur.under != None:
                    cur = cur.under
                if cur.upper != None:
                    cur = cur.upper
            if dire == "next":
                cur.next = new_node
            elif dire == "under":
                cur.under = new_node
            elif dire == "upper":
                cur.upper = new_node
#tokens = vector de nodos
def tokenizer (input):# COMPLETO convierte a tokens:(){}[] : = , . " + grupos de(A-Z) y (0-9)
    current = 0
    tokens = []
    alphabet = re.compile(r"[a-z]", re.I)#l m a o   e k s d e e
    numbers = re.compile(r"[0-9]")
    whiteSpace = re.compile(r"\s")
    while current < len(input):#divide todo en conjuntos, ignora espacios
        char = input[current]
        if re.match(whiteSpace, char):#ignora espacios
            current = current + 1
            continue
        if char == "(":
            tokens.append(node("(","Lparen"))
            current = current + 1
            continue
        if char == ")":
            tokens.append(node(")","Rparen"))
            current = current + 1
            continue
        if char == "{":
            tokens.append(node("{","Lllav"))
            current = current + 1
            continue
        if char == "}":
            tokens.append(node("}","Rllav"))
            current = current + 1
            continue
        if char == "[":
            tokens.append(node("[","Lcorch"))
            current = current + 1
            continue
        if char == "]":
            tokens.append(node("]","Rcorch"))
            current = current + 1
            continue
        if char == ",":
            tokens.append(node(",","coma"))
            current = current + 1
            continue
        if char == "+":# + y += aca
            if input[(current + 1)] == "=":
                tokens.append(node("+=","masIgu"))
                current = current + 2
            else:
                tokens.append(node("+","mas"))
                current = current + 1
            continue     
        if char == ":":
            tokens.append(node(":","dospun"))
            current = current + 1
            continue
        if char == ".":#.islower y .upper aca
            if input[(current + 1)] == "i" and input[(current + 2)] == "s" and input[(current + 3)] == "l" and input[(current + 4)] == "o" and input[(current + 5)] == "w" and input[(current + 6)] == "e" and input[(current + 7)] == "r":
                tokens.append(node(".islower","isLower"))
                current = current + 8
                continue
            elif input[(current + 1)] == "u" and input[(current + 2)] == "p" and input[(current + 3)] == "p" and input[(current + 4)] == "e" and input[(current + 5)] == "r":
                tokens.append(node(".upper","Upper"))
                current = current + 6
                continue
        if char == "\"":#todos los strings como "TEXTO"
            text = ""
            current = current +1
            while current < len(input) and input[current] != "\"":
                text += input[current]
                current = current + 1
                if(input[current] != "\""):
                     text += " "
            text += "\""
            tokens.append(node(text, "cita"))
            current = current + 1
            continue
        if char == "=":
            tokens.append(node("=","igual"))
            current = current + 1
            continue
        if char == "!" and input[(current + 1)] == "=":#!= aca
            tokens.append(node("!=","dif"))
            current = current + 2
            continue
        if re.match(alphabet, char) or re.match(numbers, char):#secuencia de letras y/o numeros
            text = ""
            while current < len(input):
                if re.match(alphabet, input[current]) or re.match(numbers, input[current]):
                    text += input[current]
                    current = current + 1
            tokens.append(node(text, "text"))
            continue
        if char == "-":#ENTER
            tokens.append(node("-","enter"))
            current = current + 1
            continue
        raise ValueError("digit not understood by compiler: " + char)#error
    return tokens#devuelve la secuencia de tokens divididos
#lista = secuencia serpenteante de nodos
def leveler (tokens):# lee todos los nodos y crea una lista serpenteante
    def keys(node):
        while node.next != None:
            node = node.next
        if node.upper != None:
            return node.upper
        else:
            node.next = keys(node.under)

    current = 0
    cont = 0
    lista = list()
    while current < len(tokens):
        if tokens[current].data == "{":
            lista.append(tokens[current],"under")
            cont -= 1
        elif tokens[current] == "}":
            lista.append(tokens[current],"upper")
            cont += 1
        else:
            lista.append(tokens[current],"next")
        current = current + 1
    if cont < 0:
        print("ERROR: falta cerrar llaves")
    elif cont > 0:
        print("ERROR: falta abrir llaves")
    else:
        keys(node.head)
        return lista

def traverser(lista):
    def op1(supdic, aux):# 1 dict = {   }
        dict = {}
        check = True
        while aux.data != "}" and check:
            if aux.data == None or aux.next.data != ":" or aux.next.next.data == None or aux.next.next.next.data != ";":
                print ("Error: directorio no formulado completamente")
                check = False
            else:
                if aux.type == "text":
                    a = supdic[aux.data]
                else:
                    a = aux.data
                aux = aux.next.next
                if aux.type == "text":
                    b = supdic[aux.data]
                else:
                    b = aux.data
                if a == None or b == None:
                    print ("Error: directorio no pudo completar con los 2 textos dados")
                else:
                    dict[a] = [b]
                    aux = aux.next.next
        aux = aux.upper
        v = vari("1", aux, dict)
        return v
    def op2(supdic, aux):#2 x = y
        if(aux.next.next.type == "cita" or aux.next.next.type == "cita"):
            asign = aux.next.next.data
        elif(aux.next.next.type == "text"):
            asign = supdic[aux.next.next.data]
        else:
            print("Error: no sabe que asignar")
        v = vari("2", aux.next.next.next, asign, aux.next.next.data)
        return v
    def op3(supdic, aux):#3 x += y
        xx = aux.data
        texti = ""
        aux = aux.next.next
        while aux.data != "-":
            if(aux.type == "cita"):
                texti += aux.data
                aux = aux.next
            elif(aux.type == "text"):
                texti += supdic[aux.data]
                aux = aux.next
            elif(aux.data == "+"):
                aux = aux.next
            else:
                print("Error: no termino la cadena")
        v = vari("3", aux, xx, texti)
        return v
    def op4(supdic, aux):#4) return
        if(aux.next.type == "cita"):
            asign = aux.next.data
        elif(aux.next.type == "text"):
            asign = supdic[aux.next.data]
        else:
            print("Error: no puede retornar eso")
        v = vari("4", aux.next.next, asign)
        return v
    def op5(supdic, aux):#5) print
        if(aux.next.next.type == "cita" and aux.next.next.next.data == ")"):
            asign = aux.next.next.data
        elif(aux.next.next.type == "text" and aux.next.next.next.data == ")"):
            asign = supdic[aux.next.next.data]
        else:
            print("Error: no puede imprimir eso")
        v = vari("5", aux.next.next.next.next, asign)
        return v
    def op6(supdic, aux):#6) while SKIPPED
        aux = aux.next.next
        if aux.type == "text" and (aux.next.data == "=" or aux.next.data == "!=") and aux.next.next.type == "text" and aux.next.next.next.data == ")" and aux.next.next.next.next.data == "{":
            while(aux.data != "}"):
                print("eliminar esto")
            aux = aux.next.next.next.next.next
        else:
            print("Error: while no formulado correctamente")
        '''def op7(supdic, aux):
        for aux.next.next.data in aux.next.next.next.next.data:
            print("lol")'''
    def op7(supdic, aux):#7) for TEXT in TEXT {   } SKIPPED R E D O
        aux = aux.next.next.next.next.next.under
        while aux.data != "}" and check:
            if aux.type == "text" and aux.next.data == ":" and aux.next.next.type == "text" and aux.next.next.next == ",":
                dict(aux.data) = aux.next.next.data
                aux = aux.next.next.next.next
            else:
                print ("Error: ")
                check = True
    def op8(supdic, aux):#8) def code (){   } SKIPPED
        aux = aux.next.next.next.next.next.under
        while aux.data != "}" and check:
            if aux.type == "text" and aux.next.data == ":" and aux.next.next.type == "text" and aux.next.next.next == ",":
                dict(aux.data) = aux.next.next.data
                aux = aux.next.next.next.next
            else:
                print ("Error: ")
                check = True
    def lector(lista):
        supdic = {}
        aux = lista.head
        va = vari()
        vh = vari()
        line = 0
        while aux != None:
            print(aux.data)
            if(aux.type == "text"):
                #1 dict = {   }
                if aux.data.lower() == "dict" and aux.next.data == "=" and aux.next.next.data == "{":
                    v = op1(supdic, aux.next.next.under)
                #2 x = y
                elif aux.type == "text" and aux.next.data == "=" and aux.next.next.type == "text":
                    v = op2(supdic, aux)
                #3 x += y
                elif aux.type == "text" and aux.next.data == "+=" and aux.next.next.type == "text":
                    v = op3(supdic, aux)
                #4) return
                elif aux.data.lower() == "return":
                    v = op4(supdic, aux)
                #5) print
                elif aux.data.lower() == "print" and aux.next.data == "(":
                    v = op5(supdic, aux)
                #6) while SKIPPED
                elif aux.data.lower() == "while" and aux.next.data == "(":
                    v = op6(supdic, aux)
                #7) for TEXT in TEXT {   } SKIPPED
                elif aux.data.lower() == "for" and aux.next.data == "(" and aux.next.next.type == "text" and aux.next.next.next.type == "in" and aux.next.next.next.type == "text" and aux.next.next.next.type == ")" and aux.next.next.next.next.type == "{":
                    v = op7(supdic, aux)
                #8) def code (){   } SKIPPED
                elif aux.data.lower() == "def" and aux.next.type == "text" and aux.next.next.data == "(" and aux.next.next.next.type == "text" and aux.next.next.next.next.data == ")" and aux.next.next.next.next.next.data == "{":
                    v = op8(supdic, aux)
                #ninguno de los anteriores
                else:
                    print("wtf es esto?: " + aux.data)
            elif aux.data == "-":
                line += 1
                aux = aux.next
            else:
                print("Error: no es texto: " + aux.data)
            if vh.data == None:
                vh = v
                va = vh
            else:
                va.next = v
                va = v
        return vh
    return lector(lista)

def generator(vh):
    aux = vh
    while aux != None:
        print("lol")
        aux = aux.next
    return "output"

def compiler(input):#usa todo y retorna el resultado en string
    tokens = tokenizer(input)
    lista = leveler(tokens)
    vh = traverser(lista)
    output = generator(vh)
    return output

def main():# COMPLETO
    input = "banana"
    output = compiler(input)
    #print(output)

if __name__ == "__main__":# COMPLETO
    main()
