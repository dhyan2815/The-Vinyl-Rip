'''THE VINYL RIP MUSIC DOWNLOADER '''

import http.client
import json
import webbrowser  # To open the link in the default browser

# Function to display a formatted header
def display_header():
    print("SPOTIFY MUSIC DOWNLOADER".center(50))
    print("=" * 50)

# Display the header
display_header()

# Establish connection to the RapidAPI service
conn = http.client.HTTPSConnection("spotify-downloader9.p.rapidapi.com")

# Headers with your RapidAPI key
headers = {
    'x-rapidapi-key': "bd97d9112cmsh631ad95b2e92a96p1cee46jsnebd727207003",  
    # Replace with your actual API key
    'x-rapidapi-host': "spotify-downloader9.p.rapidapi.com"
}

# Input Spotify album URL
album_id = input("\nEnter the Spotify album URL: ").strip()

# Make the request to download the album
print("\nFetching download link, please wait...\n")
conn.request("GET", f"/downloadAlbum?albumId={album_id}", headers=headers)

# Get the response
res = conn.getresponse()
data = res.read()

# Decode the response (it will likely be in JSON format)
decoded_data = data.decode("utf-8")

# Pretty-print the API response
try:
    json_data = json.loads(decoded_data)
    print("-" * 50)
    print(json.dumps(json_data, indent=4))  # Pretty-print the JSON response
    print("-" * 50)
    
    # Check for data in the response
    if "data" in json_data and "songs" in json_data["data"]:
        print("\nSongs found in the album:\n")
        for song in json_data["data"]["songs"]:
            print(f"Title: {song['title']}")
            print(f"Artist: {song['artist']}")
            print(f"Download Link: {song.get('downloadLink', 'N/A')}")
            print("-" * 50)
    else:
        print("\nNo songs found in the response or invalid data format.")
except json.JSONDecodeError:
    print("\nFailed to parse response as JSON.")
    print("Ensure the API response is in the expected format.")

# Footer
print("\n" + "=" * 50)
print("Thank you for using Spotify Music Downloader!".center(50))
print("=" * 50)