from src.model.user_profile_dto import UserProfileDto
from src.database.database import get_database_connection
from src.constants.constants import USER_PROFILE_COLLECTION


async def create_user(user_profile_dto: UserProfileDto):
    
    user_profile_model = user_profile_dto.toModel()
    create_id = await get_database_connection(USER_PROFILE_COLLECTION).insert_one(user_profile_model)
    
    return {"id":str(create_id.inserted_id)}