import concurrent.futures
import slack_bolt
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests
import asyncio

SLACK_BOT_TOKEN = ""
SLACK_SIGNING_SECRET = ""
SLACK_APP_TOKEN = ""

app = slack_bolt.App(token=SLACK_BOT_TOKEN)

WEBSITES = {
    "Google": "https://www.google.com",
    "Example": "https://www.example.com",
    "My API": "https://test.example.com",
}

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()