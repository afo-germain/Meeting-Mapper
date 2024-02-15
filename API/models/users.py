from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import List, Tuple,Optional

class User(BaseModel):
    id: int
    nom: str
    prenom: str
    latitude: float
    longitude: float
    adresse: str
    
    def model_dump(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "adresse": self.adresse,
        }