import json
from fastapi import HTTPException
from fastapi import APIRouter
from datetime import datetime
from typing import List, Dict


from config.database import users_collection
from models.users import User
from schema.users import list_serial
from bson import ObjectId

router=APIRouter()

# Chargement des users depuis un fichier JSON
def charger_users():
    try:
        with open("donnees.json", "r") as fichier:
            users = json.load(fichier)
    except FileNotFoundError:
        users = []
    return users

# Sauvegarde des users dans le fichier JSON
def sauvegarder_users(users):
    with open("donnees.json", "w") as fichier:
        json.dump(users, fichier, indent=4)

# Route pour récupérer tous les users
@router.get("/", response_model=List[Dict])
async def get_users():
    return charger_users()

# Route pour récupérer un user par son ID
@router.get("/{id}", response_model=Dict)
async def get_user(id: int):
    users = charger_users()
    for user in users:
        print("\n\n\n\n", user["id"], id, user["id"] == id)
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User non trouvé")

# Route pour ajouter un nouvel user
@router.post("/")
async def create_user(user: User):
    print(user)

    users = charger_users()
    if users:
        nouvelle_id = max(users, key=lambda x: x['id'])['id'] + 1
    else:
        nouvelle_id = 1
    user_dict = user.model_dump()
    user_dict["id"] = nouvelle_id
    users.append(user_dict)
    sauvegarder_users(users)
    return {"message": "User ajouté avec succès"}

# Route pour mettre à jour un user existant
@router.put("/{id}")
async def update_user(id: int, mise_a_jour_user: User):
    users = charger_users()
    for i, user in enumerate(users):
        if user["id"] == id:
            mise_a_jour_user_dict = mise_a_jour_user.model_dump()
            mise_a_jour_user_dict["id"] = id
            users[i] = mise_a_jour_user_dict
            sauvegarder_users(users)
            return {"message": "User mise à jour avec succès"}
    raise HTTPException(status_code=404, detail="User non trouvé")

# Route pour supprimer un user
@router.delete("/{id}")
async def delete_user(id: int):
    users = charger_users()
    for i, user in enumerate(users):
        if user["id"] == id:
            del users[i]
            sauvegarder_users(users)
            return {"message": "User supprimée avec succès"}
    raise HTTPException(status_code=404, detail="User non trouvé")

    
    
    
    
    
    
    
    
    
    
    
    
    
"""  
@router.get("/")
def users():
    users=list_serial(users_collection.find())
    return users

# Find user by ID
@router.get("/{user_id}")
def find_user_by_id(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if user:
        return {"message":"User found successfully", "user":user_helper(user)}
    else:
        return {"status_code":404, "message":"User not found"}

# Register User //We will implement it further
@router.post("/register")
async def register_user(user:User):
    result=users_collection.insert_one(dict(user))
    if result.inserted_id:
        user.id = result.inserted_id
        return {"message": "User registered successfully", "user": user.model_dump()}
    else:
        raise HTTPException(status_code=500, detail="Failed to register user")

# UPDATE USER
@router.put("/{id}")
async def update_user(id: str, user: User):
    result = users_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(user)},
        return_document=True
    )
    if result:
        return {"message": "User updated successfully", "user": result}
    else:
        raise HTTPException(status_code=404, detail="User not found")"""