from .api_router import api_router
from .welcome_routes import router
from .users_routes import router as users_router
from .computations_routes import router as computations_router

api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(computations_router, prefix="/meeting", tags=["Computations"])
