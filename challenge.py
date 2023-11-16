
#challenge

message=input('> ')

def text(message):

    words=message.split( " ")

    Emoji={
        ":)" : "smile",
        ":(" : "sad"

    }

    output=" "
    for word in words:
        output +=Emoji.get(word,word) +" "

    print(output) # return(output)


# message=input('> ') #or we can write here
print('message : ')
text(message)  #out_text=text(message)   # or we can use the green write instead
               #print(out_text)

