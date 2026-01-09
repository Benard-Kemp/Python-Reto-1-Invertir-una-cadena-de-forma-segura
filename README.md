# Reto #1 — Invertir una cadena de forma segura (Python)

Este reto forma parte de **SolveConPython**, una colección de ejercicios prácticos en español para aprender Python resolviendo problemas reales y testeables.

En este reto implementarás una función que invierte una cadena de texto de forma **segura**, manejando correctamente casos borde como `None` o tipos incorrectos.

---

## 🧠 Objetivo del reto

Crear una función que:
- Invierta una cadena de texto
- Maneje entradas inválidas de forma explícita
- Sea fácil de probar con tests automatizados

---

## 📋 Reglas

La función debe cumplir las siguientes reglas:

- `None` → devuelve una cadena vacía `""`
- Si el valor no es una cadena (`str`) → lanza `TypeError`
- Si es una cadena válida → devuelve la cadena invertida

---

## 🧪 Ejemplos

```python
invertir_cadena_segura("hola")      # "aloh"
invertir_cadena_segura("")          # ""
invertir_cadena_segura(None)        # ""
invertir_cadena_segura(123)         # TypeError


