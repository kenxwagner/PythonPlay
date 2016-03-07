first_name = "Monty"
last_name = "Python"
full_name = first_name + " " + last_name
year = 1969
origin = "Presented originally in " + str(year)
sentence = "Back in " + str(year) + ", a legend was born.\n" + "We know it now as \n\t" + first_name + " " + last_name + "\n\t\t" + "What a show!"

print(full_name)
print (origin)
print (str(year))
print (sentence)


word1 = 'Good'
half1 = len(word1)//2
end1 = word1[half1:]

word2 = 'Evening'
half2 = len(word2)//2
end2 = word2[half2:]

print (word1 + word2)