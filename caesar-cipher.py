# coding=utf-8
import sys, getopt
from string import ascii_lowercase
from collections import Counter

##----TODO-------
#
#tener la BD de los idiomas y sus letras más comunes
#analizar la corresondencia para determinar el idioma
#encriptar pasando por parámetro el cambio
#
##--------------

inputfile = ''
outputfile = ''
metodo = ''

def decrypt(reemplazar,escribir):
    with open(reemplazar) as f:
        c = Counter(letter for line in f 
            for letter in line.lower() 
                if letter in ascii_lowercase)
        letra = ''
        repeticion = 0
        for letter, repetitions in c.iteritems():
            if repeticion < repetitions:
                repeticion = repetitions
                letra = letter
        letrascii = ord(letra)
        print 'la letra que mas se repite es %s', letra
        diferencia = ord('e')-ord(letra) #se supone idioma ingles
        
        archivo = open(escribir,"w")
        
        with open(reemplazar) as fileobj:
            for line in fileobj:  
                for ch in line: 
                    letrascii = ord(ch)
                    valorsincodificar = 0
                    if letrascii < (97-diferencia):
                        valorsincodificar = letrascii + 26 + diferencia
                    else:
                        valorsincodificar = letrascii + diferencia
                    letra2 = chr(valorsincodificar)
                    archivo.write(letra2)
        archivo.close()
        print 'Status : COMPLETED'

def main(argv):

    try:
        opts, args = getopt.getopt(argv, "hi:o:cd", ["ifile=","ofile="])
    except getopt.GetoptError:
        print 'cryptography-caesar-cipher.py -<metodo> -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'cryptography-caesar-cipher.py -<metodo> -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt == "-c":
            metodo = 'crypt'
        elif opt == "-d":
            metodo = 'decrypt'
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if metodo == 'decrypt':
        decrypt(inputfile,outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
