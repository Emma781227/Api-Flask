import random
# mon_dictionnaire = {"clé1": "valeur1", "clé2": 2, "clé3": [1, 2, 3]};
# for keys in mon_dictionnaire:
#     print(mon_dictionnaire[keys]);
    
# def sommealeatoire(a, b):
#     aleatoiren1 = random.randint(1,a);
#     aleatoiren2 = random.randint(1,b);
#     sommes = aleatoiren1 + aleatoiren2;
#     return sommes;

# n1 = int(input("Enter the max number  :") )
# n2 = int(input("Enter the max nomber :") )
# # n3 = float(input("Enter the first nomber :") )

# # result = somme(n1,n2,n3);
# resultaleatoire = sommealeatoire(n1,n2)
# print(resultaleatoire);
    
    

# print (mon_dictionnaire["clé1"]);



# my_list = ["pomme", "banane", "orange", "kiwi", "mangue"]

# random_element = random.choice(my_list)

# print(f"Element aléatoire : {random_element}")




# def create_list(array):
#     valeur_aleatoir = random.choice(create_list);
#     return valeur_aleatoir;

# def display_random_element(user_list):
#     if  user_list:
#         print("La liste est vide !")
#     else:
#         random_element = random.choice(user_list)
#     print(f"Element aléatoire : {random_element}")
#     valeur_aleatoir = create_list(user_list)
#     return valeur_aleatoir;
    
# user_list = []
# print("rempliser la list eppuiyer sur entree pour terminer")
# while True:
#     element = input("Entrez un élément pour la liste  ")
#     if element.lower() == "":
#       break
#     else:
#         user_list.append(element)

# print("list remplie", user_list)

# display_random = display_random_element(user_list)





def aleatoire (emma, list, min, max): 
#   Fonction qui applique random.choice ou random.randint selon un booléen.
  if emma:
    random_element = random.choice(list )
  else: 
     random_element = random.randint(min, max)
  return random_element

rez = aleatoire(True, [1,2,3,4,5], 1, 2)
print(rez)

   




  


