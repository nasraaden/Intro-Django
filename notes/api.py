from rest_framework import serializers, viewsets
from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        logged_in_user = self.request.user
        # if user is not logged in return nothing
        if logged_in_user.is_anonymous:
            return PersonalNote.objects.none()
        # otherwise if user is logged in, return logged in user
        else:
            return PersonalNote.objects.filter(user=logged_in_user)
