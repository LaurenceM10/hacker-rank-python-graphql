import graphene
from graphene_django import DjangoObjectType

from .models import Link
from .models import Book


# Define the output fields based in Link model
class LinkType(DjangoObjectType):
    class Meta:
        model = Link
        description = 'This represent a Link'


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        description = 'This represent a Book'

# Query to list links
class Query(graphene.ObjectType):
    links = graphene.List(LinkType)
    books = graphene.List(BookType)

    # Return the links from database using Django ORM
    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()



class CreateLink(graphene.Mutation):
    # Output fields
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    # Mutation arguments
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # Mutation method: to create a link in the database
    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        # Return the link saved, this matches with the output fiels 
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )


# Mutation class to resolved the CreateLink mutation
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
