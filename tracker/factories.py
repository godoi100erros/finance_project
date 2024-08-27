import factory
from tracker.models import Category, Transaction, User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'tracker.User'  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('username',)

    username = 'john'

