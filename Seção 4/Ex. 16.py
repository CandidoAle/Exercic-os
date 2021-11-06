"""Exercício 16 (36)

Calcular volume de um cilindro com os dados altura e raio da base.
Formula -> V = pi * raio ** 2 * altura
"""
import numpy

altura = float(input('Qual a altura do cilindro: '))
raio = float(input('Qual o raio da base do cilindro: '))

volume = numpy.pi * raio ** 2 * altura
print(volume)
