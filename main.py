meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }
print("Hola, este programa te enseñara el significado de ciertas palabras que no entiendas.")
print("Puedes buscar el significado de 5 palabras: CRINGE , LOL , ROLF , SHEESH , CREEPY , AGGRO")

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
        # ¿Qué debemos hacer si se encuentra la palabra?
    else:
        print("No se en encuentra esa palabra")
        # ¿Qué hacer si no se encuentra la palabra?
