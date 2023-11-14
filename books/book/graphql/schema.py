from .query import Query
from .mutation import Mutation
import strawberry 

schema = strawberry.Schema(query=Query, mutation=Mutation)