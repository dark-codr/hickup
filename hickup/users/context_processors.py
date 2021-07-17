from hickup.users.models import User
from hickup.utils.cache_processors import memorize

def total_members(request):

    return {

        'total_members', memorize(

            lambda: User.objects.number_of_members(),

        )

    }