import requests

def tiktok_stalk(username):
    try:
        url = f'https://tools.revesery.com/stalktk/revesery.php?username={username}'
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()

        if 'base64' in data:
            del data['base64']

        return data
    except requests.exceptions.HTTPError as http_err:
        return {'error': f'HTTP error occurred: {http_err}'}
    except requests.exceptions.RequestException as req_err:
        return {'error': f'Request error occurred: {req_err}'}
    except ValueError as json_err:
        return {'error': f'JSON decode error occurred: {json_err}'}
    except Exception as e:
        return {'error': str(e)}