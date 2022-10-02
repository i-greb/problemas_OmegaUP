""""Cada vez que Nicolás y su mamá van a hacer las compras, el niño exige que se le compren  juguetes. 
Normalmente termina ocurriendo, pero esta vez, la madre se puso firme y le dijo a Nicolás que no le comprará  juguetes, 
sino solamente . Es decir, si siempre le compraba  juguetes, esta vez le compraría solo .

Nicolás está en una situación difícil y necesita conseguir la mayor diversión posible. Cada juguete tiene un nivel de 
diversión y la diversión final es la suma de los niveles de diversión de los juguetes adquiridos. 
Tu trabajo es conseguir la mayor diversión posible."""""

"entrada:5" \
"niveles de diversión (entradas): 8,5,3,6,8 "
def _main() -> None:
    n= int(input())
    maydiv=0
    lista_diversion = []
    for x in range(0, n):
        lista_diversion.append(int(input()))

    lista_diversion.sort()
    print(lista_diversion)

    for x in range (1,len(lista_diversion)):
        maydiv += lista_diversion[x]

    print (maydiv)

if __name__ == '__main__':
    _main()
