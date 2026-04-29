from datetime import datetime


# ======================
# JÁRAT
# ======================
class Jarat:
    def __init__(self, jaratszam, celallomas, jegyar, tipus):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.tipus = tipus

    def __str__(self):
        return f"{self.tipus} | {self.jaratszam} -> {self.celallomas} | {self.jegyar} Ft"


# ======================
# FOGLALÁS
# ======================
class JegyFoglalas:
    def __init__(self, nev, jarat, datum):
        self.nev = nev
        self.jarat = jarat

        try:
            self.datum = datetime.strptime(datum, "%Y-%m-%d")
        except:
            raise ValueError("Hibás dátum formátum!")

        if self.datum.date() < datetime.now().date():
            raise ValueError("A dátum nem lehet múltbeli!")

    def __str__(self):
        return f"{self.nev} | {self.jarat.jaratszam} | {self.datum.date()}"


# ======================
# LÉGITÁRSASÁG
# ======================
class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def jaratok_listazasa(self):
        for j in self.jaratok:
            print(j)

    def foglalas(self, jaratszam, nev, datum):
        jarat = None

        for j in self.jaratok:
            if j.jaratszam == jaratszam:
                jarat = j
                break

        if jarat is None:
            print("Nincs ilyen járat!")
            return

        try:
            uj = JegyFoglalas(nev, jarat, datum)
            self.foglalasok.append(uj)
            print(f"Foglalás sikeres! Ár: {jarat.jegyar} Ft")
        except ValueError as hiba:
            print("Hiba:", hiba)

    def lemondas(self, nev, jaratszam):
        talalat = None

        for f in self.foglalasok:
            if f.nev == nev and f.jarat.jaratszam == jaratszam:
                talalat = f
                break

        if talalat:
            self.foglalasok.remove(talalat)
            print("Foglalás törölve!")
        else:
            print("Nincs ilyen foglalás!")

    def foglalasok_listazasa(self):
        if len(self.foglalasok) == 0:
            print("Nincs foglalás.")
        else:
            for f in self.foglalasok:
                print(f)


# ======================
# ADATOK
# ======================
def inicializalas():
    lt = LegiTarsasag("WizzAir")

    lt.jarat_hozzaadas(Jarat("J1", "Kréta", 85000, "Nemzetközi"))
    lt.jarat_hozzaadas(Jarat("J2", "Mallorca", 90000, "Nemzetközi"))
    lt.jarat_hozzaadas(Jarat("J3", "Berlin", 40000, "Nemzetközi"))
    lt.jarat_hozzaadas(Jarat("J4", "Korfu", 67000, "Nemzetközi"))
    lt.jarat_hozzaadas(Jarat("J5", "Szardínia", 97000, "Nemzetközi"))
    lt.jarat_hozzaadas(Jarat("J6", "Stuttgart", 35000, "Nemzetközi"))
    lt.jarat_hozzaadas(Jarat("J7", "London", 75000, "Nemzetközi"))

    # alap foglalások
    lt.foglalas("J1", "Anna", "2026-06-01")
    lt.foglalas("J2", "Béla", "2026-06-02")
    lt.foglalas("J3", "Cecil", "2026-06-03")

    return lt


# ======================
# MENÜ
# ======================
def menu():
    lt = inicializalas()

    while True:
        print("\n--- REPÜLŐJEGY RENDSZER ---")
        print("1 - Járatok")
        print("2 - Foglalás")
        print("3 - Lemondás")
        print("4 - Foglalások")
        print("0 - Kilépés")

        v = input("Választás: ")

        if v == "1":
            lt.jaratok_listazasa()

        elif v == "2":
            lt.jaratok_listazasa()
            j = input("Járatszám: ")
            n = input("Név: ")
            d = input("Dátum (YYYY-MM-DD): ")
            lt.foglalas(j, n, d)

        elif v == "3":
            n = input("Név: ")
            j = input("Járatszám: ")
            lt.lemondas(n, j)

        elif v == "4":
            lt.foglalasok_listazasa()

        elif v == "0":
            print("Kilépés...")
            break

        else:
            print("Hibás választás!")


# ======================
# FUTTATÁS
# ======================
menu()
