# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatcher CLI 1.0** — A command-line music recommender that scores songs based on categorical (genre, mood) and numerical (energy) user preferences.

---

## 2. Intended Use  

This CLI-first recommender is designed for **classroom exploration and algorithm validation** rather than production music streaming. It assumes users can express their taste as a combination of (1) favorite genre, (2) preferred mood, and (3) target energy level on a 0-1 scale. The system generates ranked lists of top-k song recommendations by scoring each song in the catalog against the user profile. It is intended to teach scoring algorithms, ranking logic, and the practical implications of weighting design choices.

---

## 3. How the Model Works  

The recommender scores each song by awarding points for categorical matches and numerical closeness: **+2.0 for genre match**, **+1.5 for mood match**, and **0-1.0 for energy closeness** (calculated as max(0, 1 - |song_energy - user_target_energy|)). For example, a pop/happy song with energy 0.82 compared to a user preferring pop/happy/0.8 scores 4.48 (2.0 + 1.5 + 0.98). All songs are then scored, sorted descending, and the top k results are returned with transparent explanations of why each song ranked. The scoring equation is: **final_score = genre_bonus + mood_bonus + energy_component**.

---

## 4. Data  

The model uses a curated catalog of **17 songs** with attributes: id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. Genres include pop (2), lofi (3), rock, ambient, jazz, synthwave, indie pop, electronic, country, reggae, blues, metal, and classical. Moods cluster around chill (3), happy (2), and intense (2), with single instances of sad, melancholic, angry, romantic, nostalgic, euphoric, focused, and moody. Energy ranges from 0.25 (Moonlit Serenade) to 0.95 (Raging Fire) with mean 0.61. The dataset was not modified, representing a small teaching corpus rather than a production music library. Notable gaps: no EDM, no reggae/happy combination, very few sad or melancholic songs.

---

## 5. Strengths  

**Intuitive Ranking:** The system produces musically sensible results for "mainstream" profiles. High-Energy Pop users get Sunrise City (perfect match on all three dimensions), Chill Lofi users receive Library Rain and Midnight Coding (both exact mood + genre fits with ideal energy closeness), and Deep Intense Rock users find Storm Runner. **Robustness:** The system gracefully handles edge cases like unknown genres or conflicting preferences without crashing; the energy-closeness component provides a fallback ranking mechanism. **Transparency:** Every recommendation includes explicit breakdown of scoring reasons ("genre match +2.0, mood match +1.5, energy closeness +0.98"), enabling users to understand the algorithmic decision. **Sensitivity Testing:** Experimental weight shifts proved the original weighting is stable and balanced; doubling energy and halving genre caused unintended flips, validating the design.  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

**Critical Limitation: Small Dataset Creates Rare-Mood Filter Bubble**

The recommender system exhibits a significant bias toward frequently-occurring moods due to the small dataset size (17 songs with highly imbalanced mood distribution). Specifically, chill mood appears 3 times while romantic, nostalgic, angry, and sad moods each appear only once. This means users with preferences for underrepresented moods (e.g., users who like romantic or angry music) will almost never receive the +1.5 mood match bonus, resulting in systematically lower recommendation scores compared to chill/happy preference users. Additionally, when a user requests a genre not present in the catalog (such as EDM or progressive-metal), they never achieve the +2.0 genre match bonus regardless of other quality factors, creating an "invisible penalty" for minority taste profiles. The energy-gap calculation also inadvertently favors moderate-energy users; the dataset mean energy is 0.61, so users seeking very low energy songs (0.1-0.3) will find fewer close matches in the catalog, while high-energy preferences (0.8+) benefit from better dataset coverage. Users with rare combinations (e.g., metal + chill) are effectively ignored because these pairings don't exist in the training data.

---

## 7. Evaluation  

Tested six distinct user profiles: (1) High-Energy Pop (baseline), (2) Chill Lofi (niche low-energy), (3) Deep Intense Rock (contrasting intensity), (4) Contradictory Profile with high energy + sad mood (stress test), (5) Unknown-Genre edge case (robustness test), and (6) Ambient Relaxation (genre-mood mismatch recovery). For each profile, verified that top-5 results matched musical intuition: pop/happy preferrers got pop songs, lofi fans got lofi songs, rock fans got rock. Confirmed that different profiles produced different top-1 winners (Sunrise City, Library Rain, Storm Runner, Gym Hero, etc.), proving the system isn't dominated by dataset size quirks. Ran sensitivity experiment by doubling energy weight and halving genre weight; original rankings remained stable, confirming robust weighting. Verified graceful degradation: the contradictory and unknown-genre profiles still produced ranked output rather than errors.

---

## 8. Future Work  

**Expand dataset** to include hundreds of songs covering underrepresented genres (EDM, K-pop, metal) and rare mood-genre combinations to reduce filter-bubble risk. **Add more scoring dimensions** like danceability, valence (positivity), and acousticness to enable richer preference expression. **Implement diversity penalties** so that top-k results don't all come from the same artist or genre, providing more exploration. **Build user feedback loop** allowing users to rate recommendations and adjust weights (e.g., "I love this but want more variety" could reduce genre weight). **Develop cold-start heuristics** for new genres and moods with single samples by considering feature-space neighbors. **Create preference elicitation UI** so users can explore the weighting tradeoffs interactively (e.g., sliders for genre/mood/energy importance) rather than submitting fixed dictionaries.  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
