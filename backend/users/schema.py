import graphene
from graphene_django import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    email = graphene.String()
    password = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, email, password, first_name, last_name):
        user = User(first_name=first_name, last_name=last_name)
        user.save()

        return CreateUser(
            id=user.id,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
        )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
