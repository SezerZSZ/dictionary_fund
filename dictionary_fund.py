my_dict = {}

# first we're going with this section -> the for loop to done the noting first...
data = input().split(" | ")

for item in data:
    extract = item.split(": ")
    word = extract[0]
    definition = extract[1]

    if word not in my_dict:
        my_dict[word] = [definition]
    else:  # if the word is in dict, simply adding the definition to it's list value...
        my_dict[word] += [definition]

# then we're continuing with the taking of the other input, the words to test
# and the commands to perform operations:
teacher_words = ''  # creating a helping variable to use below

command = input()

while True:

    if '|' in command:
        teacher_words += command  # taking the teacher's words to test...

    if command == "Test":
        extract = teacher_words.split(" | ")
        search_word = extract[0:]
        for text in search_word:
            if text in my_dict:
                print(f"{text}:")
                for key, value in my_dict.items():
                    if key == text:
                        for val in value:
                            print(f' -{val}')
        # after the for loop, operation performed, end the program
        break

    elif command == "Hand Over":
        for key, value in my_dict.items():
            print(key, end=" ")  # printing the keys in dict separated by space (" ")...
        # after the for loop, operation performed, end the program
        break

    command = input()
