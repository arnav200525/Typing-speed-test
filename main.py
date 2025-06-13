import random
from datetime import datetime
import time

sentences = [
    "Hello, this is me testing my typing speed using python program developed by arnav deore. The goal is to test my typing speed accurately and correctly",
    "Python is widely regarded as one of the most beginner-friendly programming languages, making it a perfect starting point for aspiring software developers around the world.",
    "Typing speed and accuracy are skills that can significantly improve over time with consistent practice, patience, and a strong focus on proper technique.",
    "Software development life cycle (SDLC) is a structured process that is used to design, develop, and test good-quality software",
    "The main and important goal of the softaware development life cycle model is to deliver high-quality, maintainable software that meets the user's requirements.",
    "Round Robin is a cpu scheduling algorithm where each process is cyclically assigned a fixed time slot, it is the preemptive version of the First come First Serve cpu Scheduling algorithm.",
    "A trigger is a stored procedure in a database that automatically invokes whenever a special event in the database occurs and every trigger has a table attached to it.",
]

random.shuffle(sentences)

print("!!..TYPING SPEED TESTOR..!!")
print()
print("Note: Cases, commas, fullstops are also counted")
 
print("********Sentence********")
print()
print(sentences[0])
print()
print("************************")

i = 5

while i >= 1:
    print(i)
    i -= 1
    time.sleep(1.2)

start = time.time()
user_sentence = input("Start typing Now: \n").split(" ")
end = time.time()
total_required_time = end - start

sentence = sentences[0].split(" ")

correct = 0
orignal = []
mistakes = []

for i in range(0, len(sentence)):
    try:
        if user_sentence[i] == sentence[i]:
            correct += 1
        else:
            orignal.append(sentence[i])
            mistakes.append(user_sentence[i])
    except IndexError:
        print("You entered extra or less amount of total words")
    except Exception as e:
        print("Unexpected error occured", e)

wpm = (len(sentence) / total_required_time) * 60  # wpm = words per miniute

print("Results!")
print()
print(f"Total Time Taken: {total_required_time} sec")
print(f"Correctly Typed words: {correct} out of {len(sentence)}")
print(f"Words per miniute: {wpm}")
print()
print("Mistakes:")

for i in range(0, len(orignal)):
    print(f"{orignal[i]} - {mistakes[i]}")

# print(datetime.now().date())

with open("Typing Speed history.txt", "a") as f:
    f.write(f"\nDate : {datetime.now().date()}")
    # f.write(f"\nSentence : {sentence}")
    f.write("\n")
    for word in sentence:
        f.write(word + " ")
    f.write(f"\nTotal Time Taken: {total_required_time} sec")
    f.write(f"\nCorrectly Typed words: {correct} out of {len(sentence)}")
    f.write(f"\nWords per miniute: {wpm}")
    f.write(f"\n\nMistakes:\n")
    for i in range(0, len(orignal)):
        f.write(f"{orignal[i]} - {mistakes[i]}\n")
    f.write("\n\n")