from model_mommy.recipe import Recipe, seq

# Relative imports of the 'app-name' package
from speakers.models import SpeakerUser

speaker_test_functional = Recipe(
    SpeakerUser,
    first_name='Speaker Test',
    bio='lorem ipsum dolor'
)

speakers_list = Recipe(
    SpeakerUser,
    first_name='Jhon',
    last_name='Doe',
)
