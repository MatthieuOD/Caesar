message  = 'bonjour ca va mon gars comment tu te sens'

key = 1

alphabet = 'abcdefghijklmnopqrstuvwxyz'

spec_car = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~1234567890"

dictionaire = "Few people would choose a prison as the location for /a special evening out. However, Italy has launched its first restaurant to be located in a real jail.  At the Ingalera Restaurant in Bollate prison, Milan, there are four prisoners working as waiters and five others cooking in the kitchen, headed by a professional chef and a maître. It is a ground-breaking project, which allows prisoners to be gradually included into society. The reataurant has had great reviews: everyone says the food is worth going to prison for."

split_dict = dictionaire.split()



def encode(message, key) :

    crypt_message = ''

    if key > 26 :
        key = key - len(alphabet)

    for i in message :

        if i in spec_car :
            crypt_message += i

        else :
            crypt_message += alphabet[alphabet.index(i) + key]

    return crypt_message



def decode(crypted_message='fsrnsyv ge ze qsr kevw gsqqirx xy xi wirw') :

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

        keys['score'] = (score / len(split_message)) * 100
        keys_scores.append(keys)
        keys = dict()
        score = 0
    
    best_score = 0
        
    for i in keys_scores :
        if i['score'] > best_score :
            best_score = i['score'] 
            bskey = i['message']

    print(bskey)
    print('Score : ' + str(round(best_score)) + '%' )

        
    
        
  
    


        
decode()

