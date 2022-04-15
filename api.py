
import requests
class Giphy:
    def get_url(self, search_word):
        api = "UCf57i74uVQ9iOUiXX73F3RJVcmfk8tZ"
        gif = requests.get(url="https://api.giphy.com/v1/gifs/translate", params={"api_key": api, "s":search_word})
        gif_url = gif.json()["data"]["images"]["original"]["mp4"]
        return gif_url

    def get_joke(self):
        joke = requests.get(url="https://dad-jokes.p.rapidapi.com/random/joke",
                            headers={"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
                                     "X-RapidAPI-Key": "620bd1d7demsh48804bacb855cecp188b4ejsnfb123ef1a98d"})
        setup = joke.json()["body"][0]["setup"]
        punchline = joke.json()["body"][0]["punchline"]
        return (setup, punchline)


    def location(self):
        iss = requests.get(url="http://api.open-notify.org/iss-now.json").json()
        long = iss["iss_position"]["longitude"]
        lat = iss["iss_position"]["latitude"]
        return (lat, long)



