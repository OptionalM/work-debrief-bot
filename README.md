# Work Debrief Bot

A Mastodon bot, written in Python, that will post random lines from
`data/debrief_quotes.txt`.

Currently posts at 10AM, 6PM, and 12PM (in the `Europe/Berlin` timezone) at [@work_debrief@infosec.exchange](https://infosec.exchange/@work_debrief).

Forked from [Sidneys1/wellness-session-bot](https://github.com/Sidneys1/wellness-session-bot).

## Configuration

Configured via these environment variables:
<dl>
    <dt><code>CLIENT_KEY</code></dt>
    <dd>Mastodon API Key.</dd>
    <dt><code>CLIENT_SECRET</code></dt>
    <dd>Mastodon API Secret.</dd>
    <dt><code>ACCESS_TOKEN</code></dt>
    <dd>Mastodon API token.</dd>
    <dt><code>API_BASE</code></dt>
    <dd>Mastodon API base URL (e.g., <code>https://mastodon.social</code>).</dd>
</dl>

You can get the API values from the Mastodon settings:
1. Register a Mastodon account.
2. In the Mastodon web interface, navigate to <kbd><kbd>Preferences</kbd> &rarr; <kbd>Development</kbd></kbd>.
   * Create an application as necessary. The only scopes currently required are
     `profile` and `write:statuses`.
3. Open your application, the "Client key", "Client secret", and "Your access
   token" will be displayed at the top of that page.

## Running

To run manually (optionally create a virtual environment) by installing the 
prerequisites (`python3 -m pip install -r requirements.txt`) and running
`python3 debrief.py`.

<details><summary>With Docker/Podman</summary>

To run in containers you can use the `docker.io/optional/debrief_bot` image 
(replace `podman` with `docker` as necessary):

```sh
# Fill .env with the configuration environment variables above as necessary.
touch .env

podman run --detach --name work-debrief-bot --env-file=.env docker.io/optional/debrief_bot

# To stop
podman stop work-debrief-bot

# To remove
podman rm work-debrief-bot
```

</details>

<details><summary>With Docker/Podman Compose</summary>

See [`compose.yml`](./compose.yml) for an example Compose configuration (replace
`podman compose` with `docker compose` as necessary).

```sh
# Fill .env with the configuration environment variables above as necessary.
touch .env

podman compose up

# To stop
podman compose stop

# To remove
podman compose rm
```

</details>

## Building

To build the Docker/Podman image (replace `podman compose` with `docker compose`
as necessary):

```sh
podman compose build
```
