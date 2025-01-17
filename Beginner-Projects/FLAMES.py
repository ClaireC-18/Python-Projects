#FLAMES is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling. 
#This game does not accurately predict whether or not an individual is right for you, but it can be fun to play this with your friends.

#Take the two names.
name1 = input("Enter the first name: ").lower().replace(" ", "")
name2 = input("Enter the second name: ").lower().replace(" ", "")

# TODO:Remove the common characters with their respective common occurrences.
for letter in name1:
    if letter in name2:
        name1 = name1.replace(letter, '', 1)
        name2 = name2.replace(letter, '', 1)
# TODO:Get the count of the characters that are left .
sum = len(name1) + len(name2)
# TODO:Take FLAMES letters as [“F”, “L”, “A”, “M”, “E”, “S”]
FLAMES = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
# TODO:Start removing letter using the count we got.
index = 0
while len(FLAMES) > 1:
    index = (index + sum - 1) % len(FLAMES)
    FLAMES.pop(index)

# TODO:The letter which last the process is the result.
print(f"Relationship status: {FLAMES[0]}")