"""

PY1010 Arbeidskrav 2
Jesper Lundström (jelun6183@usn.no)
24.10.2026

"""

#%% Oppgave 1: Alder i 2024
alder = int(input("Hvilket år er du født? "))
år = 2024

alder_2024 = år - alder

print(f"I løpet av 2024 blir du {alder_2024} år gammel")

#%% Oppgave 2: Pizza til klassefest
import numpy as np
antall_elever = int(input("Skriv inn antall elever: "))

pizzaer = int(np.ceil(antall_elever/4))

print(f"{pizzaer} pizzaer skal handles inn til festen")

#%% Oppgave 3: Grader til radianer
import numpy as np
v_grad = float(input("Skriv inn gradetallet: "))

v_rad = v_grad*np.pi/180

print(f"{v_grad} grader tilsvarer {v_rad:.2f} radianer.")

#%% Oppgave 4: Dictionary med land og hovedstader
# a) Dictionary
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

# b) Oppslag
land = input("Skriv inn et land: ")
if land in data:   
    hovedstad, innbyggere = data[land]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} millioner innbyggere i {hovedstad}.")
else:
    print(f"{land} finnes ikke i ordboken")
    # c) Legge til land
    legge_til = input("Ønsker du å legge til landet i ordboken? (Ja/Nei): ")
    if legge_til.lower() == "ja":
        nytt_land = input("Landets navn: ")
        ny_hovedstad = input("Hovedstad: ")
        ny_innbygger = float(input("Hvor stor er befolkningen (i millioner)? "))
        data[nytt_land] = [ny_hovedstad, ny_innbygger]
        print(data)

#%% Oppgave 5: Areal og omkrets

import numpy as np

# Funksjon og inn-argumenter
def beregn_figur(a, b):
    hypotenus = np.sqrt(a**2 + b**2)
    radius = a/2
    areal_sirkel = np.pi*radius**2
    omkrets_sirkel = 2*np.pi*radius
    areal_trekant = (a*b)/2
    
    figur_areal = areal_trekant + areal_sirkel/2
    figur_omkrets = b + hypotenus + omkrets_sirkel/2
    return figur_areal, figur_omkrets

# Verdier for a og b
a = float(input("Verdien på a er: "))
b = float(input("Verdien på b er: "))
figur_areal, figur_omkrets = beregn_figur(a, b)

print(f"Figurens areal er {figur_areal:.2f}, og omkretsen er {figur_omkrets:.2f}.")

#%% Oppgave 6: Plotting
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)

y = -x**2 - 5

plt.figure()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, label = "f(x) = $-x^2$ - 5")
plt.legend()
plt.grid()

