import os
import shutil

def sortuj_pliki(katalog_zrodlowy="."):
    """
    Sortuje pliki w podanym katalogu do podkatalogów na podstawie ich rozszerzeń.
    Domyślnie sortuje pliki w bieżącym katalogu (.).
    """
    print(f"Rozpoczynam sortowanie plików w katalogu: {katalog_zrodlowy}")

    # Pobierz listę wszystkich elementów (plików i katalogów) w katalogu źródłowym
    elementy = os.listdir(katalog_zrodlowy)

    for element in elementy:
        sciezka_elementu = os.path.join(katalog_zrodlowy, element)

        # Sprawdź, czy to jest plik, a nie katalog
        if os.path.isfile(sciezka_elementu):
            # Podziel nazwę pliku na nazwę i rozszerzenie
            nazwa_pliku, rozszerzenie = os.path.splitext(element)

            # Usuń kropkę z rozszerzenia i zamień na małe litery
            # Np. '.jpg' -> 'jpg'
            rozszerzenie = rozszerzenie[1:].lower() 

            # Jeśli plik nie ma rozszerzenia (np. 'README'), omiń go
            if not rozszerzenie:
                continue

            # Utwórz nazwę katalogu docelowego (np. 'JPG', 'PDF')
            nazwa_katalogu_docelowego = rozszerzenie.upper() 

            # Pełna ścieżka do katalogu docelowego
            katalog_docelowy = os.path.join(katalog_zrodlowy, nazwa_katalogu_docelowego)

            # Sprawdź, czy katalog docelowy istnieje, jeśli nie, utwórz go
            if not os.path.exists(katalog_docelowy):
                os.makedirs(katalog_docelowy)
                print(f"Utworzono katalog: {katalog_docelowy}")

            # Przenieś plik
            try:
                shutil.move(sciezka_elementu, katalog_docelowy)
                print(f"Przeniesiono '{element}' do '{katalog_docelowy}'")
            except Exception as e:
                print(f"Błąd podczas przenoszenia '{element}': {e}")
        elif os.path.isdir(sciezka_elementu) and element == "venv":
            # Ignorujemy katalog venv, aby go nie przenosić
            continue # To jest ważne, żeby skrypt nie próbował przenosić swojego własnego środowiska!
        elif os.path.isdir(sciezka_elementu) and element != "venv":
            # Wyświetlamy, jeśli pominięto inny folder (niż venv)
            print(f"Pominięto katalog: '{element}'")

    print("Sortowanie plików zakończone.")

if __name__ == "__main__":
    sortuj_pliki()