def encode(decoded):

    encoded = decoded.replace(' ', '_')

    return encoded

def decode(encoded):

    decoded = encoded.replace('_', ' ')

    return decoded

URL = 'test_av_en_url'

print(URL)
print(decode(URL))
