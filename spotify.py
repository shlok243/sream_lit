import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace these with your Spotify API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# Authenticate
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Streamlit App
st.title("Spotify Track Search")

query = st.text_input("Enter the name of the song or artist:")

if st.button("Search"):
    if query:
        results = sp.search(q=query, type='track', limit=5)
        if results['tracks']['items']:
            for idx, track in enumerate(results['tracks']['items']):
                st.write(f"**Track Name**: {track['name']}")
                st.write(f"**Artist**: {track['artists'][0]['name']}")
                st.write(f"**Album**: {track['album']['name']}")
                st.write(f"[Preview Link]({track['external_urls']['spotify']})")
                st.write("-" * 50)
        else:
            st.write("No tracks found. Please try a different search query.")
    else:
        st.write("Please enter a search query.")

st.write("\nSearch for your favorite tracks and get links to listen on Spotify!")
