meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    value = meme_dict[word]
    print("Bu kelimenin karşılığı:", value)
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Maalesef, bu kelime sözlükte yok!")
    
