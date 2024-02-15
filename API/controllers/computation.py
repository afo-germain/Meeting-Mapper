import requests
import numpy as np
import pandas as pd

# Matrix output to xlsx file
writer = pd.ExcelWriter('origin-destination_matrix.xlsx', engine = 'xlsxwriter')

def get_optimal_meeting_location(users):
    """
    Calcule le lieu de rencontre optimal pour une liste d'utilisateurs.

    Args:
    users: Liste d'objets utilisateurs contenant leurs coordonnées.

    Returns:
    Le lieu de rencontre optimal sous forme d'objet.
    """

    # Calculer la matrice de distances
    distance_matrix = calculate_distance_matrix(users)
    
    # Calculer le centre de gravité
    center_of_gravity = calculate_center_of_gravity(users, distance_matrix)

    # Trouver le lieu le plus proche du centre de gravité
    meeting_location = find_closest_location(center_of_gravity)

    return meeting_location

def calculate_distance_matrix(users):
    """
    Calcule la matrice de distances entre tous les utilisateurs.

    Args:
    users: Liste d'objets utilisateurs contenant leurs coordonnées.

    Returns:
    Une matrice carrée de distances.
    """
    n = len(users)
    matrix = [[None] * n for _ in range(n)]
        
    for i in range(n):
        for j in range(n):
            if i != j:
                coord_i = [users[i]['longitude'], users[i]['latitude']]
                coord_j = [users[j]['longitude'], users[j]['latitude']]
                route_info = get_osrm_route(coord_i, coord_j)
                
                if route_info:
                    matrix[i][j] = round(route_info['distance'] / 1000, 2) 
                    """{
                        'distance': round(route_info['distance'] / 1000, 2), # Convert in km
                        #'duration': round(route_info['duration'] / 60, 2), # Convert in mn
                    }"""
            else: 
                matrix[i][j] = 0
                """{
                    'distance': 0,
                }"""
                
    # Write in Excel file
    df2 = pd.DataFrame(matrix)
    df2.to_excel(writer, sheet_name = 'Origin-destination')
    writer.close()
    
    return matrix

# Compute the distance and duration of two coordinates
def get_osrm_route(coord1, coord2):
    # Open Source Route Machine API (Computation of distance and duration)
    # Format des coordonnées : [longitude, latitude]
    url = f"http://router.project-osrm.org/route/v1/driving/{coord1[0]},{coord1[1]};{coord2[0]},{coord2[1]}"
    response = requests.get(url)
    
    if response.status_code == 200:
        route_data = response.json()
        return route_data['routes'][0] if route_data['code'] == 'Ok' and len(route_data['routes']) > 0 else None
    else:
        return None

def calculate_center_of_gravity(users, distance_matrix):
    """
    Calcule le centre de gravité d'une matrice de distances.

    Args:
    distance_matrix: Matrice carrée de distances.

    Returns:
    Le centre de gravité sous forme de tuple (latitude, longitude).
    """
    
    # Calculation of weight
    weight = np.sum(distance_matrix, axis=1) # / np.sum(distance_matrix)    

    long = sum(w * user['longitude'] for user, w in zip(users, weight)) / sum(weight)
    lat = sum(w * user['latitude'] for user, w in zip(users, weight)) / sum(weight)
    
    return {'longitude': long, 'latitude': lat}

def find_closest_location(center_of_gravity):
    """
    Trouve le lieu le plus proche d'un point donné.

    Args:
    center_of_gravity: Point de référence (latitude, longitude).

    Returns:
    Le lieu le plus proche sous forme d'objet.
    """
    
    url = f"https://nominatim.openstreetmap.org/reverse?lat={center_of_gravity['latitude']}&lon={center_of_gravity['longitude']}&format=json&type=amenity"
    response = requests.get(url)
    
    if response.status_code == 200:
        address = response.json()
    else:
        return None

    return address