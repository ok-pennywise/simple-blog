from ninja import ModelSchema

from blogs.models import Image, Blog


class ImageIn(ModelSchema):
    class Meta:
        model = Image
        fields = "__all__"


class ImageOut(ModelSchema):
    class Meta:
        model = Image
        fields = ("media",)


class BlogIn(ModelSchema):
    images: list[ImageIn]

    class Meta:
        model = Blog
        fields = "__all__"


class BlogOut(ModelSchema):
    images: list[ImageOut]

    class Meta:
        model = Blog
        fields = "__all__"
