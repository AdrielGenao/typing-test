import time

input("Press Enter to start the timer. Type text as it is one whole line; do not press enter to make a new line. Press Enter when you finish the text.\n\nToday, historians relate that, as a general rule,\nbuying and selling securities was very much unorganized\nbefore the year 1792. Every person who owned a security\nfaced the problem of finding interested buyers who\nmight consider the purchase of a debt-free investment.\nThis meant most people were somewhat slow in investing\nin stocks and bonds because these securities could not\nreadily be converted into money. We have been told that\nan interesting number of traders and merchants agreed\nto try to do something to help correct the situation.\n")
start = time.time()
user = input()
end = time.time()
total = end - start
test = "Today, historians relate that, as a general rule, buying and selling securities was very much unorganized before the year 1792. Every person who owned a security faced the problem of finding interested buyers who might consider the purchase of a debt-free investment. This meant most people were somewhat slow in investing in stocks and bonds because these securities could not readily be converted into money. We have been told that an interesting number of traders and merchants agreed to try to do something to help correct the situation."
test = list(test)
user = list(user)
accuracy = 0
if len(user)<len(test):
    print("Error - Did not type full paragraph. You most likely had a missed space or misplaced character.")
else:    
    for i in range(len(test)):
        if test[i] == user[i]:
            accuracy+=1
    percent = float((accuracy/len(test))*100)
    speed = int(((accuracy/5)/total)*60)
    print("Your accuracy was %"+"{:.2f}".format(percent)+", and your speed was "+str(speed)+ " words/minute!")
