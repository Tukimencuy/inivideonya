
import facebook


# Ganti dengan Access Token yang Anda dapatkan pada langkah 2
access_token = 'EAABwzLixnjYBABEneERatnpcxKV1w90J44XDCIb5rpcu2f9qZC21OQA999CDq8IPCZC55m1ZADedxgIOhLCIu6SdXvHXDSESzvli7mylFLBpIomECNZAC2oac69UrhozkhcxVZBNNX8AV4KfAzug7q6p2EJEwtG217wc3v7IdzYt4oMZBYjG49VoeKMFA4VqMZD'

# Ganti dengan ID postingan yang ingin Anda komentari
post_id = '1410848536428986'

# Ganti dengan teks promosi yang ingin Anda komentari
promo_text = 'Halo, kontol'

# Membuat instance Graph API
graph = facebook.GraphAPI(access_token)

# Mengecek apakah Access Token valid
user = graph.get_object('me')
if user:
    print("Access Token valid, pengguna:", user['name'])
else:
    print("Access Token tidak valid")
    exit(1)

# Mengomentari postingan dengan teks promosi
comment = graph.put_comment(object_id=post_id, message=promo_text)
if comment:
    print("Komentar promosi berhasil diposting, ID komentar:", comment['id'])
else:
    print("Gagal mengomentari postingan")
