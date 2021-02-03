import string
import random


def generateSlug(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def findUrl(slug, arrUrl):
    counter = 0
    for url in arrUrl:
        if url.slug == slug:
            return counter
        counter += 1
