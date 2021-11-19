HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["16184901"])
    API_HASH = environ["fa54b34efb7d52516e8b5ae7f32ceb8d"]
    SESSION_STRING = environ[
        "AQDBEfR9tZBD3RVfCn-eJWHVLKJSY5pSe9etKKsBzueTzlLWqZcVIztmUEdCdgpYYDo2I45FJB-UEhjbbEdWfXYtii2lgzqGGKReXl9xMN4CwlVOnM9XS4bt4XfARnuIFvxUMjnqk29qtv4tgldglabU5N5i0PePXrQ3wWOUsmFP7SIGr2peYalVfO3bQJ9cFRW3oksPlHcjnctB3jBeOOgMS5g40epTbgYfGJWC1K2neDrgu-17G_7PpCM70dmwyYvlgQ5CRDep9J6XY6XlKPEVF3rGOckSdNAv5yScxVc5fR3RPv35dCohlCoHPakwklEd0AAZjzlJElQIWdZeYreye_qCUgA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["KOBZLP-NWVBHG-MBLNSC-PLJNMR-ARQ"]
    CHAT_ID = int(environ["-1001439224033"])
    DEFAULT_SERVICE = environ.get("saavn") or "youtube"
    BITRATE = int(environ["512"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"
