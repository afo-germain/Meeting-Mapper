def individual_serial(user)->dict:
    return {
        "id":str(user["_id"]),
        "nom":user["nom"],
        "prenom":user["prenom"],
        "latitude":user["latitude"],
        "longitude":user["longitude"],
        "adresse":user["adresse"],
    }

def list_serial(users)->list:
    return [individual_serial(user) for user in users]