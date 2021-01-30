numero_inicial = 1
numero_final   = 100

dic_resultados = {
					(False, False):'',
					(True , False):'IT',
					(False, True ):'BHUT',
					(True , True ):'BHUT TI'
				}

for numero in range(numero_inicial, numero_final + 1):
	
	eh_multiplo_de_3 = numero % 3 == 0
	eh_multiplo_de_5 = numero % 5 == 0
	
	chave = (
			eh_multiplo_de_3,
			eh_multiplo_de_5
			)
	
	frase_de_resultado = dic_resultados[chave]
	
	print(
			numero,
			frase_de_resultado,
			end='\t'
		)
