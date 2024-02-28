userDB = "hidrotech123";
passwordDB = "admin123";

print('software Tech Hidroituango');
print('**************************');
userName = input('Digita tu usuario:  ');
userPassword = input('Digita tu contraseña:  ');

'''if(userName == userDB & userPassword == passwordDB):
    print('Ingreso Exitoso');
else:
    print('Usuario o contraseña no coinside');
'''
print('Ingreso Exitoso') if userName == userDB and userPassword == passwordDB else print ('Usuario o contraseña no coinside')
