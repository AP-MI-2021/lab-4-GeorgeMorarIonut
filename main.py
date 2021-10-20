def citireLista():
    lst = []
    n = int(input("Dati nr de elemente din lista: "))
    for i in range(n):
        lst.append(int(input("l[" + str(i) + "]= ")))
    return lst


def afisareNumereNegativeNenule(lst):
    """
    Determina numerele negative, nenule dintr-o lista de numere intregi.
    :param lst: o lista de numere intregi
    :return: numerele negative, nenule dintr-o lista de numere intregi
    """
    rezultat = []
    for i in lst:
        if i < 0:
            rezultat.append(i)
    return rezultat


def testAfisareNumereNegativeNenule():
    assert afisareNumereNegativeNenule([]) == []
    assert afisareNumereNegativeNenule([23, 0, -2, 98, -87, -9889]) == [-2, -87, -9889]
    assert afisareNumereNegativeNenule([23, 45, 6, 4, 0]) == []


def smallestLastDigit(lst, k):
    """
    Determina cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    :param lst: o lista de numere intregi
    :param k: un numar intreg
    :return: cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură sau None in
    cazul in care nu exista.
    """
    minim = None
    for element in lst:
        if element % 10 == k and (minim is None or element < minim):
            minim = element
    return minim


def testSmallestLastDigit():
    assert smallestLastDigit([1, 6, 34, 68, 40, 48, 20], 8) == 48
    assert smallestLastDigit([8, 76, 90, 88, 18], 8) == 8
    assert smallestLastDigit([98, 76, 5, 76, 131, 87], 9) is None


def isPrime(nr):
    """
    Determina daca un numa este prim.
    :param nr: un nr intreg
    :return: True daca numarul este prim sau false in caz contrar
    """
    if nr < 2:
        return False
    for i in range(2, nr // 2 + 1):
        if nr % i == 0:
            return False
    return True


def testIsPrime():
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(19) is True


def isSuperprime(nr):
    """
    Determina daca un numar este superprim.
    :param nr: nr intreg
    :return: True daca numarul este superprim sau False in caz contrar.
    """
    while nr > 0:
        if not isPrime(nr):
            return False
        nr = nr // 10
    return True


def testIsSuperprime():
    assert isSuperprime(239) is True
    assert isSuperprime(373) is True
    assert isSuperprime(100) is False


def numereSuperPrime(lst):
    """
    Afiseaza numerele superprime dintr-o lista.
    :param lst: o lista de numere intregi
    :return: numerele superprime dintr-o lista
    """
    rezultat = []
    for i in lst:
        if isSuperprime(i):
            rezultat.append(i)
    return rezultat


def testNumereSuperPrime():
    assert numereSuperPrime([]) == []
    assert numereSuperPrime([23, 239, 12, 90, 373, 20]) == [23, 239, 373]
    assert numereSuperPrime([42, 87, 94, 88, 32]) == []

def celMaiMareDivCom(nr1 ,nr2):
    """
    Determina cel mai mare divizor comun dintre doua numere.
    :param nr1: numar intreg
    :param nr2: numar intreg
    :return: cel mai mare divizor comun dintre doua numere
    """
    if nr1 == 0:
        if nr2 == 0:
            return -9999
        else:
            return nr2
    else:
        while nr2 != 0:
            r = nr1 % nr2
            nr1 = nr2
            nr2 = r
        return nr1

def testCelMaiMareDivCom():
    assert celMaiMareDivCom(12, 144) == 12
    assert celMaiMareDivCom(6, 12) == 6
    assert celMaiMareDivCom(24, 16) == 8


def cmmdcNumerePozitive(lst):
    """
    Determina cmmdc-ul numerelor pozitive dintr-o lista.
    :param lst: o lista de numere
    :return: cmmdc-ul numerelor pozitive dintr-o lista
    """
    cmmdc = 0
    for i in lst:
        if i > 0:
            cmmdc = celMaiMareDivCom(cmmdc, i)
    return cmmdc

def testCmmdcNumerePozitive():
    assert cmmdcNumerePozitive([-2, 24, 4, 13, -16, 12]) == 1
    assert cmmdcNumerePozitive([6, 12, -3, 4, 3]) == 1
    assert cmmdcNumerePozitive([-76, 12, 24, -13, 144]) == 12


def inversSiCmmdc(lst):
    """
    Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    :param lst: o lista de numere
    :return:lista obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă
    """
    rezultat = []
    for i in lst:
        if i > 0:
            rezultat.append(cmmdcNumerePozitive(lst))
        elif i <= 0:
            iStr = str(i)
            x = iStr.split("-")[1]
            x = x[::-1]
            x = int(x)
            x = 0 - x
            rezultat.append(x)
    return rezultat


def testInversSiCmmdc():
    assert inversSiCmmdc([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]
    assert inversSiCmmdc([12, 4, -87, -34, 16]) == [4, 4, -78, -43, 4]
    assert inversSiCmmdc([]) == []


def testAll():
    testAfisareNumereNegativeNenule()
    testSmallestLastDigit()
    testIsPrime()
    testIsSuperprime()
    testNumereSuperPrime()
    testCelMaiMareDivCom()
    testCmmdcNumerePozitive()
    testInversSiCmmdc()


def main():

    lst = [12, -2, 24]
    testAll()


    while True:
        print("1. Citire")
        print("a. Show all")
        print("2. Afiseaza numerele negative din lista citita.")
        print("3. Afiseaza cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură")
        print("4. Afișarea tuturor numerelor din listă care sunt superprime.")
        print("5. Ex 5")
        print("x. Iesire")


        optiune = input("Dati optiune: ")
        if optiune == "1":
            lst = citireLista()
        elif optiune == "a":
            print(lst)
        elif optiune == "2":
            print(afisareNumereNegativeNenule(lst))
        elif optiune == "3":
            k = int(input("Dati valoarea lui k: "))
            print(smallestLastDigit(lst, k))
        elif optiune == "4":
            print(numereSuperPrime(lst))
        elif optiune == "5":
            print(inversSiCmmdc(lst))
        elif optiune == "x":
           break
        else:
           print("Optiune gresita! Selectati alta optiune!")



if __name__ == '__main__':
    main()