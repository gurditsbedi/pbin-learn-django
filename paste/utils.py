import random
import string

from .models import pasteModel

SHORTCODE_LEN = 6


def code_generator(size=SHORTCODE_LEN, chars=string.ascii_lowercase
                                            + string.ascii_uppercase
                                            + string.digits):
    return ''.join(random.choice(chars)  for _ in range(size))


def create_shortcode(size=SHORTCODE_LEN):
    new_code = code_generator(size=size)
    qs_exists = pasteModel.objects.filter(slug=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
