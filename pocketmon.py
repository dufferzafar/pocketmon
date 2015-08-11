"""
Add reading time tags to each article on Pocket.
"""

import pocket

from config import (
    consumer_key,
    access_token,
)


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
