"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Display recommendations in a clean, readable format
    print("\n" + "="*70)
    print(f"TOP RECOMMENDATIONS FOR {user_prefs['genre'].upper()}/{user_prefs['mood'].upper()} PROFILE")
    print("="*70 + "\n")
    
    for rank, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        artist = song.get('artist', 'Unknown')
        print(f"{rank}. {song['title']} | {artist}")
        print(f"   Score: {score:.2f}")
        # Extract the reasons part (remove "Because: " prefix)
        reasons = explanation.replace("Because: ", "")
        print(f"   Reasons: {reasons}")
        print()


if __name__ == "__main__":
    main()
