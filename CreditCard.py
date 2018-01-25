#  File: CreditCard.py

#  Description: Input a credit card number and determine if it is valid and the brand

#  Name: Arturo Reyes Munoz

#  Date Created: 04/07

#  Date Last Modified: 04/07

def valid(card):

	if len(card)==16:

		oddprod=[card[0]*2]
		s=0

		for i in range(1,len(card)):

			if i%2==0:

				oddprod.append(card[i]*2)

				for i in range(len(oddprod)):

					if oddprod[i]>9:

						oddprod[i]=(oddprod[i]%10)+1

			elif i%2!=0:

				s+=card[i]

		if (sum(oddprod)+s)%10==0:

			return True

		else:

			return False

	elif len(card)==15:

		s = card[0]

		oddprod = []

		for i in range(1,len(card)):

			if i%2!=0:

				oddprod.append(card[i]*2)

				for i in range(len(oddprod)):

					if oddprod[i]>9:

						oddprod[i]=(oddprod[i]%10)+1

			elif i%2==0:

				s+=card[i]

		if (sum(oddprod)+s)%10==0:

			return True

		else:

			return False

def cardbrand(cardlist):

	num=0

	for i in range(4):

		num=(num*10)+cardlist[i]

	if num//100==34 or num//100==37:

		return 'American Express'

	elif num==6011 or (num//10==644) or (num//100==65):

		return'Discover'

	elif num//100==50 or num//100==55:

		return 'Mastercard'

	elif num//1000==4:

		return 'Visa'
	
	else:
		
		return 'none'

def main():

	cardnum=eval(input('Enter 15 or 16-digit credit card number: '))

	cardlist=[]
	cardtype=''

	while cardnum>9:

		cardlist.append(cardnum%10)
		cardnum=cardnum//10

	cardlist.append(cardnum)
	cardlist.reverse()


	if len(cardlist)!=15 and len(cardlist)!=16:

		print('Not a 15 or 16-digit number')
		return

	else:

		if valid(cardlist):

			cardtype=cardbrand(cardlist)

			if cardtype == 'none':

				print('Valid credit card number')

			else:

				print('Valid '+cardtype+' credit card number')

		else:

			print('Invalid credit card number')

main()




		






















