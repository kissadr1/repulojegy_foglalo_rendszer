from abc import ABC, abstractmethod
from datetime import datetime


# ======================
# JÁRAT (ABSZTRAKT)
# ======================
class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self._jaratszam = jaratszam
        self._celallomas = celallomas
        self._jegyar = jegyar

    @property
    def jaratszam(self):
        return self._jaratszam

    @property
    def jegyar(self):
        return self._jegyar

    @abstractmethod
    def tipus(self):
        pass

    def __str__(self):
        ar = f"{self._jegyar:,}".replace(",", " ")
        return f"{self.tipus()} | {self._jaratszam} -> {self._celallomas} | {ar} Ft"


# ======================
# BELFÖLDI
# ======================
class BelfoldiJarat(Jarat):
    def tipus(self):
        return "Belföldi"


# ======================
# NEMZETKÖZI
# ======================
class NemzetkoziJarat(Jarat):
    def tipus(self):
        return "Nemzetközi"


# ======================
# JEGY FOGLALÁS
# ======================
class JegyFoglalas:
    def __init__(self, nev, jarat, datum):
        self._nev = nev
        self._jarat = jarat

        try:
            self._datum = datetime.strptime(datum, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Hibás dátum formátum!")

        if self._datum < datetime.now():
            raise ValueError("A dátum nem lehet múltbeli!")

    @property
    def nev(self):
        return self._nev

    @property
    def jarat(self):
        return self._jarat

    def __str__(self):
        return f"{self._nev} | {self._jarat.jaratszam} | {self._datum.date()}"


# ======================
# LÉGITÁRSASÁG
# ======================
class LegiTarsasag:
    def __init__(self, nev):
        self._nev = nev
        self._jaratok = []
        self._foglalasok = []

    def jarat_hozzaadas(self, jarat):
        self._jaratok.append(jarat)

    def jaratok_listazasa(self):
        for j in self._jaratok:
            print(j)

    def foglalas(self, jaratszam, nev, datum):
        jarat = next((j for j in self._jaratok if j.jaratszam == jaratszam), None)

        if not jarat:
            print("❌ Nincs ilyen járat!")
            return

        try:
            foglalas = JegyFoglalas(nev, jarat, datum)
            self._foglalasok.append(foglalas)
            print(f"✅ Foglalás sikeres! Ár: {jarat.jegyar} Ft")
        except Exception as e:
            print("❌ Hiba:", e)

    def lemondas(self, nev, jaratszam):
        for f in self._foglalasok:
            if f.nev == nev and f.jarat.jaratszam == jaratszam:
                self._foglalasok.remove(f)
                print("✅ Foglalás törölve!")
                return

        print("❌ Nincs ilyen foglalás!")

    def foglalasok_listazasa(self):
        if not self._foglalasok:
            print("Nincs foglalás.")
            return

        for f in self._foglalasok:
            print(f)


# ======================
# ELŐKÉSZÍTÉS (A TE JÁRATAID!)
# ======================
def inicializalas():
    lt = LegiTarsasag("WizzAir")

    lt.jarat_hozzaadas(NemzetkoziJarat("J1", "Kréta", 85000))
    lt.jarat_hozzaadas(NemzetkoziJarat("J2", "Mallorca", 90000))
    lt.jarat_hozzaadas(NemzetkoziJarat("J3", "Berlin", 40000))
    lt.jarat_hozzaadas(NemzetkoziJarat("J4", "Korfu", 67000))
    lt.jarat_hozzaadas(NemzetkoziJarat("J5", "Szardínia", 97000))
    lt.jarat_hozzaadas(NemzetkoziJarat("J6", "Stuttgart", 35000))
    lt.jarat_hozzaadas(NemzetkoziJarat("J7", "London", 75000))

    # alap foglalások
    lt.foglalas("J1", "Anna", "2026-06-01")
    lt.foglalas("J2", "Béla", "2026-06-02")
    lt.foglalas("J3", "Cecil", "2026-06-03")
    lt.foglalas("J4", "Dani", "2026-06-04")
    lt.foglalas("J5", "Erika", "2026-06-05")
    lt.foglalas("J6", "Feri", "2026-06-06")

    # te
    lt.foglalas("J7", "Balogh Adrienn", "2026-07-01")

    return lt


# ======================
# MENÜ
# ======================
def menu():
    lt = inicializalas()

    while True:
        print("\n--- REPÜLŐJEGY RENDSZER ---")
        print("1 - Járatok listázása")
        print("2 - Jegy foglalása")
        print("3 - Foglalás lemondása")
        print("4 - Foglalások listázása")
        print("0 - Kilépés")

        valasz = input("Választás: ")

        if valasz == "1":
            lt.jaratok_listazasa()

        elif valasz == "2":
            lt.jaratok_listazasa()
            j = input("Járatszám: ")
            n = input("Név: ")
            d = input("Dátum (YYYY-MM-DD): ")
            lt.foglalas(j, n, d)

        elif valasz == "3":
            n = input("Név: ")
            j = input("Járatszám: ")
            lt.lemondas(n, j)

        elif valasz == "4":
            lt.foglalasok_listazasa()

        elif valasz == "0":
            print("Kilépés...")
            break

        else:
            print("❌ Hibás választás!")


# ======================
# FUTTATÁS
# ======================
if __name__ == "__main__":
    menu()