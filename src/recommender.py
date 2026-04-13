from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

# Define a specific taste profile for the recommender
taste_profile = {
    'favorite_genre': 'rock',
    'favorite_mood': 'intense',
    'target_energy': 0.9,
    'target_tempo_bpm': 150,
    'target_valence': 0.5,
    'target_danceability': 0.7,
    'target_acousticness': 0.1
}

@dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numerical values to float/int."""
    import csv
    songs = []
    with open(csv_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert numerical values
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song based on genre, mood, and energy preferences."""
    score = 0.0
    reasons = []
    
    # Genre match: +2.0 points
    if song['genre'] == user_prefs.get('genre'):
        score += 2.0
        reasons.append("genre match (+2.0)")
    
    # Mood match: +1.5 points
    if song['mood'] == user_prefs.get('mood'):
        score += 1.5
        reasons.append("mood match (+1.5)")
    
    # Energy score: add closeness (1 - abs(diff)) * 1.0
    if 'energy' in user_prefs:
        energy_diff = abs(song['energy'] - user_prefs['energy'])
        energy_score = max(0, 1 - energy_diff) * 1.0
        score += energy_score
        reasons.append(f"energy closeness ({energy_score:.2f})")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by score, highest to lowest."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "Because: " + ", ".join(reasons) if reasons else "No matching preferences"
        scored_songs.append((song, score, explanation))
    
    # Sort by score descending
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    
    # Return top k
    return scored_songs[:k]
