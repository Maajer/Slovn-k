
znamky = {
    "Anna": [1, 2, 1],
    "David": [2, 3, 1],
    "Eva": [1, 1, 1]
}

studenti = {
    "Anna": {
        "vek": 17,
        "trida": "1.B",
        "znamky": [1, 2, 1]
    },
    "David": {
        "vek": 16,
        "trida": "1.A",
        "znamky": [2, 3, 1]
    },
    "Eva": {
        "vek": 17,
        "trida": "1.A",
        "znamky": [1, 1, 1]
    }
}

print("Třída Anny:", studenti["Anna"]["trida"])

prumer_david = sum(studenti["David"]["znamky"]) / len(studenti["David"]["znamky"])
print("Průměr známek Davida:", prumer_david)

vsechny_znamky = []
for data in studenti.values():
    vsechny_znamky.extend(data["znamky"])
prumer_vsech = sum(vsechny_znamky) / len(vsechny_znamky)
print("Průměr známek všech studentů:", prumer_vsech)

trida = "1.A"
print(f"Studenti ve třídě {trida}:")
for jmeno, info in studenti.items():
    if info["trida"] == trida:
        print("-", jmeno)


for info in studenti.values():
    info["dochazka"] = 95  


for info in studenti.values():
    info["znamky"].append(1)


predmety = {
    "Matematika": ["Anna", "David"],
    "Český jazyk": ["Anna", "Eva"],
    "Fyzika": ["David", "Eva"]
}


filmy = {
    "Inception": {
        "rok": 2010,
        "rezie": "Christopher Nolan",
        "hodnoceni": 8.8
    },
    "Matrix": {
        "rok": 1999,
        "rezie": "Wachowski",
        "hodnoceni": 8.7
    }
}


hrac = {
    "jmeno": "Karel",
    "uroven": 5,
    "inventar": ["meč", "lektvar", "štít"]
}


hrac["inventar"].append("klíč")


postavy = {
    "Rytíř": {
        "zdravi": 100,
        "utok": 25,
        "schopnosti": ["obrana", "úder štítem"]
    },
    "Čaroděj": {
        "zdravi": 80,
        "utok": 30,
        "schopnosti": ["ohnivá koule", "léčení"]
    }
}

utocnik = "Čaroděj"
obrance = "Rytíř"

print(f"Původní zdraví {obrance}:", postavy[obrance]["zdravi"])
print(f"{utocnik} útočí s útokem {postavy[utocnik]['utok']}")

postavy[obrance]["zdravi"] -= postavy[utocnik]["utok"]

print(f"Nové zdraví {obrance}:", postavy[obrance]["zdravi"])
