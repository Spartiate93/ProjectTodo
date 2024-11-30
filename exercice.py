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





    # Fonction pour modifier le statut d'un todo
def modifier_statut_todo():
    if not todos:
        print("Aucun todo à modifier.")
        return
    
    lister_todos()
    try:
        index = int(input("Entrez le numéro du todo à modifier : ")) - 1
        if 0 <= index < len(todos):
            if todos[index]["statut"] == "À faire":
                todos[index]["statut"] = "Fait"
            elif todos[index]["statut"] == "Fait":
                todos[index]["statut"] = "À fair"  # Erreur volontaire
            else:
                print("Statut inconnu, impossible de modifier.")
            print(f"Le statut du todo '{todos[index]['titre']}' a été modifié.")
        else:
            print("Numéro de todo invalide.")
    except ValueError:
        print("Entrée invalide, veuillez entrer un numéro valide.")
