
while True:
    print ("Figuras Geométricas")
    print ("1 - Círculo")
    print ("2 - Triângulo")
    print ("3 - Quadrado")
    print ("4 - Retângulo")
    print ("5 - Paralelogramo")
    print ("6 - Losango")
    print ("7 - Trapézio")
    print ("0 - sair")

    opcao = input ("Escolha uma opção:")
    if opcao == "1":
     raio_circulo = float (input ("digite o raio de seu circulo:"))
     pi = 3.14
     resultado = (raio_circulo * raio_circulo * pi) 
     print (f"area do seu circulo é: {resultado}")

    elif opcao == "2":
     base_triangulo = float (input ("digite a base do triangulo:"))
     altura_triangulo = float (input("digite a altura do triangulo:"))
     resultado = (base_triangulo * altura_triangulo) /2
     print (f"area do seu triangulo é: {resultado}")

    elif opcao == "3":
     lado1_quadrado = float (input ("digite um lado do seu quadrado:"))
     lado2_quadrado = float (input("digite digite outro do seu quadrado:"))
     resultado = (lado1_quadrado * lado2_quadrado) 
     print (f"area do seu quadrado é: {resultado}")

    elif opcao == "4":
     base_retangulo = float (input ("digite a base do retangulo:"))
     altura_retangulo = float (input("digite a altura do retangulo:"))
     resultado = (base_retangulo * altura_retangulo) 
     print (f"area do seu retangulo é: {resultado}")

    elif opcao == "0":
        print ("saindo do sistema...")
        break

    elif opcao == "5":
     base_paralelogramo = float (input ("digite a base do paralelogramo:"))
     altura_paralelogramo = float (input("digite a altura do paralelogramo:"))
     resultado = (base_paralelogramo * altura_paralelogramo) 
     print (f"area do seu paralelogramo é: {resultado}")

    elif opcao == "6":
     Diagonal_maior= float (input ("digite diagonal maior:"))
     Diagonal_menor= float (input("digite a diagonal menor:"))
     resultado = (Diagonal_maior * Diagonal_menor / 2)
     print (f"area do seu losango é: {resultado}")

    elif opcao == "7":
     base_maior = float (input ("digite o valor da base maior:"))
     base_menor= float (input("digite o valor da base menor:"))
     altura_trapezio = float  (input("digite a altura"))
     resultado = (base_maior + base_menor) * (altura_trapezio) /2
     print (f"area do seu losango é: {resultado}")
    else: 
        print ("opcao invalida, tente novamente!!!")
        