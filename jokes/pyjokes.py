from __future__ import absolute_import
import random

from .jokes_en import jokes_en

all_jokes = {
    'en': jokes_en
}


class LanguageNotFoundError(Exception):
    pass


class CategoryNotFoundError(Exception):
    pass


def get_jokes(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'chuck', 'all', 'twister'
    lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu', 'it'

    Returns
    -------
    jokes: list
    """

    if language not in all_jokes:
        raise LanguageNotFoundError('No such language %s' % language)

    jokes = all_jokes[language]

    if category not in jokes:
        raise CategoryNotFoundError('No such category %s in language %s' % (category, language))

    return jokes[category]


def get_joke(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'chuck', 'all', 'twister'
    lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu', 'it'

    Returns
    -------
    joke: str
    """

    jokes = get_jokes(language, category)
    return random.choice(jokes)
