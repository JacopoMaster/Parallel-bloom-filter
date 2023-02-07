import math
import hashlib
import random
import string
import time


def hash_calculate(string, n, j):
    sha256 = hashlib.sha256()
    # Aggiorna l'oggetto sha256 con la stringa e l'indice i
    sha256.update((string + str(j)).encode('utf-8'))
    return int(sha256.hexdigest(), 16) % n


class BloomFilter:



    def __init__(self, size, hash_count):
        # Crea un array di bit di dimensione size, inizialmente tutti impostati su zero
        self.bit_array = [0] * size
        self.size = size
        self.hash_count = hash_count


    def initialize(self, urls):
        # Itera per il numero di volte specificato nella proprietà hash_count
        for j in range(self.hash_count):
            # Utilizza la funzione hash_calculate per ogni url
            # e aggiorna il filtro
            for i in range(len(urls)):
                self.bit_array[hash_calculate(urls[i], self.size, j)] = 1


    def check(self, url):
        for i in range(self.hash_count):
            if self.bit_array[hash_calculate(url, self.size, i)] == 0:
                return False
        return True







# test di funzionamento


url_maligni = ["http://evilhackers.com", "http://phishing.ru", "http://virusdownload.net",
               "http://malware.cn", "http://trojanhorse.de", "http://spyware.jp", "http://keylogger.fr",
               "http://rootkit.uk", "http://zombienetwork.com", "http://botnet.io", "http://adware.biz",
               "http://ransomware.us", "http://backdoor.ca", "http://worm.cn", "http://ddos.ru", "http://spam.de",
               "http://scam.jp", "http://fakeupdate.fr", "http://exploit.uk", "http://hack.com", "http://stealer.io",
               "http://leak.biz", "http://cryptojacking.us", "http://clickfraud.ca"]

# i primi 7 sono url_maligni
url_test = ["http://evilhackers.com", "http://phishing.ru", "http://virusdownload.net",
            "http://malware.cn", "http://trojanhorse.de", "http://spyware.jp", "http://keylogger.fr",
            "http://starwars.com", "http://lotr.com", "http://harrypotter.com", "http://marvel.com",
            "http://dc.com", "http://disney.com", "http://pixar.com", "http://tolkien.com",
            "http://startrek.com", "http://stargate.com", "http://battlestar.com", "http://warhammer40k.com",
            "http://wow.com", "http://eveonline.com", "http://dnd.com", "http://pathfinder.com",
            "http://magic.com", "http://mtg.com", "http://pokemon.com", "http://yugioh.com", "http://worldofwarcraft.com",
            "http://diablo.com", "http://overwatch.com"]



bf = BloomFilter(1000, 10)

start_time = time.time()
bf.initialize(url_maligni)
end_time = time.time()
print("Tempo di esecuzione per l'inserimento degli URL maligni:", end_time - start_time)

start_time = time.time()
for url in url_test:
    if bf.check(url):
        print(url, "è un URL maligno")
end_time = time.time()
print("Tempo di esecuzione per la verifica degli URL:", end_time - start_time)



# test prestazioni
#
# def generate_random_word(length):
#     # Genera una stringa casuale di lettere minuscole di lunghezza length
#     return ''.join(random.choices(string.ascii_lowercase, k=length))
#
# element= 100000 #numero di elementi di prova
#
# testing=[]
# testing2=[]
#
# random.seed(30)
# for i in range (element):
#     testing.append(generate_random_word(10))
#
# for i in range (element):
#     testing2.append(generate_random_word(10))
#
#
#
# bf = BloomFilter(100000, 70)
#
# start_time = time.time()
# bf.initialize(testing)
# end_time = time.time()
# print("Tempo di esecuzione per l'inserimento degli URL maligni:", end_time - start_time)
#
# start_time = time.time()
# for i in testing2:
#      bf.check(i)
# end_time = time.time()
# print("Tempo di esecuzione per la verifica degli URL:", end_time - start_time)







