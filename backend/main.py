import spotify
import lyrics
import utils

from dotenv import load_dotenv
import os


SPOTIFY_ACCESS_TOKEN = utils.get_access_token()


def main():
    get_recommendations_in_language(playlist_id='7sUcocXdBtRDrMqV07gnX9', language='he')


def get_recommendations_in_language(playlist_id: str, language: str) -> set[str]:
    """get recommended songs in the target language

    Args:
        playlist_id (str): spotify id of the playlist
        language (str): in the following format: English -> en

    Returns:
        set[str]: set of recommendations
    """
    # TODO: document if the output is of ids or names

    load_dotenv()

    all_recommendations = spotify.get_recommendations(access_token=SPOTIFY_ACCESS_TOKEN, playlist_id=playlist_id)

    out = set()
    for recommendation in all_recommendations['tracks']:
        filtered = lyrics.get_song_in_language(api_key=os.getenv('LYRICS_API_KEY'), name=recommendation['name'], language=language)
        if filtered is None:
            continue
        out.add(recommendation['name'])
    print(out)



if __name__ == '__main__':
    main()