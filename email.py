email = input("Introduce tu email electrónico: ").strip()

nombreUsuario = email[:email.index("@")]

dominio = email[email.index("@")+1:]

resultado = "Tu nombre de Usuario es: {}\nTu dominio es: {}".format(nombreUsuario, dominio)
print(resultado)