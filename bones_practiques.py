#!/usr/bin/env python
dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))

quocient = dividend // divisor
residu = dividend % divisor

print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")