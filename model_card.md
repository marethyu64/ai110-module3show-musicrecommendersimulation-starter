# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**MusicRecs 1.0**

---

## 2. Goal / Task  

This system gets the user's taste in music based on genre, music, and energy, then ranks all songs in the catalog to find the best match. The best match is the song that scores the highest based on how well it fits the user's preferences.

---

## 3. Data Used  

We used a dataset of 17 songs with their listed genre, mood, energy level, title, artist, tempo, danceability, and acousticness. The limit of the dataset was we only had 17 songs to go off of, so there were some cases where sad/angry/romantic songs only appeared 1 time each, which limited the recommendations.

---

## 4. Algorithm Summary  

We scored the songs by adding up points. If the song's genre matched the user's favorite genre, it receives 2 points. If the song's mood matches, it receives 1.5 points. The song will also receive a range of 0 to 1 points depending on how close its energy is to the user's favorite energy.

---

## 5. Observed Behavior / Biases  

The main problem we found was rare moods would get ignored. For instance, our dataset only has 1 sad song but 3 chill songs. AS a result, users who like sad/angry/romantic music always get lower match scores than users who like chill/happy music.

---

## 6. Evaluation Process  

I testesd this by creating 6 different user profiles and running the recommender on each user.

1. High-Energy Pop (standard preference)
2. Chill Lofi (low-energy preference)
3. Deep Intense Rock (contrasting preference)
4. Contradictory Profile (high energy + sad mood = conflicting)
5. Unknown Genre (genre not in dataset)
6. Ambient Relaxation (niche combination)

From reviewing the results, I concluded the top results felt right, with pop users getting pop songs, lofi users getting lofi songs, etc. Different profiles did get different top results, and the system was able to handle weird/unknown genre inputs,

For an experiment, I doubled the energy level weight and cut the genre weight value in half. The raknings were mostly stable, meaning our original weights were solid.

---

## 7. Intended Use and Non-Intended Use  

This system is designed for learning how scoring algorithms work and experimenting with how weight values affect recommendations. For a user's case, this system would be used to recommend songs with general recommendations, but isn't practical due to its lack of data.

This system is not designed for actual recommendation algorithms, since it's very simple and lacking in data.

---

## 8. Ideas for Improvement  

If I kept building this, I would like to add a lot more data, perhaps over a thousand to ensure all user preferences are covered. In addition, I'd like to give the user the ability to modify the system, adding more weight on values they value more like genre, energy, etc.

---

## 9. Personal Reflection  


My biggest learning moment during this project was learning how small datasets can create hidden biases due to lack of data. I thought my system was functional for all users, but it actually favors users with popular tastes (ones most prevalent in the dataset) such as pop, happy, or chill.

AI tools helped me in quickly breaking down concepts for me, generating, and debugging code. I needed to double-check its output whenever possible to assure myself I knew what was going on.

What surprised me about how simple algorithms can still "feel" like recommendations was that changing the weight values, such as doubling the energy weight, actually changed which songs won, showing how important the choice of weight values are. My system's recommendations could have drastic differences if the weights are slightly modified.

If I could extend this project, I'd like to add more data and experiment with a different type of recommendation system, comparing which ones are better.

---  
