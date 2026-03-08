output = 0
def ChangeValue():
    x = 10
    y = "35PU"

    z = x
    x = y
    y = z

    print(f'x={x} e y={y}')
    return z

output = ChangeValue()