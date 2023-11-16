
# Emoji tutor

message=input('> ')
words=message.split( " ")

print(words)


Emoji={
    ":)" : "smile",
    ":(" : "sad"

}

output=" "
for word in words:
    output +=Emoji.get(word,word) +" "
print(output)
