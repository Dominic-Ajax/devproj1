import requests

def get_nearby_attractions(api_key, latitude, longitude, radius=1000, place_type='tourist_attraction'):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f"{latitude},{longitude}",
        'radius': radius,
        'type': place_type,
        'key': api_key
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        results = response.json().get('results', [])
        attractions = []
        
        for place in results:
            name = place.get('name')
            address = place.get('vicinity')
            rating = place.get('rating')
            attractions.append({
                'name': name,
                'address': address,
                'rating': rating
            })
        
        return attractions
    else:
        print(f"Error: {response.status_code}")
        return []
