def get_spn(json_response: dict):
    k = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    a1, a2 = list(map(float, k['lowerCorner'].split()))
    b1, b2 = list(map(float, k['upperCorner'].split()))
    return b1 - a1, b2 - a2
