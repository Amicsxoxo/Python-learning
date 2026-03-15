sentence = "What is the Airspeed Velocity of an Unladen Swallow"

print(sentence.split())
result = {word:len(word) for word in sentence.split()}
# print(result)