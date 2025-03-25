import os
import time
import random
from pathlib import Path

import schedule
from mastodon import Mastodon

def ensure_env(key: str) -> str:
    """Get the value of a required environment variable."""
    if key not in os.environ:
        raise RuntimeError(f'Environment variable `{key}` not provided.')
    return os.environ[key]

DEBRIEF_QUOTES_FILE = Path.cwd() / 'data/debrief_quotes.txt'

CLIENT = Mastodon(
    client_id=ensure_env('CLIENT_KEY'),
    client_secret=ensure_env('CLIENT_SECRET'),
    access_token=ensure_env('ACCESS_TOKEN'),
    api_base_url=ensure_env('API_BASE')
)

def random_line(file: Path) -> str:
    """Read a random line from a text file."""
    with file.open('r') as stream:
        stream.seek(random.randrange(file.stat().st_size))
        stream.readline()  # discard
        line = stream.readline()
        if len(line) == 0:
            stream.seek(0)
            line = stream.readline()
    return line.strip()

def post() -> None:
    """Post a random line as a Mastodon toot."""
    line = random_line(DEBRIEF_QUOTES_FILE)
    print(f'Random line: {line!r}')
    CLIENT.toot(f"{line}\n\n#Severance")

schedule.every().day.at('00:00', tz='Europe/Berlin').do(post)
schedule.every().day.at('10:00', tz='Europe/Berlin').do(post)
schedule.every().day.at('18:00', tz='Europe/Berlin').do(post)

if __name__ == '__main__':
    post()
    while True:
        schedule.run_pending()
        sleep = schedule.idle_seconds()
        if sleep is None:
            raise RuntimeError("Got `None` from `idle_seconds()`?")
        print(f"Sleeping for {sleep} seconds....")
        time.sleep(sleep)
