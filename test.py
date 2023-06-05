import tweepy
import time

# Gantilah dengan kredensial API Twitter Anda
API_KEY = 'VP7MFUujfw77j9EaN08fgOtTV'
API_KEY_SECRET = 'e0938S6m5tNBi2v7IqwCKUu9nrtGgt8VyaDudzhG9cTrSdqwKU'
ACCESS_TOKEN = '1132657959412985856-omaYUXVM3WvtuMJQiX6tHk7EkAAlSo'
ACCESS_TOKEN_SECRET = 'ycQciFu8iEP7UbNAP6F1pBWhg26Uz67ye0FWWwmKuc7fn'


# Fungsi untuk mengautentikasi dan mengembalikan objek API
def authenticate():
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api



# Fungsi untuk mencari dan mengomentari tweet
def search_and_comment(api, keyword, comment_text):
    tweets = api.search_tweets(q=keyword, count=10)  # Anda dapat mengubah jumlah tweet yang ingin dicari
    for tweet in tweets:
        try:
            api.update_status(status=comment_text, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
            print(f"Berhasil mengomentari tweet dengan ID: {tweet.id}")
        except tweepy.TweepError as e:
            print(f"Gagal mengomentari tweet dengan ID: {tweet.id}. Alasan: {e.reason}")

api = authenticate()
keyword = "indonesia"  # Ganti dengan kata kunci yang ingin Anda cari
comment_text = "Hai! Guyss cek https://t.co/rlXlkMo4uS"  #Ganti dengan teks komentar promosi Anda
search_and_comment(api, keyword, comment_text)



# # Autentikasi Twitter API
# auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# Kata kunci pencarian dan pesan promosi
# search_keyword = 'vcs'
# promo_message = 'Hai! Guyss cek https://t.co/rlXlkMo4uS'

# def main():
#     while True:
#         try:
#             # Mencari tweet berdasarkan kata kunci
#             tweets = api.search_tweets(q=search_keyword, lang='id', result_type='recent', count=10)
#             for tweet in tweets:
#                 # Menanggapi tweet dengan pesan promosi
#                 reply_to = f'@{tweet.user.screen_name}'
#                 api.update_status(status=f'{reply_to} {promo_message}', in_reply_to_status_id=tweet.id)
#                 print(f'Replied to tweet by {reply_to}')
#                 time.sleep(60)  # Waktu jeda antara komentar (dalam detik)
#         except Exception as e:
#             print(f'Error: {e}')
#             time.sleep(60)

# if __name__ == '__main__':
#     main()
