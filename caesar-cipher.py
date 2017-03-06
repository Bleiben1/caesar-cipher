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
    letra = ''
    diferencia = 0

    with open(reemplazar) as f:
        c = Counter(letter for line in f 
            for letter in line.lower() 
                if letter in ascii_lowercase)
        repeticion = 0
        for letter, repetitions in c.iteritems():
            if repeticion < repetitions:
                repeticion = repetitions
                letra = letter
        letrascii = ord(letra)
        print 'The letter %s is the most common with %s reps.' % (letra, repeticion)
        diferencia = ord('e')-ord(letra) #se supone idioma ingles por ahora

        result = ''

        with open(reemplazar) as fileobj:
            for line in fileobj:
                for ch in line:
                    letrascii = ord(ch)
                    valorsincodificar = 0
                    if letrascii < (97-diferencia):
                        valorsincodificar = letrascii + 26 + diferencia
                    else:
                        valorsincodificar = letrascii + diferencia
                    letra = chr(valorsincodificar)
                    result = result + letra
 
        if escribir == 'console':
            print result
        else:
            archivo = open(escribir,"w")
            archivo.write(result)
            archivo.close()
            print 'Status : COMPLETED'
        
def main(argv):

    try:
        opts, args = getopt.getopt(argv, "hi:o:cd", ["ifile=","ofile="])
    except getopt.GetoptError:
        print """
Usage : cryptography-caesar-cipher.py -<metodo> -i <inputfile> -o <outputfile>
            
Options : 
     <method> : -> -d  allow to give an encripted message as an input and give a readable output
                -> -c  allow to give clear or readable text file and return a encrypted output
         
     <inputfile> : indicate the input file with the message that would be the target for the method selected
         
     <outputfile> : indicate the output file where would be stored the message.
                   -o console : allow to print the message on the terminal without saving.
            """
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print """
Usage : cryptography-caesar-cipher.py -<metodo> -i <inputfile> -o <outputfile>
            
Options : 
     <method> : -> -d  allow to give an encripted message as an input and give a readable output
                -> -c  allow to give clear or readable text file and return a encrypted output
         
     <inputfile> : indicate the input file with the message that would be the target for the method selected
         
     <outputfile> : indicate the output file where would be stored the message.
                   -o console : allow to print the message on the terminal without saving.
            """
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
