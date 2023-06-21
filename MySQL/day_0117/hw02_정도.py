import random

a=[]
card_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_suit = ["♠", "♥", "♣", "◆"]

# 초기카드 생성
for i in card_number:
    for j in card_suit:
        a.append((i,j))


print(f'----------------------------------------------------------------')
for o in range(1, len(a)+1):
    print(a[o-1], end='\n' if o%13==0 else '')
        
print(f'----------------------------------------------------------------')



# 셔플 카드
random.shuffle(a)
player_1=[]
player_2=[]

for p in range(1, len(a)+1):        #p가 1, 셔플a+1 번째까지 돌아가면서
    print(a[p-1], end='\n' if p%13==0 else '')      #하나씩 프린트해줘라, a[p-1]번을!, 근데 만약 p가 13으로 나눌때의 몫이 0이 될때 줄바꿈 해주고 아니면 그냥 옆으로 띄워쓰면서 출력해줘라.



# 딜링 카드
for m in range(6):
    if m%2 == 0:
        player_1.append(a.pop())
    else:
        player_2.append(a.pop())
print(f'player1 : {player_1}')
print(f'player2 : {player_2}')


# 점수 부여
score1=0
score2=0

for n in range(len(player_1)):
    if player_1[n-1][1] == "♠":
        p1=3
    elif player_1[n-1][1] == "♥":
        p1=1
    elif player_1[n-1][1] == "♣":
        p1=4
    elif player_1[n-1][1] == "◆":
        p1=2
    score1+= player_1[n-1][0]*p1



for n in range(len(player_2)):
    if player_1[n-1][1] == "♠":
        p2=3
    elif player_1[n-1][1] == "♥":
        p2=1
    elif player_1[n-1][1] == "♣":
        p2=4
    elif player_1[n-1][1] == "◆":
        p2=2
    score2+=player_2[n-1][0]*p2

# 결과
print(f'player1 : {score1}, player2 : {score2}')

if score1 > score2:
    print(f'player1 win')
else:
    print(f'player2 win')



