from djapian import space, Indexer
from movieApp.models import movie

class movieEntry(Indexer):
    fields = [('name', 2), ]

    def trigger(indexer, object):
        return object.is_published

space.add_index(movie, movieEntry, attach_as='indexer')