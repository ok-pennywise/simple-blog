from ninja import NinjaAPI
from users.routes import router as user_router
from blogs.routes import router as blog_router

api = NinjaAPI()

api.add_router("/users/", user_router)
api.add_router("/blogs/", blog_router)
