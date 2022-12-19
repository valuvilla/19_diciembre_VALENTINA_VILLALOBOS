from ast import main
import re




def is_nessie_here():
    text = input("Enter text: ")
    if re.search(r'tree fiddy' or 'three fifty' or '3.50', text) is not None:
        return "Estamos hablanco con el monstruo de Loch Ness"

#probamos el codigo
print(is_nessie_here())

if __name__ == '__main__':
    main()