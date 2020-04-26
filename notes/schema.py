from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note


class NoteType(DjangoObjectType):

    # which model to expose to GraphQL
    class Meta:
        # this is the model to export
        model = Note
        # tell it what kind of data this is, this one is a node
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    # field that we see exported
    # when we do a query on notes, we want it to return a list which will be a list of objects that corresponds to NoteType we decalred above which corresponds to our Note model
    notes = graphene.List(NoteType)
    # has to be named the same as above

    def resolve_notes(self, info):
        # return a list of all the notes to show
        return Note.objects.all()


schema = graphene.Schema(query=Query)
