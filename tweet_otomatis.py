import tweepy
import time


# Kredensial API Anda
API_KEY = 'TE0bnBFNdiZ5mS9dfM4n14bId'
API_KEY_SECRET = '3HOIRqtEdZm4oMOo4tvtzAzru4d8vcJyUCJeVZuTLh79p0y5hM'
ACCESS_TOKEN = '1132657959412985856-rXOA6GMdEjCF5eByOXJ0wJxXpLr4Ac'
ACCESS_TOKEN_SECRET = 'Mn9ulZHPetJEDw6sPx4yw3DyVCn6YrMdbWD4xSxDBhy67'

# Autentikasi ke Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Buat objek API
api = tweepy.API(auth)

# Fungsi untuk mengirim tweet otomatis


def tweet_otomatis(text):
    try:
        api.update_status(text)
        print(f"Tweet berhasil: {text}")

    except tweepy.TweepyException as e:
        print(f"Gagal menge-tweet: {e}")


# Contoh penggunaan
if __name__ == '__main__':
    tweet_otomatis(
        "Halo, ini adalah tweet otomatis menggunakan Twitter API 1.1!")
