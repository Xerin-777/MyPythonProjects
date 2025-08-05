def policz_znaki(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            zawartosc = plik.read()
            liczba_slow = len(zawartosc.split())
            liczba_znakow = len(zawartosc)
            print(f"Plik '{nazwa_pliku}' zawiera:")
            print(f"  - {liczba_slow} słów")
            print(f"  - {liczba_znakow} znaków (włączając spacje)")
    except FileNotFoundError:
        print(f"Błąd: Plik '{nazwa_pliku}' nie został znaleziony.")

if __name__ == "__main__":
    policz_znaki("dane.txt")