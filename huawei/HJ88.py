
cards=input().split('-')
card1,card2=cards[0].split(' '),cards[1].split(' ')
while True:
    if card1==['joker','JOKER'] or card2==['joker','JOKER']:
        print('joker JOKER')
        break
    if len(card1)==4 and len(card2)!=4:
        print(' '.join(card1))
        break
    if len(card2)==4 and len(card1)!=4:
        print(' '.join(card2))
        break
    if len(card1)!=len(card2):
        print('ERROR')
        break
    order='3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER'
    print(' '.join(card1) if order.find(card1[0])>order.find(card2[0]) else ' '.join(card2))
    break
