#!/usr/bin/env python

"""Scrape PyCon UK's youtube channel for videos and link them in the session.

Fragile regular expressions are used for parsing the youtube channel and the
session files. Use only with care and version control!

Without third party libraries only few videos can be retrieved from youtube.
Youtube's official API is not used to avoid need of user credentials. If
youtbe-dl is installed, all videos are found (but it is not very fast).

Matching videos to sessions is done via a poor-man fuzzy match. A title
identifier is created by stripping all characters from title except a-z and A-Z
and converting to lower case. This identifier is used for matching videos
and sessions.

TODO:
 - improve fuzzy matching
 - options via argparse

"""

import re
import time
import logging
from glob import iglob
from urllib.request import urlopen

try:
    import youtube_dl
    use_youtube_dl = True
except ImportError:
    use_youtube_dl = False


YOUTUBE_URI = 'https://www.youtube.com/channel/UChA9XP_feY1-1oSy2L7acog/videos'
YOUTUBE_TITLE_PREFIX = 'PYCON UK 2017'
YOUTUBE_URI_PREFIX = 'https://www.youtube.com'
YOUTUBE_REGEX = '<a .* href="(.*)">{prefix}: (.*)</a>'.format(
    prefix=YOUTUBE_TITLE_PREFIX)

SESSION_FILES = './sessions/**/*.md'

# title might contain quotes, they get stripped in title_identifier() anyway
TITLE_REGEX = 'title: (.*)'


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] - %(message)s')


def title_identifier(title):
    """See module docstring."""
    title_id = re.sub('[^a-zA-Z0-9]', '', title).lower()
    title_id = re.sub('keynote', '', title_id)
    return title_id


def retrieve_youtube_videos_poor_man():
    with urlopen(YOUTUBE_URI) as response:
        # TODO hardcoded encoding might not be the best idea
        html = response.read().decode('utf-8')
    return {title_identifier(title): YOUTUBE_URI_PREFIX + uri
            for uri, title in re.findall(YOUTUBE_REGEX, html)}


def retrieve_youtube_videos_youtube_dl():
    logging.info("Downloading information from youtube (this might take a few "
                 "minutes)...")
    with youtube_dl.YoutubeDL({}) as ydl:
        videos = ydl.extract_info(YOUTUBE_URI, download=False)

    def strip_prefix(title):
        return title[len(YOUTUBE_TITLE_PREFIX) + 2:]

    return {
        title_identifier(strip_prefix(video['title'])): video['webpage_url']
        for video in videos['entries']
        if video['title'].startswith(YOUTUBE_TITLE_PREFIX)
    }


def retrieve_youtube_videos():
    """Download list of youtube videos from channel and return a dictionary of
    the form {title_identifier: video_uri}."""
    if use_youtube_dl:
        return retrieve_youtube_videos_youtube_dl()
    else:
        return retrieve_youtube_videos_poor_man()


def main():
    t0 = time.time()

    youtube_videos = retrieve_youtube_videos()

    logging.info("Found %d links to youtube videos in channel.",
                 len(youtube_videos))

    no_video_found = []
    videos_added = []
    video_already_there = []

    for fname in iglob(SESSION_FILES, recursive=True):
        with open(fname, 'r') as f:
            session_content = f.read()

        title = re.search(TITLE_REGEX, session_content)
        if not title:
            logging.error("No title found in %s", fname)
            continue

        title = title.groups()[0]

        title_id = title_identifier(title)
        youtube_uri = youtube_videos.pop(title_id, None)

        if not re.search('video:( )*\n', session_content):
            # TODO check if there is really a link already and if it is
            # identical to scraped link
            video_already_there.append(title)
            continue

        if youtube_uri is None:
            no_video_found.append(title)
            continue

        session_content = re.sub('video:( )*\n', 'video: {}\n'.format(
            youtube_uri), session_content)

        # TODO this is not safe, should write to tmp file first, but it is a
        # GIT repository anyway...

        logging.debug("Adding video link %s to session file %s...",
                      youtube_uri, fname)
        with open(fname, 'w') as f:
            # video already there?
            f.write(session_content)

        videos_added.append(title)

    logging.info("Added %d video links to sessions.", len(videos_added))
    logging.info("%d video links were already there.", len(video_already_there))
    logging.info("No video found for %d sessions.", len(no_video_found))
    if len(youtube_videos):
        # this prints the title identifier, which is a bit ugly
        no_session = "\n".join("    {}: {}".format(title_id, uri)
                               for title_id, uri in youtube_videos.items())
        logging.error("No session file found for %d videos:\n%s",
                      len(youtube_videos), no_session)

    logging.info("Scraping took %s seconds.", time.time() - t0)


if __name__ == '__main__':
    main()
