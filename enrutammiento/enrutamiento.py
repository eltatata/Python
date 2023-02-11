# ACCEDER A UN MODULO FUERA DE LA RUTA ACTUAL

import sys

# develve una lista de "paths"
for path in sys.path: print(path)
print()

sys.path.append("c:\\Users\\Usuario\Desktop\\Python\\Python-2023\\modulos")
for path in sys.path: print(path)
print()

from moduloMath import math as m

print(m("1 * 3 + 2"))