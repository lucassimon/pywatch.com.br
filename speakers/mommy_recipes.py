from model_mommy.recipe import Recipe

# Relative imports of the 'app-name' package
from speakers.models import Speaker

speaker_test_functional = Recipe(
    Speaker,
    name='Speaker Test',
    bio='lorem ipsum dolor'
)