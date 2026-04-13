"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


# Define distinct user preference profiles
USER_PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9
    },
    "Contradictory Profile (High Energy + Sad)": {
        "genre": "pop",
        "mood": "sad",
        "energy": 0.95
    },
    "Edge Case (Unknown Genre)": {
        "genre": "unknown_genre",
        "mood": "happy",
        "energy": 0.5
    },
    "Ambient Relaxation": {
        "genre": "ambient",
        "mood": "relaxed",
        "energy": 0.2
    }
}


def print_recommendations(profile_name: str, user_prefs: dict, recommendations: list) -> None:
    """Display recommendations in a clean, readable format."""
    print("\n" + "="*70)
    print(f"TOP RECOMMENDATIONS FOR '{profile_name}'")
    print(f"User Preferences: Genre={user_prefs['genre']}, Mood={user_prefs['mood']}, Energy={user_prefs['energy']}")
    print("="*70 + "\n")
    
    if not recommendations:
        print("No recommendations found.\n")
        return
    
    for rank, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        artist = song.get('artist', 'Unknown')
        print(f"{rank}. {song['title']} | {artist}")
        print(f"   Score: {score:.2f}")
        reasons = explanation.replace("Because: ", "")
        print(f"   Reasons: {reasons}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}\n")

    # Test each profile
    for profile_name, user_prefs in USER_PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(profile_name, user_prefs, recommendations)


if __name__ == "__main__":
    main()
