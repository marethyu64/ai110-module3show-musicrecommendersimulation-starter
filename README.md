# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world music recommendation systems like Spotify combine collaborative filtering (analyzing user behavior patterns) with content-based filtering (matching song attributes) to predict preferences, often using machine learning for personalization. My simplified version prioritizes content-based filtering, focusing on numerical audio features to compute similarity scores, as this approach is interpretable and works well for small datasets without requiring user interaction data.

### Song Object Features
- id (unique identifier)
- title (song name)
- artist (performer)
- genre (e.g., pop, lofi, rock)
- mood (e.g., happy, chill, intense)
- energy (0-1 scale for intensity)
- tempo_bpm (beats per minute)
- valence (0-1 scale for emotional positivity)
- danceability (0-1 scale for dance suitability)
- acousticness (0-1 scale for acoustic vs. electronic)

### UserProfile Object Features
- preferred_genre (string, e.g., "pop")
- preferred_mood (string, e.g., "chill")
- preferred_energy (float, 0-1)
- preferred_valence (float, 0-1)
- preferred_danceability (float, 0-1)
- preferred_acousticness (float, 0-1)

### Scoring Algorithm Recipe

The Recommender uses a **point-weighting strategy** that combines categorical matching (exact matches) with continuous similarity scoring (distance-based):

#### **Base Points (Categorical Matching)**
- **Genre Match:** +2.0 points
  - Exact match between user's preferred_genre and song's genre
  - Rationale: Genre is the strongest indicator of music preference and sets user expectations
  
- **Mood Match:** +1.0 point
  - Exact match between user's preferred_mood and song's mood
  - Rationale: Mood is important but more flexible than genre (users may listen to pop in different moods)

#### **Continuous Similarity Points**
- **Energy Similarity:** +2.0 points (max)
  - Formula: `2.0 × (1 - |user_energy - song_energy|)`
  - Why: Energy significantly impacts listening experience; close proximity = higher score
  
- **Valence Similarity:** +1.5 points (max)
  - Formula: `1.5 × (1 - |user_valence - song_valence|)`
  - Why: Emotional tone (positivity) should align with user preference
  
- **Danceability Bonus:** +1.0 point (max)
  - Formula: `song_danceability × 1.0` (applied if user indicates danceability preference)
  - Why: Nice-to-have bonus for upbeat, groove-oriented tracks

#### **Total Score Calculation**
```
TOTAL SCORE = Genre_Points + Mood_Points + Energy_Points + Valence_Points + Danceability_Points
MAXIMUM POSSIBLE SCORE: 8.5 points
NORMALIZED SCORE (0-1): Total_Score / 8.5
```

#### **Output**
- Songs are scored individually, then sorted by total score in descending order
- Top K songs (e.g., top 5) are returned as ranked recommendations
- Each recommendation includes the song's title, artist, score, and relevance explanation

### Expected Biases and Limitations

⚠️ **Over-prioritizes Genre (2.0 vs 1.0 for mood):**
- The system may ignore excellent songs that match the user's mood but not their genre
- Example: A user preferring "pop" and "happy" would never see a "rock" song with 0.95 valence, even if it's musically compatible
- **Mitigation:** Consider reducing genre weight to 1.5 or adding a "genre flexibility" parameter for discovery mode

⚠️ **Binary Genre/Mood Matching:**
- A song with genre="indie pop" won't match a user with preferred_genre="pop" (exact match only)
- Real systems use genre hierarchies or similarity measures
- **Mitigation:** Could implement fuzzy matching or genre families (e.g., "indie pop" ⊂ "pop")

⚠️ **Ignores Implicit Patterns:**
- The system doesn't learn from user listening history or detect that "pop + happy + high energy" usually works well together
- It treats each feature independently without interaction effects
- **Mitigation:** Future improvements could add feature interactions or use collaborative filtering

⚠️ **Small Dataset & Limited Features:**
- With only 17 songs and 10 attributes, the system cannot capture nuanced preferences
- Missing features: lyrics, artist, similar artists, release date, user history
- **Mitigation:** Expand dataset and add temporal/social features

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

