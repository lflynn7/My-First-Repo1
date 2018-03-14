name = "Liam"

subjects = ["English","History","Science","Math" ]

print("my name is " + name)

#print(subjects)

for i in subjects:
    print("One of my classes is " +i)

characters = ["Dwight Shrute", "Jim Halpert", "Michael Scott"]

for i in  characters:
    print("One of the best characters in the Office is " + i)
        
for i in characters:
    if i == "Dwight Shrute":
        print (i + "beets")

tv_showes =[]

while True:
    print("What's one of your favorite movies? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        tv_showes.append(answer)


for i in tv_showes:
    print("one of your favorite movies is " + i)
