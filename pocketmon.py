"""
Add reading time tags to each article on Pocket.
"""

import logging

import pocket

from config import (
    consumer_key,
    access_token,
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



if __name__ == '__main__':
    api = pocket.Api(consumer_key=consumer_key,
                     access_token=access_token)

    items = api.get(sort='newest', state='unread', tag='_untagged_',
                    detailType='complete')

    for item in items:

        item.word_count = int(item.word_count)
        item.is_article = int(item.is_article)

        if item.word_count:
            # Add tag for minutes
            pass

        elif not item.is_article:
            # Add tag 'not an article'
            pass
