from ninja import Router

from blogs import schemas
from blogs.models import Blog


router = Router()


@router.post("/write", response=schemas.BlogOut)
def write_blog(request, payload: schemas.BlogIn):
    return Blog.objects.create(**payload.dict())


@router.get("/{id}", response={404: None, 200: schemas.BlogOut})
def get_blog(request, id: int):
    try:
        return Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return 404, None


@router.delete("/delete/{id}")
def delete_blog(request, id: int):
    Blog.objects.filter(id=id).delete()
