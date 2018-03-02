import sys
import string

#print("Podaj jakiś tekst")
#s=sys.stdin.readline() #Wczytuje wiersz
#print("Twój tekst to: "+"coś"+s)


#zadanie 1
#tekst = input("napisz cokolwiek\n")
#print("ilość spacji: " + str(tekst.count(" ")))

#zadanie 2
#print("podaj dwie liczby")
#a=sys.stdin.readline()
#x,y=a.split(" ")
#x1=int(x)
#y1=int(y)
#sys.stdout.write(str(x1*y1))

#zadanie 4
#a=int(input("daj mje liczbe\n"))
#if a<0:
    #print("wartość bezwzględna: "+str(-a))
#else:
    #print("wartość bezwzględna: "+str(a))


#zadanie 5
#print("podaj trzy liczby")
#a=sys.stdin.readline()
#x1,y1,z1=a.split(" ")
#x=int(x1)
#y=int(y1)
#z=int(z1)
#if x>0 and x<11:
    #if x>y or y>z:
        #print("dobrze marian")
    #else:
        #print("no nie bardzo")
#else:
    #print("no nie bardzo")


#zadanie 6
#lista=[10,15,1235,2346,12356,256,537]
#for i in lista:
    #if i % 5 == 0:
        #print(str(i)+" jest podzielne przez 5")


#zadanie 7
#for i in range(1,6,1):
    #int(input("\ndej mje numer\n"))
    #print(a*a)

#zadanie 8
#lista=[]
#i = 0
#while i < 6:
    #lista.append(input("liczba: \n"))
    #i = i+1
#print(lista)


#zadanie 9
#i=0
#suma=int(0)
#x=input("liczba:\n")
#while i < len(x):
    #czynnik = int(x[i])
    #suma = suma + czynnik
    #i=i+1
#print(suma)


#zadanie 10
#a=int(input("podaj wysokość wieży\n"))
#if a < 11:
    #for i in range(1,a + 1,1):
        #for j in range(1,i + 1,1):
            #sys.stdout.write("A")
        #print()


#zadanie 11
a=int(input("podaj wysokość wieży\n"))
b=int(a//2)
if a < 10 and a > 3:
    for i in range(1,(a+1)*2,2):
        if i < b+1:
            sys.stdout.write("a")
        else:
            if i == b+1:
                for j in range(1,a+1,1):
                    sys.stdout.write("a")
        print()
