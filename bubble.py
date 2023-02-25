#Bubble sort Funkce

A = [5, 2, 9, 1, 4, 6, 3]
def bubble_sort(A, B=True):
    X = 7
    for c in range(X):
        for d in range(X - c - 1):
            if B:
                if A[d] > A[d + 1]:
                    A[d], A[d + 1] = A[d + 1], A[d]
            else:
                if A[d] < A[d + 1]:
                    A[d], A[d + 1] = A[d + 1], A[d]
    return A
# vzestupně
vzestupne = bubble_sort(A, True)
print("vzestupně seřazený:", vzestupne)

# sestupně
sestupne = bubble_sort(A, False)
print("sestupně seřazený:", sestupne)

y=5
vysledek = list(filter(lambda x: x<y, A))
print("Tohle jsou čísla menší než 5 " + str(vysledek))