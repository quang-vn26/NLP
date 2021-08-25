from bs4 import BeautifulSoup
from pprint import pprint
import requests

import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize

from textblob import TextBlob
from collections import Counter

from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

# b1: chon 1 bai viet tieng anh
url1 = "https://e.vnexpress.net/news/travel/stranded-in-vietnam-foreign-tourists-find-silver-lining-4339108.html"
# url2= "https://e.vnexpress.net/news/news/military-to-oversee-food-provision-in-hcmc-during-lockdown-pm-4343801.html"

def lay_noi_dung(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content,'html.parser')
	# print(soup.title)
	post_detail = soup.find('span',class_="lead_post_detail row")

	all_text = soup.find_all('p',{'class':'Normal'})
	doan_van = ""
	doan_van+=post_detail.get_text().strip()	
	for i in all_text:
		doan_van += i.get_text()
	# Lowercasting
	doan_van=doan_van.lower()
	doan_van.encode('utf-8')

	doan_van = xoa_ki_tu_phan_cach(doan_van)
	# print(doan_van)

	return doan_van

def xoa_stop_word(chuoi):
	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(chuoi)
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	# print(word_tokens)
	# print(filtered_sentence)
	# print("rut gon:"+str(len(filtered_sentence))+"|nguyen goc: "+str(len(word_tokens)))

	return filtered_sentence

def xoa_ki_tu_phan_cach(chuoi):
	ki_tu_rut_gon = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	for ki_tu in chuoi:
		if ki_tu in ki_tu_rut_gon:
			chuoi = chuoi.replace(ki_tu,"")
	return chuoi

def nhan_dien_ngon_ngu(chuoi):
	ngon_ngu = TextBlob(chuoi[:30])
	ngon_ngu =ngon_ngu.detect_language()
	return ngon_ngu
def dem_so_lan_cua_1_tu(chuoi):
	my_dict={}
	for tu in chuoi:
		try:
			my_dict[tu]+=1
		except:
			my_dict[tu]=1			
	return my_dict

def dem_so_chu_trong_1_tu(chuoi):
	my_dict={}
	for tu in chuoi:
		my_dict[tu] = len(str(tu))
	return my_dict	
def Stemming(chuoi):
	stemmer = PorterStemmer()
	my_array = []
	for i in chuoi:
		my_array.append(stemmer.stem(i))
	return my_array		
def Lemmatization(chuoi):
	wordnet_lemmatizer = WordNetLemmatizer()
	my_array = []
	# print("{0:20}{1:20}".format("Word","Lemma"))
	for i in chuoi:
		tmp = wordnet_lemmatizer.lemmatize(i)
		my_array.append(tmp)
		# print ("{0:20}{1:20}".format(i,tmp))
	return my_array
def so_sanh_stemming_lemma(chuoi,ky_thuat_stemming,ky_thuat_lemma):
	print("{0:20}{1:20}{2:20}".format("Word","Stemming","Lemmatization"))
	for i in range(0,len(chuoi)):
		print("{0:20}{1:20}{2:20}".format(chuoi[i],ky_thuat_stemming[i],ky_thuat_lemma[i]))
def luu_file(chuoi):
	f = open('mytext.txt', "w") #a: append; w: write		
	f.write(chuoi)
	f.close()
def tach_cau():
	response = requests.get(url1)
	soup = BeautifulSoup(response.content,'html.parser')
	soup.encode('utf-8')
	# print(soup.title)
	post_detail = soup.find('span',class_="lead_post_detail row")

	all_text = soup.find_all('p',{'class':'Normal'})
	doan_van = ""
	doan_van+=post_detail.get_text().strip()	
	for i in all_text:
		doan_van += i.get_text().strip()
	doan_van = doan_van.replace(".",". ")
	# Lowercasting
	# doan_van=doan_van.lower()
	# doan_van.encode('utf-8')

	my_array = nltk.tokenize.sent_tokenize(doan_van)
	return my_array	

doan_van = lay_noi_dung(url1)
doan_van2 = xoa_ki_tu_phan_cach(doan_van)
doan_van3 = xoa_stop_word(doan_van2)
ngon_ngu = nhan_dien_ngon_ngu(doan_van)
dem_so_tu = dem_so_lan_cua_1_tu(doan_van3)
dem_do_dai_cua_1_tu = dem_so_chu_trong_1_tu(doan_van3)
ky_thuat_stemming = Stemming(doan_van3)
ky_thuat_lemma = Lemmatization(doan_van3)
tach_cau_array = tach_cau()

# print(doan_van3)
# print("Ngon Ngu:"+ngon_ngu)
# print(dem_so_tu)
# print(dem_do_dai_cua_1_tu)
# print(ky_thuat_stemming)
# print(ky_thuat_lemma)
# so_sanh_stemming_lemma(doan_van3,ky_thuat_stemming,ky_thuat_lemma)
# luu_file(doan_van)
print(tach_cau_array)





	




