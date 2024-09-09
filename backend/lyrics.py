import requests
from constants import *


def get_song_in_language(api_key: str, name: str, language: str, verbose: bool = True) -> dict:
    """get the song

    Args:
        api_key (str): api key
        name (str): name of track
        language (str): in the following format: English -> en, Italien -> it
        verbose (str): whether to print if a song is in the language or is not

    Returns:
        dict: track object
    """

    url = f'{LYRICS_API_URL}/track.search'
    params = {
        'apikey': api_key,
        'q_track': name,
        'f_lyrics_language': language
    }

    response = requests.get(url, params)
    if response.status_code != 200:
        raise Exception(response.json())
    if response.json()['message']['body']['track_list'] == []:
        if verbose:
            print(f'song "{name}" is not in language "{language}"')
        return None
    if verbose:
        print(f'found song: "{name}"')
    return response.json()['message']['body']['track_list'][0]['track']


def get_lyrics(api_key: str, commontrack_id: str) -> dict:
    url = f'{LYRICS_API_URL}/track.lyrics.get'
    params = {
        'apikey': api_key,
        'commontrack_id': commontrack_id
    }

    response = requests.get(url, params)
    if response.status_code != 200 :
        raise Exception(response.json())
    if response.json()['message']['header']['status_code'] != 200:
        raise Exception(response.json()['message']['header'])  # TODO: make consistent with rest of errors
    return response.json()['message']['body']['lyrics']


if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_key = os.getenv("LYRICS_API_KEY")

    song = get_song_in_language(api_key=api_key, name='Shape of You', language='en')

    if song is not None:
        lyrics = get_lyrics(api_key, song['commontrack_id'])
        print(lyrics['lyrics_body'])
    