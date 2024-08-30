from ninja import ModelSchema

from users.models import User


class UserIn(ModelSchema):
    class Meta:
        model = User
        fields = ("email", "password", "full_name")


class UserOut(ModelSchema):
    class Meta:
        model = User
        fields = ("email", "date_joined", "full_name")
