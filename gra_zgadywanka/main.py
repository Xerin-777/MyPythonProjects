import random

def gra_w_zgadywanie():
    # 1. Losowanie liczby z przedziału od 1 do 100
    wylosowana_liczba = random.randint(1, 100)
    
    # 2. Inicjalizacja licznika prób
    liczba_prob = 0
    
    print("Witaj w grze 'Zgadnij Liczbę'!")
    print("Wylosowałem liczbę z przedziału od 1 do 100. Spróbuj ją odgadnąć.")
    
    # 3. Pętla, która będzie działać, dopóki gracz nie odgadnie liczby
    while True:
        # 4. Zwiększanie licznika prób i odbieranie odpowiedzi
        liczba_prob += 1
        try:
            zgadywana_liczba = int(input("Podaj swoją liczbę: "))
        except ValueError:
            print("To nie jest prawidłowa liczba. Spróbuj ponownie.")
            continue # Przejdź do następnej iteracji pętli
        
        # 5. Sprawdzanie, czy zgadywana liczba jest poprawna
        if zgadywana_liczba < wylosowana_liczba:
            print("Za mało!")
        elif zgadywana_liczba > wylosowana_liczba:
            print("Za dużo!")
        else:
            print(f"Brawo! Odgadłeś liczbę {wylosowana_liczba} w {liczba_prob} próbach!")
            break # Zakończ pętlę, bo gracz odgadł liczbę

if __name__ == "__main__":
    gra_w_zgadywanie()

