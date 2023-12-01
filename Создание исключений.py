class InvalidDataException(Exception):
    pass


class Processing(Exception):
    pass


try:

    raise InvalidDataException('Дождь зимой')

except InvalidDataException as e:
    print(f"Аномалия: {e}")

try:
    raise Processing('Снег летом')

except Processing as e:
    print(f"Аномалия: {e}")
finally:
    print("У природы нет плохой погоды!")
