# -*- coding: utf-8 -*-
class Vigenere(object):
	key=''
	message=''
	code_message=''
	len_key=0
	b_text=[]
	out_message=''
	alph=' абвгдежзийклмнопрстуфхцчшщъыьэюя'
	alph_freq=' оеуаинтслрвкмдпуяыьзгбчйжхшюэщцфъ'


	def __init__(self):
		var=input("Что будем делать? c-кодировать, d-декодировать: ")
		if var=='c':
			self.input_message("исходное")
			self.encryption(sign=1,bd=0,type_message="Зашифрованное")
		elif var=='d':
			self.input_message("зашифрованное")
			self.decryption()


	def input_message(self,type_message):
		self.message=input('Введите '+type_message+' сообщение: ').lower()
		self.code_message=input('Введите кодовое слово: ').lower()

	def encryption(self,sign,bd,type_message):
		count=0
		for char in self.message:
			if char in self.alph:
				self.key=(self.alph.index(char)+sign*self.alph.index(self.code_message[count])+bd)%len(self.alph)
				self.out_message+=self.alph[self.key]
				count=(count+1)%len(self.code_message)
			else:
				self.out_message+=char
		print(type_message+ ' сообщение: '+ self.out_message,file=open('cryption.txt','w'))


	def decryption(self):
		self.encryption(sign=-1, bd=len(self.alph), type_message="Расшифрованное")

cipher=Vigenere()