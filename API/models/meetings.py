from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import List, Tuple,Optional

class Meeting(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    date_heure: datetime
    latitude: float
    longitude: float
    nb_participants: int
    
    def model_dump(self):
        return {
            "date_heure": self.date_heure,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "nb_participants": self.nb_participants,
        }