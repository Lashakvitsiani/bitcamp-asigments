quote = input("What is the quote?") 
author = input("Who said it?")
print(f"{author} says, \"{quote}\"")

# BONUS:

quotes = {
  "bill gates" : "I use windows every day. I have at least 4 windows in my room.",
  "oto zakalashvili" : "Learning and fighting!",
  "Winston Churchill" : "If you are going through hell, keep going."

}

try:
    print(f"{author} says, \"{quotes[author]}\"")
except KeyError:
    pass
