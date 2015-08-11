"""
Add reading time tags to each article on Pocket.
"""

import logging

import pocket

from config import (
    consumer_key,
    access_token,
    words_per_minute,
    logging_level,
    logging_handler,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging_level)
logger.addHandler(logging_handler)


def add_tag(item, tag):
    """ Add a tag on an article. """

    logger.debug('Tag "%s" on %s -- %s' % (tag, item.id, item.title))

    api.send("""
    [
        {
            "action"  : "tags_add",
            "item_id" : "%s",
            "tags"    : "%s"
        }
    ]
    """ % (item.id, tag))


def reading_time(minutes):
    """ Convert minutes to a nice string representing the time. """
    rounded = int(5 * round(float(minutes)/5)) or 2

    if 2 < rounded < 50:
        return '%d minutes' % rounded
    elif 50 <= rounded < 75:
        return '1 hour'
    elif 75 <= rounded < 90:
        return '1.5 hours'
    else:
        return '2 hours'


if __name__ == '__main__':
    api = pocket.Api(consumer_key=consumer_key,
                     access_token=access_token)

    try:
        items = api.get(sort='newest', state='unread', tag='_untagged_',
                        detailType='complete')
    except AttributeError:
        items = []

    for item in items:

        item.word_count = int(item.word_count)
        item.is_article = int(item.is_article)

        if item.word_count:
            add_tag(item, reading_time(item.word_count // words_per_minute))

        elif not item.is_article:
            add_tag(item, 'not an article')
