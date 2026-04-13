# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatcher CLI 1.0**

A simple music recommender you use in the terminal. It suggests songs based on what genre, mood, and energy level you like.

---

## 2. Goal / Task  

**What does it do?**

The system takes a user's music taste (genre, mood, energy) and ranks all songs in the catalog to find the best matches. The "best" song is the one that scores highest based on how well it matches the user's preferences.

**Example:** If you say you like pop/happy/high-energy music, the recommender will score pop songs higher than jazz songs, happy songs higher than sad songs, and songs with high energy higher than calm songs.

---

## 3. Data Used  

**How many songs?** 17 songs (small dataset, just for learning).

**What information do we have about each song?**
- Genre (pop, lofi, rock, ambient, jazz, etc.)
- Mood (chill, happy, intense, sad, relaxed, etc.)
- Energy level (0 = very calm, 1 = very energetic)
- Also: title, artist, tempo, danceability, acousticness

**Dataset limits:**
- Lofi appears 3 times, but sad/angry/romantic appear only 1 time each
- No EDM or K-pop in the dataset
- Some mood + genre combinations don't exist (e.g., no reggae/happy song)

---

## 4. Algorithm Summary  

**How does it score songs? (in plain language, no code)**

For each song, we add up points:
- **+2.0 points** if the song's genre matches the user's favorite genre
- **+1.5 points** if the song's mood matches the user's favorite mood  
- **0 to +1.0 points** based on how close the song's energy is to the user's target energy

Then we sort songs from highest to lowest score and return the top recommendations.

**Simple example:** A pop/happy song with energy 0.82 is compared to a user who wants pop/happy/0.8:
- Genre match? Yes → +2.0
- Mood match? Yes → +1.5
- Energy closeness? 0.82 vs 0.8 (very close) → +0.98
- **Total score: 4.48** (very good match!)

---

## 5. Observed Behavior / Biases  

**The main problem we found: Rare Moods Get Ignored**

Since our dataset has only 1 sad song but 3 chill songs, users who like sad/angry/romantic music get systematically lower scores than users who like chill/happy music. A sad-music lover will rarely earn the +1.5 mood bonus, while chill-music lovers earn it almost every time.

**Other biases:**
- If you ask for a genre not in the dataset (like EDM), you can never get the +2.0 genre bonus
- The dataset's average energy is 0.61 (moderate), so very calm or very energetic users have fewer good matches
- Some combinations don't exist (metal + chill), so those users get worse recommendations

---

## 6. Evaluation Process  

**How did we test it?**

We created 6 different user profiles and ran the recommender on each:
1. High-Energy Pop (standard preference)
2. Chill Lofi (low-energy preference)
3. Deep Intense Rock (contrasting preference)
4. Contradictory Profile (high energy + sad mood = conflicting)
5. Unknown Genre (requested a genre not in dataset)
6. Ambient Relaxation (niche combination)

**What did we check?**
- Do the top results feel right? (Yes, pop users got pop songs, lofi users got lofi, etc.)
- Do different profiles get different winners? (Yes—Sunrise City, Library Rain, Storm Runner, etc.)
- Does it break on weird inputs? (No, it handles unknown genres gracefully)

**Sensitivity experiment:** We doubled the energy weight and halved the genre weight. Rankings stayed mostly stable, which proved our original weights were solid.

---

## 7. Intended Use and Non-Intended Use  

**What it's DESIGNED for:**
- Teaching students how scoring algorithms work
- Exploring how weighting choices affect recommendations
- Testing edge cases and biases in naive algorithms
- Small classroom projects

**What it's NOT designed for:**
- Real music streaming apps (too small and biased)
- Making business decisions about music curation  
- Recommending music to millions of actual users
- Handling complex or nuanced user preferences

---

## 8. Ideas for Improvement  

**What we'd add if we kept building this:**

1. **Bigger dataset:** Include 1,000+ songs with balanced genres/moods. This would fix the rare-mood filter bubble.

2. **More features:** Use danceability, valence (positivity), and acousticness in the scoring. Let users control which features matter most.

3. **Diversity:** Make sure the top-5 results don't all come from the same genre or artist. Give variety!

---

## 9. Personal Reflection  

**What we learned:**

This project showed us that small datasets create hidden biases you don't notice at first. We thought our system was fair, but it actually favored users with mainstream tastes (pop, happy, chill) over users with niche tastes (sad, metal, very low energy).

**The surprising part:** Doubling the energy weight didn't just shift scores—it actually changed which songs won! This proved our weighting choices are really important. Small tweaks create big differences.

**How it changed our thinking:** When we use Spotify or Netflix, there's probably bias hidden in their data too. If their dataset has 10× more pop songs, pop lovers will always win. Fair AI isn't just about the algorithm—it's about the data we feed it.

---  
