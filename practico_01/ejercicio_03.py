"""Único return vs múltiples return."""

from typing import Union


def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    flag = 0
    if multiplicar:
        flag = a * b
    else:
        if b != 0:
            flag = a/b
        else:
            flag = "Operación no válida"
    return flag

# NO MODIFICAR - INICIO
assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN


###############################################################################


def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    if multiplicar:
        return(a * b)
    else:
        if b != 0:
            return (a/b)
        else:
            return( "Operación no válida")

# NO MODIFICAR - INICIO
assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN
