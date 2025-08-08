# Lista z nazwiskami znanych osób
znane_nazwiska = ['Lewandowski', 'Skłodowska-Curie', 'Wałęsa', 'Chopin', 'Kowalski']

# Dodanie nowego nazwiska na koniec listy
znane_nazwiska.append('Piłsudski')

# Zmiana nazwiska na 3. pozycji (indeks 2) na 'Milik'
znane_nazwiska[2] = 'Milik'

# Słownik przechowujący dane o bohaterze
bohater = {
    "imie": "Superman",
    "moc": "latanie",
    "slaby_punkt": "kryptonit"
}

# Dodanie nowego klucza i wartości do słownika
bohater["kolor_stroju"] = "niebieski"

# Wyświetlenie mocy i słabego punktu bohatera
print(bohater['moc'], bohater['slaby_punkt'])