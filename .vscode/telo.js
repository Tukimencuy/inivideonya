const axios = require('axios');

// Ganti dengan token akses yang sesungguhnya
const ACCESS_TOKEN = 'EAABwzLixnjYBABEneERatnpcxKV1w90J44XDCIb5rpcu2f9qZC21OQA999CDq8IPCZC55m1ZADedxgIOhLCIu6SdXvHXDSESzvli7mylFLBpIomECNZAC2oac69UrhozkhcxVZBNNX8AV4KfAzug7q6p2EJEwtG217wc3v7IdzYt4oMZBYjG49VoeKMFA4VqMZD';

// ID Postingan Facebook
const POST_ID = 'post_id';

// Komentar yang ingin Anda kirim
const COMMENT = 'Ini adalah komentar otomatis';

// Fungsi untuk mengirim komentar
const postComment = async (postId, comment) => {
  const url = `https://m.facebook.com/groups/loyalityavehount3/permalink/1410848536428986/?fs=1&focus_composer=0&m_entstream_source=feed_mobile&paipv=0&eav=AfbaepxUeeIuGt7OI-jaLMJLGIjBAY8AVpp79IXpKY3TnMisrWj7F2nG8ZBzgD_aRNU/${postId}/comments`;

  try {
    const response = await axios({
      method: 'post',
      url: url,
      params: {
        message: comment,
        access_token: ACCESS_TOKEN,
      },
    });

    console.log(`Komentar berhasil diposting: ${response.data.id}`);
  } catch (error) {
    console.error(`Error posting comment: ${error}`);
  }
};

// Panggil fungsi untuk mengirim komentar
postComment(POST_ID, COMMENT);
