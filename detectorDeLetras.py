def _leerInput():
    entrada = input()
    aLetras = entrada.split(" ")
    return aLetras

def _main()-> None:
     entrada = _leerInput()
     contador= 0
     for x in entrada:
         cAscii=ord(x)
         if (cAscii>=65 and cAscii <=90):
             if (cAscii == 65 or cAscii == 69 or cAscii == 73 or cAscii== 79 or cAscii==85):
                 print("V", end=" ")
                 contador +=1
             elif (cAscii==89):
                 print("S", end=" ")
                 contador += 1
             else:
                 print("C", end=" ")
                 contador += 1
         if contador== 10:
            break



if __name__ == '__main__':
    _main()
