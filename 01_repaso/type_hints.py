"""
    03. Type Hints
    Son una nueva sintaxis de Python, que permite declarar el tipo de una variable.

    FastAPI trabaja con estos type hints.
"""

my_string_variable = "My String variable"
print(my_string_variable)
print(type(my_string_variable))

# Python es de tipado dinamico: esta variable que era str ahora es int.
my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

# Usando Type Hints ayuda a definir el tipo de una variable.
print("\n Type Hints:")

my_typed_variable: str = "My type String variable"
print(my_typed_variable)
print(type(my_typed_variable))

# Si ahora reasignamos, el seguira ejecutando.
my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))