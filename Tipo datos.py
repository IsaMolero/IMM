# Tipos de dato

## Número

tipo_basico_num = 1 # class int -> Entero
type_of_basico_num = type(tipo_basico_num)
print(type_of_basico_num)

tipo_basico_num_float = 1.8 # class float -> coma flotante
type_basico_num_float = type(tipo_basico_num_float)
print(type_basico_num_float)

sumatory = tipo_basico_num + tipo_basico_num_float
print('este es el sumatorio: ', sumatory)
print('y es de tipo', type(sumatory))
print('convertido a entero', int(sumatory))
sumatory_to_text = str(sumatory)
type_sumatory_to_text = type(sumatory_to_text)
print('pasado a texto:  ', type_sumatory_to_text)

print('modulo de 4/2', 4 % 2)

## Texto
simple_text = 'a' # class str -> String
type_of_de_var = type(simple_text)
print(type_of_de_var)

complex_text = 'hola mundo' # class str -> String
print(type(complex_text))

text_sumatory = complex_text + ' ' + simple_text
print(text_sumatory)
print(sumatory_to_text + complex_text)

## Multiply text
multiplied_text = complex_text * 5
print(multiplied_text)

# divided_text = complex_text / 5

## Boolean
True
False

print(True == True)
print(False == True)
print(False == False)
print(False != True)