#ejercico 5 parcial 1
def verificar_valor(valor):
    if valor is None:
        print('el valor no esta asignado (es None).')
    else:
        print(f'el valor es : {valor}')
    
verificar_valor(None)
verificar_valor(321)