#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


list_of_names = []


with open("./input/names/invited_names.txt" , "r") as name:
    list_of_names += name.readlines()
    
for names_ in range(len(list_of_names)):
    list_of_names[names_] = list_of_names[names_].split("\n")
    list_of_names[names_] = (list_of_names[names_])[0]

    

print(list_of_names)
