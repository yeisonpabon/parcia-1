#ejercicio 3 parcial 1 

tex = input('ingrese una cadena de texto:')
tex_Mayus = tex.upper()
longuitud = len(tex)

contien_phyton = 'python' in tex 

print(f'su cadena en mayusculas: {tex_Mayus}')
print(f'numero de caracteres: {longuitud}' )
print(f'contiene la palabra python:{contien_phyton}')