from playsound import playsound

RED = '\033[31m'
GREEN = '\033[32m'
END = '\033[0m'

while (True):
    password = input("password==>")
    
    if password == "very sexy":
        break
    
    if password == "4545":
        print("")
        print(GREEN + " ___ _   _  ___ ___ ___  ___ ___ " + END)
        print(GREEN + "/ __| | | |/ __/ __/ _ \/ __/ __|" + END)
        print(GREEN + "\__ \ |_| | (_| (_|  __/\__ \__ \ " + END)
        print(GREEN + "|___/\__,_|\___\___\___||___/___/" + END)
        print("")
        
        #ここに正解した時のサウンドのディレクトリを置く(mp3 OR wav)
        
        playsound("key1.mp3")
    else:
        print("")
        print(RED + "  ___ _ __ _ __ ___  _ __ " + END)
        print(RED + " / _ \ '__| '__/ _ \| '__|" + END)
        print(RED + "|  __/ |  | | | (_) | |   " + END)
        print(RED + " \___|_|  |_|  \___/|_|   " + END)
        print("")
        
        #ここに不正解した時のサウンドのディレクトリを置く(mp3 OR wav)
        
        playsound("key2.mp3")
        
