#009

# def add(x, y):
#     return x + y

# add2 = lambda x1, y1: x1

# print(add2(1, 2))


# def return_last(x):
#     return x[-1]

# lista1 = [(1, 2), (2, 1), (0, 4)]

# lista2 = sorted(lista1, key=return_last)  # [(2, 1), (1, 2), (0, 4)]
# print(lista2)


# lista1 = [(1, 2), (2, 1), (0, 4)]

# lista2 = sorted(lista1, key=lambda x: x[-1])  # [(2, 1), (1, 2), (0, 4)]
# print(lista2)


#list comprehensions  - jednolinijkowa pętla for

# Zadanie:
# Napisz program, który z podanej listy usuwa liczby ujemne.
# Następnie przekształca pozostałe liczby na ich pierwiastki kwadratowe
# z wykorzystaniem list comprehension.
# Wydrukuj wynik jako nową listę.

# import math

# numbers = [-10, 0, 4, -5, 16, 9, -3, 25, 1]

# # Filtrowanie liczb nieujemnych i obliczanie ich pierwiastków
# roots = [math.sqrt(n) for n in numbers if n >= 0]

# print(roots)



#010

# class Payment:
#     amount = 0
#     is_done = True

#     def show_amount(self):
#         print(self.amount)

#     def who_am_i(self):
#         print("To klasa Payment")

# p1 = Payment()

# print(p1.is_done)

# p1.show_amount()
# p1.who_am_i()

# class TxtFile:
#     path = "2.txt"

#     def read_file(self):
#         with open(self.path, encoding="utf-8") as f:
#             return f.read()

#     def write_file(self, content):
#         with open(self.path, mode='w', encoding="utf-8") as f:
#             f.write(content)
#         print(f"Zapisano do pliku: {self.path}")

# # Przykład użycia:
# txt1 = TxtFile()

# # Zapis do pliku
# txt1.write_file("To jest przykładowy tekst zapisany do pliku.")

# # Odczyt z pliku
# zawartosc = txt1.read_file()
# print("Zawartość pliku:", zawartosc)
# print(zawartosc)
