from model_mommy.recipe import Recipe, foreign_key

# Relative imports of the 'app-name' package
from talks.models import Talk
from speakers.mommy_recipes import speaker_test_functional

talk_test_functional = Recipe(
    Talk,
    speaker=foreign_key(
        speaker_test_functional
    ),
    title=u'Talk to do test functional',
    slug=u'talk-to-do-test-functional',
    summary=u'test in everywhere',
)
