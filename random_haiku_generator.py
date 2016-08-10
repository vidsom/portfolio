syllable5_list = ["If you ever feel down","If life gives you pie","You will be better","Your life is over","I want cookies please","Monica is blah","You are tall, I'm not","Grab life by the toes","Say something I can't","Microwaves are good"]
syllable7_list = ["Depression leads to sadness","Take some hand sanitizer","In the jungle, we are strong","Swing from vines made of candy","Scratch your hairy back with tea"]
import random
syllable5_length = len(syllable5_list)
syllable7_length = len(syllable7_list)
random_syllable5 = random.randint(0,syllable5_length - 1)
random_syllable7 = random.randint(0,syllable7_length - 1)
random_syllable5also = random.randint(0,syllable5_length - 1)
print("A beautiful haiku for you...")
print("\n")
print(syllable5_list[random_syllable5])
print(syllable7_list[random_syllable7])
print(syllable5_list[random_syllable5also])

input()