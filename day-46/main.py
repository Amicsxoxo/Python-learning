import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --- 1. SCRAPE BILLBOARD 100 ---
date = input("Which date are you searching for e.g(YY-MM-DD): ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

print("Scraping Billboard Hot 100...")
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")

song_tag_list = soup.select(selector="li ul li h3")

# Clean up the scraped text 
song_list = [song.getText().strip() for song in song_tag_list]
print(f"Successfully scraped {len(song_list)} songs.")

# --- 2. SET UP SPOTIPY AUTHENTICATION ---
# NOTE: Make sure you delete 'token.txt' from your folder before running this!
CLIENT_ID = "1e8223f3b4974c5e855fe6d3013abcdc"
CLIENT_SECRET = "ae04bfa694e04b64bc09704a41c8189d"

# --- 2. SET UP SPOTIPY AUTHENTICATION ---
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:8888/callback",
        client_id=CLIENT_ID,          
        client_secret=CLIENT_SECRET,  
        show_dialog=True,
        cache_path="token.txt" 
    ),
    requests_timeout=20,  # <-- Tell Spotipy to wait up to 20 seconds
    retries=5             # <-- Tell Spotipy to try 5 times before giving up
)

USER_ID = sp.current_user()["id"]
PLAYLIST_NAME = f"{date} Billboard 100"  

# --- 3. SEARCH FOR THE SONGS ---
track_uris = []
print(f"\n🔍 Searching Spotify for {len(song_list)} songs...")

for song in song_list:
    result = sp.search(q=f"track:{song}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(uri)
        print(f"✅ Found: {song}")
    except IndexError:
        print(f"❌ Not Found: {song}")

# --- 4. CREATE THE PLAYLIST ---
print(f"\n✨ Creating playlist '{PLAYLIST_NAME}'...")
playlist = sp.user_playlist_create(
    user=USER_ID, 
    name=PLAYLIST_NAME, 
    public=False, 
    description=f"Top 100 songs from {date} automatically created via Python."
)
print(f"🎉 Playlist created successfully! ID: {playlist['id']}")

# --- 5. ADD SONGS TO THE NEW PLAYLIST ---
if track_uris:
    print(f"\n📤 Adding tracks to your new playlist...")
    sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
    print("🚀 Tracks added successfully! Go check your Spotify app!")
else:
    print("No tracks were found to add.")