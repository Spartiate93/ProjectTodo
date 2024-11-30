def lister_todos():
    print('Fonctionnalité "lister les todos" à venir')



    # Liste pour stocker les todos
todos = []




# Fonction pour lister les todos
def lister_todos():
    if not todos:
        print("Aucun todo disponible.")
    else:
        print("\nListe des todos :")
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo['titre']} - Statut : {todo['statut']}")
    print()