from hickup.utils.cache_processors import memorize
from hickup.topics.models import Topics

def latest_topics(request):
    return {
        'latest_topics', memorize(
            lambda: Topics.objects.all_latest()[:10],
        )
    }

def helpful_topics(request):
    return {
        'helpful_topics', memorize(
            lambda: Topics.objects.all_helpful()[:5],
        )
    }

def private_topics(request):
    return {
        'private_topics', memorize(
            lambda: Topics.objects.all_private(),
        )
    }


def total_topics(request):
    return {
        'total_topics', memorize(
            lambda: Topics.objects.all().count(),
        )    
    }
