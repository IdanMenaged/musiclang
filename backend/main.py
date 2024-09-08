import requests
from constants import *

def get_playlist(access_token: str, playlist_id: str) -> dict[str, str]:
    url = f'{API_URL}/playlists/{playlist_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if (response.status_code != 200):
        raise Exception(response.json())
    return response.json()


def get_recommendations(access_token: str, playlist_id: str):
    playlist = get_playlist(access_token, playlist_id)
    tracks = playlist['tracks']
    
    formatted_tracks = ''
    for i in tracks['items'][:MAX_RECOMMENDATION_SEEDS]:
        formatted_tracks += f',{i['track']['id']}'
    formatted_tracks = formatted_tracks[1:]

    url = f'{API_URL}/recommendations?seed_tracks={formatted_tracks}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.json())
    return response.json()


if __name__ == '__main__':
    import utils
    
    t = utils.get_access_token()
    print(get_recommendations(t, '1r37MxSmlelGq3LJCmT907'))