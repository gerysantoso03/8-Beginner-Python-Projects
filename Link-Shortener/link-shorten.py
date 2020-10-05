import pyshorteners

link = input('Please give your link : ')

# Make class object of Shortener
shortener = pyshorteners.Shortener()

# Shorten the input link
shorten_link = shortener.tinyurl.short(link)

print(shorten_link)