import string, random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import PIL
from django.core.files.uploadedfile import InMemoryUploadedFile

# crate multiple fuction for this pojects


def rand_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
     """
     used to generate random  string with a given lenght.
     """
     return ''.join(random.choice(chars) for _ in range(size))

