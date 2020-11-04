import socket

def checkWinner(server,client):
    if server=='S' and client =='P':
        return True 

    elif server=='P' and client == 'R':
        return True 

    elif server == 'R' and  client =='S':
        return True

    elif client =='S' and server=='P':
        return False 

    elif client == 'P' and server == 'R':
        return False 

    elif client == 'R' and server == 'S':
        return False

def serverside():
    sockS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sockS.bind(('127.0.0.1', 60003))
    sockS.listen(1)

    PlayerSPoints = 0
    PlayerCPoints = 0
    while True: 
        print('Listening...')
        (sockC, addr) = sockS.accept()
        print('Connection From {}'.format(addr))
        while True: 
            print('{}-{}'.format(PlayerSPoints, PlayerCPoints))
            answerS = input('Choose R OR S OR P: ')
            while answerS not in {"R", "S", "P"}:
                answerS = input('Choose R OR S OR P:')
            data =  sockC.recv(1024)
            answerC = data.decode('ascii')
            sockC.sendall(bytearray(answerS, 'ascii'))

            print("You played {} and the client played {}".format(answerS, answerC))
            if checkWinner(answerS, answerC) == True:
                PlayerSPoints +=1
            elif checkWinner(answerS, answerC) == False:
                PlayerCPoints +=1
            if PlayerSPoints == 10: 
                print("You Won")
                break
            if PlayerCPoints == 10:
                print("Player Won")
                break
                
        sockC.close()
        print('client {} disconnect'.format(addr))

def clientside(host):
    sockC = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sockC.connect((host, 60003))
    PlayerSPoints = 0
    PlayerCPoints = 0
    while True: 
        print('{}-{}'.format(PlayerSPoints, PlayerCPoints))
        answerC = input('Choose R OR S OR P: ')
        while answerC not in {"R", "S", "P"}:
            answerC = input('Choose R OR S OR P: ')
        sockC.sendall(bytearray(answerC, 'ascii'))
        answerS = sockC.recv(1024)
        answerS = answerS.decode('ascii')

        print("You played {} and the server Side played {}".format(answerC, answerS))
        if checkWinner(answerS, answerC) == True:
            PlayerSPoints +=1
        elif checkWinner(answerS, answerC) == False:
            PlayerCPoints +=1
        if PlayerSPoints == 10: 
            print("Server Side Won")
            break
        if PlayerCPoints == 10:
            print("Client Won ")
            break
    sockC.close()


print('Welcome To The Game :D')
answer = input("Do you want to be the Server (S) or the Client (C):")
answer = answer.upper()
while answer not in {"S", "C"}:
    ans = input("Do you want to be the Server (S) or Client (C):")
    ans = ans.upper()

if answer == "S": 
    serverside()
elif answer == "C":
    host = input("Enter The Server IP:")
    clientside(host)
