import datetime
from haystack import indexes
from .models import Talk


class TalkIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    speaker = indexes.CharField(model_attr='speaker')
    modified = indexes.DateTimeField(model_attr='modified')

    def get_model(self):
        return Talk

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return (
            self.get_model()
            .objects
            .filter(
                modified__lte=datetime.datetime.now()
            )
        )
