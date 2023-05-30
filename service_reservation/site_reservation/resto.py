import json
import random

emplacements = {
    "en privée1":"100$",
    "en privée2":"100$",
    "vue de mer1" : "150$",
    "vue de mer2" : "150$",
    "balcon1" : "130$",
    "balcon2" : "130$",
    "en publique1" : "50$",
    "en publique2" : "50$"
}

img = {
    "balcon1": "static/photo/balcon/balcon1.jpg",
    "balcon2": "static/photo/balcon/balcon2.jpg",
    "vue de mer1": "static/photo/mer/mer.jpg",
    "vue de mer2": "static/photo/mer/mer2.jpg",
    "en privée1": "static/photo/privée/en_privé.jpg",
    "en privée2": "static/photo/privée/privé.jpg",
    "en publique1": "static/photo/publique/pubique1.jpg",
    "en publique2": "static/photo/publique/publique2.jpg",
}   

donnees = []



for _ in range(100):
    emplacement = random.choice(["en privée1", "vue de mer1", "balcon1", "en publique1","en privée2", "vue de mer2", "balcon2", "en publique2"])
    type_table = random.choice(["table de bistriot", "table ronde", "table rectangle", "table haute et mange-debout"])
    # nombre_places = random.randint(1,10)
    couleur_nappe = random.choice(["bleu", "rouge", "noir", "blanc", "doré"])
    cout_reservation = emplacements[emplacement]
    imgs =  img[emplacement]
   

    resto = {
        "emplacement": emplacement,
        "type_table": type_table,
        # "nombre_places": nombre_places,
        "couleur_nappe" : couleur_nappe,
        "cout_reservation" : cout_reservation,
        "imgs" : imgs
    }

    donnees.append(resto)


with open("donnees_restos.json", "w", encoding="utf-8") as fichier_json:
    json.dump(donnees, fichier_json, indent=4, ensure_ascii=False)


