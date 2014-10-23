def encode(decoded):

    decoded.replace(' ', '_')

    return decoded

def decode(encoded):

    encoded.replace('_', ' ')

    return encoded
