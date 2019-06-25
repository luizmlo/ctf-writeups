from bs4 import BeautifulSoup
import hashlib
import requests
import clipboard

SESSION_COOKIES = {'PHPSESSID':'YOUR-COOKIES'}

def parse_key(COOKIES):
	source = requests.get('https://ringzer0ctf.com/challenges/13', cookies=COOKIES)
	soupSource = BeautifulSoup(source.text, 'html.parser')
	challengeClass = soupSource.find('div', class_='challenge-wrapper')
	keyClass = challengeClass.find('div', class_='message')

	classStr = str(keyClass)
	keyStart = classStr.find('BEGIN MESSAGE')
	keyEnd = classStr.find('END MESSAGE')
	key = classStr[(keyStart+28):(keyEnd-15)]
	return key


def hash_key(key):
	hashKey = hashlib.sha512()
	hashKey.update(key.encode('utf-8'))
	hashStr = str(hashKey.hexdigest())
	return hashStr


def retrieve_flag_source(hashedKey):
	url = 'https://ringzer0ctf.com/challenges/13/' + str(hashedKey)
	flagSource = requests.get(url, cookies=SESSION_COOKIES).text
	return flagSource
	

def parse_flag(flagSource):
	flagSoup = BeautifulSoup(flagSource, 'html.parser')
	flagTag = str(flagSoup.find('div', class_='alert alert-info'))
	flag = flagTag[(flagTag.find('FLAG')):flagTag.find('</div>')]
	return flag

def main():
	key = parse_key(SESSION_COOKIES)
	hashedKey = hash_key(key)
	flagSource = retrieve_flag_source(hashedKey)
	flag = parse_flag(flagSource)
	clipboard.copy(flag)
	print(flag)
	print('Flag copied to clipboard!\n')

main()



