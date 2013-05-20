# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

from twitter import Twitter, OAuth


def get_tweets(hashtag="#finalcopatve"):
    """
    Gets tweets for a given hashtag
    :arg string hashtag: Twitter hashtag to get the tweets
    :returns: A list of Tweets.
    :rtype: list
    """
    try:
        import config

        t = Twitter(auth=OAuth(config.OAUTH_TOKEN, config.OAUTH_SECRET,
                               config.CONSUMER_KEY, config.CONSUMER_SECRET))
        tweets = t.search.tweets(q=hashtag)
        return tweets['statuses']
    except:
        raise Exception("config.py file not found, please copy config.py.template \
                        to config.py and fill in the OAuth parameters")
