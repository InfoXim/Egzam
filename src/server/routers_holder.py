from .router import Router
from .resolver import Resolver
from .routers_resolvers.auth_router import AuthRouter
from src.database.models import *

UserRouter = AuthRouter("Users", Users)
ApplicationsRouter = Router("Applications", Applications)
CarsRouter = Router("Cars", Cars)
ClientRouter = Router("Client", Client)
Application_statusesRouter = Router("Application_statuses", Application_statuses)


routers = (UserRouter.router, ApplicationsRouter.router, CarsRouter.router, ClientRouter.router, Application_statusesRouter.router)
