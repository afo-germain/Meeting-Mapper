import json
from fastapi import HTTPException
from fastapi import APIRouter
from datetime import datetime
from typing import List, Dict


from config.database import users_collection
from models.users import User
from schema.users import list_serial
from bson import ObjectId

from controllers.computation import get_optimal_meeting_location
from .users_routes import get_users

router=APIRouter()

# Route pour récupérer le résultat
@router.get("/")
async def Computation():
    return get_optimal_meeting_location(await get_users())
