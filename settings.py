import os

COMMAND_PREFIX = "'"
BOT_TOKEN = os.getenv('BOT_TOKEN')
NOW_PLAYING = "Stalker | 'commands"
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

#Silencer
BLACKLIST=["404370425804488704"]
QUOTES=["Utkaj łeb Jobczyk!",
        "Mówiłem żebyś skleił pizde Jobo.",
        "Dobra wez pal wroty Jobo...",
        "W pizde se klaśnij.",
        "Ogul se pachy ziomuś.",
        "*Quack Quack* Twoja matka pali crack Jobo."]

TYPING=["Nawet nie próbuj tego wysyłać Jobo!",
        "O pies zaczyna szczekać.",
        "Znowu Jobo coś pisze."]

#Spotify Addon
SPOTIFY_USERNAME = "happyyoko"
SPOTIFY_PLAYLIST_ID ="4KBdUHSszgkRJTUzUKA0Ho"
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_TOKEN = os.getenv('SPOTIFY_TOKEN')

#Admin List

ADMIN=["247125162472767488"]
