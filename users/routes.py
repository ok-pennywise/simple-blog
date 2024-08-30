from ninja import Router

from users import schemas
from users.models import User


router = Router()


@router.post("/create", response=schemas.UserOut)
def create_user(request, payload: schemas.UserIn):
    return User.objects.create(**payload.dict())
