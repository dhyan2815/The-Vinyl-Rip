'''THE VINYL RIP MUSIC DOWNLOADER ''' '''THE VINYL RIP MUSIC DOWNLOADER ''''''THE VINYL RIP MUSIC DOWNLOADER '''

import http.client
import json
import webbrowser  # To open the link in the default browser

# Establish connection to the RapidAPI service
conn = http.client.HTTPSConnection("spotify-downloader9.p.rapidapi.com")

# Headers with your RapidAPI key
headers = {
    'x-rapidapi-key': "bd97d9112cmsh631ad95b2e92a96p1cee46jsnebd727207003",  
    # Replace with your actual API key
    'x-rapidapi-host': "spotify-downloader9.p.rapidapi.com"
}

# Spotify album URL encoded (replace with any valid album URL)
album_id = "https://open.spotify.com/album/3RZxrS2dDZlbsYtMRM89v8?si=mGmzIBQwTA-l3KzUr9cuoQ"

# Make the request to download the album
conn.request("GET", f"/downloadAlbum?albumId={album_id}", headers=headers)

# Get the response
res = conn.getresponse()
data = res.read()

# Decode the response (it will likely be in JSON format)
decoded_data = data.decode("utf-8")

# Print the full API response to inspect it
print("API Response:", decoded_data)  

# Parse the response as JSON
try:
    json_data = json.loads(decoded_data)
    
    # Check if the response contains a download link
    if 'download_link' in json_data:
        download_link = json_data['download_link']
        print(f"Download link: {download_link}")
        
        # Open the download link in the default web browser
        webbrowser.open(download_link)
        
        print("The download should start automatically in your browser.")
    else:
        print("Done hai bhaii")
except json.JSONDecodeError:
    print("Failed to parse response as JSON.")

'''THE VINYL RIP MUSIC DOWNLOADER ''''''THE VINYL RIP MUSIC DOWNLOADER ''''''THE VINYL RIP MUSIC DOWNLOADER '''