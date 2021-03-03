import math
import queue
import numpy as np


# ~~~~~~~~~~ P1 ~~~~~~~~~~
def solve_p1():
    text = input("Text: ")
    print(last_word(text))


def last_word(text):
    """
    Determina ultimul cuvant dpdv alfabetic dintr-un text
    :param text: string
    :return: string - ultimul cuvant
    """
    if text == "":
        return ""
    split = text.split(" ")
    last = split[0]
    for word in split:
        if word > last:
            last = word
    return last


# ~~~~~~~~~~ P2 ~~~~~~~~~~
def solve_p2():
    ax = int(input("aX = "))
    ay = int(input("aY = "))
    bx = int(input("bX = "))
    by = int(input("bY = "))
    print("Distanta: " + str(distanta(ax, ay, bx, by)))


def distanta(ax, ay, bx, by):
    """
    Returneaza distanta euclidiana dintre 2 puncte
    :param ax: integer
    :param ay: integer
    :param bx: integer
    :param by: integer
    :return: integer - distanta euclidiana
    """
    sx = bx - ax
    sy = by - ay
    return math.sqrt(sx * sx + sy * sy)


# ~~~~~~~~~~ P3 ~~~~~~~~~~
def solve_p3():
    pass


# ~~~~~~~~~~ P4 ~~~~~~~~~~
def solve_p4():
    text = input("Text: ")
    for word in cuvinte_care_apar_o_data(text):
        print(word)


def cuvinte_care_apar_o_data(text):
    """
    Returneaza o lista care contine cuvintele care apar o singura data intr-un text
    :param text: String
    :return: list[string] - cuvintele care apar o singura data in text
    """
    split_text = text.split()
    fr = {}
    words = []
    for word in split_text:
        if word not in fr.keys():
            fr[word] = 1
        else:
            fr[word] += 1
    for key, value in fr.items():
        if value == 1:
            words.append(key)
    return words


# ~~~~~~~~~~ P5 ~~~~~~~~~~
def solve_p5():
    string_numbers = input("Numbers: ")
    numbers = []
    for number in string_numbers.split():
        numbers.append(number)
    print(repeated_value(numbers))


def repeated_value(numbers):
    """
    Returneaza valoarea se repeta dintre numerele din lista
    :param numbers: list[integer] - list of numbers
    :return: repeated value - integer
    """
    n = len(numbers)
    gauss_sum = ((n - 1) * n) // 2
    suma = 0
    for number in numbers:
        suma += int(number)
    return suma - gauss_sum


# ~~~~~~~~~~ P6 ~~~~~~~~~~
def solve_p6():
    text = input("Numbers: ")
    numbers = text.split()
    print(element_majoritar(numbers))


def element_majoritar(numbers):
    """
    Returneaza elementul majoritar dintr-o lista de numere
    :param numbers: list[integer] - lista cu numere
    :return: integer - elementul majoritar
             none - daca nu exista element majoritar
    """
    fr = {}
    n = len(numbers)
    for number in numbers:
        if number not in fr.keys():
            fr[number] = 1
        else:
            fr[number] += 1
    for key, value in fr.items():
        if value > n // 2:
            return key
    return None


# ~~~~~~~~~~ P7 ~~~~~~~~~~
def solve_p7():
    k = int(input("K = "))
    text = input("Numbers: ")
    numbers = text.split()
    print(k_element(k, numbers))


def binary_search(arr, left, right, x):
    """
    Returneaza pozitia pe care se gaseste x in lista ordonata sau pozitia anterioara pozitiei unde ar trebui adaugat
    in cazul in care nu exista
    :param arr: list[integer]
    :param right: integer
    :param left: integer
    :param x: integer
    :return: integer
    """
    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)

        return binary_search(arr, mid + 1, right, x)

    return left - 1


def k_element(k, numbers):
    """
    Returneaza al k-lea cel mai mare element din lista de numere
    :param k: integer
    :param numbers: list[integer]
    :return: integer
    """

    first_k = []
    for i in range(k):
        first_k.append(numbers[i])
    first_k.sort()

    for i in range(k, len(numbers)):
        if numbers[i] > first_k[k - 1]:
            first_k.pop(0)
            first_k.append(numbers[i])
        elif first_k[0] < numbers[i] < first_k[k - 1]:
            poz = binary_search(first_k, 0, len(first_k) - 1, numbers[i])
            first_k[poz] = numbers[i]
    return first_k[0]


# ~~~~~~~~~~ P8 ~~~~~~~~~~
def solve_p8():
    n = int(input("N = "))
    for binary_number in generate_binary(n):
        print(binary_number)


def generate_binary(n):
    """
    Returnreaza o lista de stringuri reprezentand numerele binare de la 1 la n
    :param n: integer
    :return: list[string] - lista de numere binare de la 1 la n
    """
    q = queue.Queue()
    q.put("1")

    binary_numbers = []

    while n > 0:
        n -= 1
        s1 = q.get()
        binary_numbers.append(s1)
        s2 = s1
        q.put(s1 + "0")
        q.put(s2 + "1")

    return binary_numbers


# ~~~~~~~~~~ P9 ~~~~~~~~~~
def solve_p9():
    m = int(input("Nr linii: "))
    n = int(input("Nr coloane: "))
    print("Matrice:")
    mat = [[int(input()) for x in range(n)] for y in range(m)]

    print("Input = x,y")
    p = (int(input("Px = ")), int(input("Py = ")))
    q = (int(input("Qx = ")), int(input("Qy = ")))
    r = (int(input("Rx = ")), int(input("Ry = ")))
    s = (int(input("Sx = ")), int(input("Sy = ")))
    rez = suma_submat(m, n, mat, p, q, r, s)
    print("Sum1 = ", rez[0])
    print("Sum2 = ", rez[1])


def partial_sum_mat(mat, m, n):
    """
    Returneaza matricea sumelor partiale
    :param mat: matricea data
    :param m: nr linii
    :param n: nr coloane
    :return: matricea sumelor partiale
    """
    # Copy first row of mat[][] to aux[][]

    aux = [[0 for col in range(n)] for row in range(m)]
    for i in range(0, n, 1):
        aux[0][i] = mat[0][i]

    # Do column wise sum
    for i in range(1, m, 1):
        for j in range(0, n, 1):
            aux[i][j] = mat[i][j] + aux[i - 1][j]

    # Do row wise sum
    for i in range(0, m, 1):
        for j in range(1, n, 1):
            aux[i][j] += aux[i][j - 1]

    return aux


def suma_submat(m, n, mat, p, q, r, s):
    """
    Returneaza un tuplu cu sumele calculate pentru fiecare submatrice definita de punctele date
    :param m: intger - nr de linii
    :param n: integer - nr de coloane
    :param mat: matricea data
    :param p: tuple - (px, py)
    :param q: tuple - (qx, qy)
    :param r: tuple - (rx, ry)
    :param s: tuple - (sx, sy)
    :return: tuple - (sum1, sum2) - tuplu cu suma din submatrice
    """
    aux = partial_sum_mat(mat, m, n)
    sum1 = suma_submat_aux(aux, p[0], p[1], q[0], q[1])
    sum2 = suma_submat_aux(aux, r[0], r[1], s[0], s[1])
    return sum1, sum2


def suma_submat_aux(aux, tli, tlj, rbi, rbj):
    res = aux[rbi][rbj]

    if tli > 0:
        res = res - aux[tli - 1][rbj]

    if tlj > 0:
        res = res - aux[rbi][tlj - 1]

    if tli > 0 and tlj > 0:
        res = res + aux[tli - 1][tlj - 1]

    return res


# ~~~~~~~~~~ P10 ~~~~~~~~~~
def solve_p10():
    m = int(input("Nr linii: "))
    n = int(input("Nr coloane: "))
    print("Matrice:")
    mat = [[int(input()) for x in range(n)] for y in range(m)]
    print(ones_on_line(mat, m, n))


def ones_on_line(mat, m, n):
    for j in range(1, n, 1):
        for i in range(0, m, 1):
            if mat[i][j] == 1:
                return i + 1


# ~~~~~~~~~~ P11 ~~~~~~~~~~
def solve_p11():
    m = int(input("Nr linii: "))
    n = int(input("Nr coloane: "))
    print("Matrice:")
    mat = [[int(input()) for x in range(n)] for y in range(m)]

    replace_zeroes(mat, m, n)

    for i in range(m):
        print(mat[i])


def is_safe(m, n, mat, x, y, target):
    """
    Verifica daca mat[x,y] poate fi parcurs
    :param m: integer
    :param n: integer
    :param mat: matricea
    :param x: integer
    :param y: integer
    :param target: integer
    :return: boolean - true daca mat[x,y] e safe de parcurs
                     - false altfel
    """
    return (0 <= x < m and 0 <= y < n) and mat[x][y] == target


# Flood fill using DFS
def flood_fill(m, n, mat, x, y, replacement, row, col):
    """
    Inlocuieste 0 cu -1 pe toate pozitiile matricei prin care poate trece (a[i]j] != 1) incepand din marginile matricei
    :param m: integer
    :param n: integer
    :param mat: matricea
    :param x: integer
    :param y: integer
    :param replacement: integer
    :param row: list - lista de optiuni pt parcurgere pe linii
    :param col: list - lista de optiuni pt parcurgere pe coloane
    :return: None
    """
    target = mat[x][y]

    mat[x][y] = replacement

    for k in range(4):
        if is_safe(m, n, mat, x + row[k], y + col[k], target):
            flood_fill(m, n, mat, x + row[k], y + col[k], replacement, row, col)


def replace_zeroes(mat, m, n):
    """
    Inlocuieste toate elementele de 0 care sunt complet inconjurate de 1 in matricea m
    :param mat: matricea
    :param m: integer - nr linii
    :param n: integer - nr coloane
    :return: None
    """
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]

    # visit all cells in the first and last row of the matrix
    for i in range(n):

        if mat[0][i] == 0:
            flood_fill(m, n, mat, 0, i, -1, row, col)

        if mat[m - 1][i] == 0:
            flood_fill(m, n, mat, m - 1, i, -1, row, col)

    # visit all cells in the first and last column of the matrix
    for i in range(m):

        if mat[i][0] == 0:
            flood_fill(m, n, mat, i, 0, -1, row, col)

        if mat[i][n - 1] == 0:
            flood_fill(m, n, mat, i, n - 1, -1, row, col)

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                mat[i][j] = 1

            if mat[i][j] == -1:
                mat[i][j] = 0


# ~~~~~~~~~~ TEST_P1 ~~~~~~~~~~
def test_p1():
    assert last_word("ana are mere rosii si galbene si verzi") == "verzi"
    assert last_word("ana are mere rosii si galbene sii a") == "sii"
    assert last_word("ana alearga") == "ana"
    assert last_word("") == ""


# ~~~~~~~~~~ TEST_P2 ~~~~~~~~~~
def test_p2():
    assert distanta(1, 5, 4, 1) == 5
    assert distanta(1, 1, 1, 1) == 0
    assert distanta(1, 2, 13, 7) == 13
    assert distanta(1, 1, 2, 2) == math.sqrt(2)


# ~~~~~~~~~~ TEST_P3 ~~~~~~~~~~
def test_p3():
    pass


# ~~~~~~~~~~ TEST_P4 ~~~~~~~~~~
def test_p4():
    assert cuvinte_care_apar_o_data("ana are ana are mere") == ["mere"]
    assert cuvinte_care_apar_o_data("ana are mere") == ["ana", "are", "mere"]
    assert cuvinte_care_apar_o_data("") == []
    assert cuvinte_care_apar_o_data("ana are ana are") == []


# ~~~~~~~~~~ TEST_P5~~~~~~~~~~
def test_p5():
    assert repeated_value([1, 2, 3, 4, 5, 2]) == 2
    assert repeated_value([1, 2, 3, 4, 5, 6, 7, 7]) == 7
    assert repeated_value([1, 1, 3, 4, 5, 2]) == 1


# ~~~~~~~~~~ TEST_P6 ~~~~~~~~~~
def test_p6():
    assert element_majoritar([1, 1, 1, 1, 3, 4, 5]) == 1
    assert element_majoritar([-1, 2, -1, 2, -1, 2, -1]) == -1
    assert element_majoritar([1, 2, 3, 4, 5]) is None


# ~~~~~~~~~~ TEST_P7 ~~~~~~~~~~
def test_p7():
    assert (k_element(2, [7, 4, 6, 3, 9, 1]) == 7)
    assert (k_element(1, [7, 4, 6, 3, 9, 1]) == 9)
    assert (k_element(3, [7, 4, 6, 3, 9, 1]) == 6)
    assert (k_element(2, [7, 4, 7, 3, 9, 1]) == 7)


# ~~~~~~~~~~ TEST_P8 ~~~~~~~~~~
def test_p8():
    assert generate_binary(4) == ["1", "10", "11", "100"]
    assert generate_binary(1) == ["1"]
    assert generate_binary(7) == ["1", "10", "11", "100", "101", "110", "111"]


# ~~~~~~~~~~ TEST_P9 ~~~~~~~~~~
def test_p9():
    assert suma_submat(5, 5, [[0, 2, 5, 4, 1], [4, 8, 2, 3, 7], [6, 3, 4, 6, 2], [7, 3, 1, 8, 3], [1, 5, 7, 9, 4]],
                       [1, 1], [3, 3], [2, 2], [4, 4]) == (38, 44)
    assert suma_submat(5, 4, [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
                       [1, 1], [4, 3], [2, 1], [3, 2]) == (12, 4)


# ~~~~~~~~~~ TEST_P10 ~~~~~~~~~~
def test_p10():
    assert ones_on_line([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]], 3, 5) == 2


# ~~~~~~~~~~ TEST_P11 ~~~~~~~~~~
def test_p11():
    test_mat1 = [
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    ]

    replace_zeroes(test_mat1, 8, 10)

    assert test_mat1 == [
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    ]

    test_mat2 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    replace_zeroes(test_mat2, 3, 3)

    assert test_mat2 == [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]


def run_tests():
    test_p1()
    test_p2()
    test_p3()
    test_p4()
    test_p5()
    test_p6()
    test_p7()
    test_p8()
    test_p9()
    test_p10()
    test_p11()


def print_menu():
    print("""
        1. Determina ultimul cuv din punct de vedere lexicografic dintr-un text

        2. Sa se determine distanta euclidiana intre 2 locatii identificate prin perechi de numere

        3. Sa se determine produsul scalar a doi vectori rari

        4. Determina cuvintele unui text care apar exact o singura data in acel text

        5. Pentru un sir cu n elemente care contine valori din multime {1, 2, ..., n-1} astfel incat o singura val se 
        repeta de doua ori, sa se identifice accea val care se repeta

        6. Pentru un sir cu n elemente care contine si duplicate, sa se determine elementul majoritar

        7. Sa se determine al k-lea cel mai mare element al unui sir 

        8. Sa se genereze toate numerele (in repr binara) cuprinse intre 1 si n 

        9. Considerandu-se o matrice cu n x m elemente si o lista cu perechi formate din coordonatele
        a 2 caute din matrice (p,q), (r,s), sa se calculeze suma elem din submatricile identificate de 
        fiecare pereche

        10. Se considera o matrice cu n x m elemente binare sortate crescator pe linii, 
        sa se identifice indexul liniei care contine cele mai multe elemente de 1

        11. Considerand o matrice cu n x m elemente binare, sa se inlocuiasca cu 1 toate aparitiile 
        elementelor 0 care sunt complet inconjurate de 1

        0. Quit
        """)


def main():
    while True:
        print_menu()
        cmd = input("Rezolva problema nr: ")
        if cmd == "1":
            solve_p1()
        elif cmd == "2":
            solve_p2()
        elif cmd == "3":
            solve_p3()
        elif cmd == "4":
            solve_p4()
        elif cmd == "5":
            solve_p5()
        elif cmd == "6":
            solve_p6()
        elif cmd == "7":
            solve_p7()
        elif cmd == "8":
            solve_p8()
        elif cmd == "9":
            solve_p9()
        elif cmd == "10":
            solve_p10()
        elif cmd == "11":
            solve_p11()
        elif cmd == "0":
            break


run_tests()
main()

# 0
# 2
# 5
# 4
# 1
# 4
# 8
# 2
# 3
# 7
# 6
# 3
# 4
# 6
# 2
# 7
# 3
# 1
# 8
# 3
# 1
# 5
# 7
# 9
# 4

# p1_mat = [
#     [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
#     [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
#     [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
#     [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
#     [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
# ]
