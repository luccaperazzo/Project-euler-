file_path = r"C:\Users\Usuario\Desktop\0022_names.txt"

try:
    with open(file_path, "r") as file:
        file_contents = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print("An error occurred:", e)



def posicion(letra):
    letra = letra.upper()
    code_point = ord(letra)
    position = code_point - ord('A') + 1
    return position

def name_value(name):
    return sum(posicion(letter) for letter in name)


lista1 = file_contents.split(",")
lista2 = [name.strip('"') for name in lista1]
ordenada = sorted(lista2)
listasuma = []
cont = 1
for i in range(len(ordenada)):
    valor = name_value(ordenada[i])
    listasuma.append(valor*cont)
    cont += 1
    
print(sum(listasuma))
        