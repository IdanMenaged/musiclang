import requests
from constants import *

def get_playlist(access_token: str, playlist_id: str) -> dict[str, str]:
    url = f'{SPOTIFY_API_URL}/playlists/{playlist_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if (response.status_code != 200):
        raise Exception(response.json())
    return response.json()


def get_recommendations(access_token: str, playlist_id: str) -> dict[str, str]:
    playlist = get_playlist(access_token, playlist_id)
    tracks = playlist['tracks']
    
    formatted_tracks = ''
    for i in tracks['items'][:MAX_RECOMMENDATION_SEEDS]:
        formatted_tracks += f',{i['track']['id']}'
    formatted_tracks = formatted_tracks[1:]

    url = f'{SPOTIFY_API_URL}/recommendations?seed_tracks={formatted_tracks}&limit={LIMIT}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.json())
    return response.json()


def tracks_to_names(tracks: dict) -> set[str]:
    """translates a `tracks` object to a list of song names

    Args:
        tracks (dict): a `tracks` object

    Returns:
        set[str]: list of song names
    """
    out = set()
    for track in tracks['tracks']:
        out.add(track['name'])
    return out


def get_songs(access_token: str, ids: set[str]) -> list[dict[str, str]]:
    formatted_ids = ','.join(ids)
    
    url = f'{SPOTIFY_API_URL}/tracks'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'ids': formatted_ids
    }

    response = requests.get(url=url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(response.json())
    return response.json()


if __name__ == '__main__':
    import utils
    
    t = utils.get_access_token()
    recommendations = get_recommendations(t, '1r37MxSmlelGq3LJCmT907')
    print(tracks_to_names(recommendations))