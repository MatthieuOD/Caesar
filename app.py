message  = 'Phrase'
key = 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
spec_car = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~1234567890"
dictionaire = 'Dict'
split_dict = dictionaire.split()



def encode(message, key) :

    crypt_message = ''

    if key > 26 :
        key = key - len(alphabet)

    for i in message :
        
        crypted_index = 0

        if i in spec_car :
            crypt_message += i

        else :
            crypt_message += alphabet[alphabet.index(i) + key]

    return crypt_message

print(encode(message, 4))


def decode(crypted_message='fsrnsyv ge ze qsr kevw gsqqirx xy xi wirw') :
    
    words = crypted_message.split()
    keys_scores = []
    keys = dict()
    score = 0

    for i in range(27) :
        
        keys['key'] = i
        message = encode(crypted_message, -i)
        split_message = message.split()
        keys['message'] = message

        for i in split_message :
            for v in split_dict :
                if i == v :
                    score += 1

        keys['score'] = score
        keys_scores.append(keys)
        keys = dict()
        score = 0
    
    best_score = 0
        

    for i in keys_scores :

        if i['score'] > best_score :

            best_score = i['score']
            bskey = i['message']

    print(bskey)
    print(best_score)

        
    
        
  
    


        
decode()





