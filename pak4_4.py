def generuj_funkcje_potegowania(exponent):
    def potegowanie(x):
        return x ** exponent
    return potegowanie

do_kwadratu = generuj_funkcje_potegowania(2)
do_szescianu = generuj_funkcje_potegowania(3)


print("3 do kwadratu =", do_kwadratu(3))

print("3 do sześcianu =", do_szescianu(3))
