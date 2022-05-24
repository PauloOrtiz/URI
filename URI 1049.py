tipo = input()
especie = input()
animal = input()

if(tipo == "vertebrado"):
  if(especie == "ave"):
    if(animal == "carnivoro"):
      print("aguia")
    elif(animal == "onivoro"):
      print("pomba")
  elif(especie == "mamifero"):
    if(animal == "onivoro"):
      print("homem")
    elif(animal == "herbivoro"):
      print("vaca")
elif(tipo == "invertebrado"):
  if(especie == "inseto"):
    if(animal == "hematofago"):
      print("pulga")
    elif(animal == "herbivoro"):
      print("lagarta")
  elif(especie == "anelideo"):
    if(animal == "hematofago"):
      print("sanguessuga")
    elif(animal == "onivoro"):
      print("minhoca")