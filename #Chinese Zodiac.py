#Chinese Zodiac
#The Chinese zodiac assigns animals to years in a 12-year cycle. One 12-year cycle is shown in the table below. The pattern repeats from there, with 2012 being another year of the dragon, and 1999 being another year of the hare.

#Year Animal
#2000 Dragon
#2001 Snake
#2002 Horse
#2003 Sheep
#2004 Monkey
#2005 Rooster
#2006 Dog
#2007 Pig
#2008 Rat
#2009 Ox
#2010 Tiger
#2011 Hare

#Write a program that reads a year from the user and displays the animal associated with that year. Your program should work correctly for any year greater than or equal to zero, not just the ones listed in the table.
animals = ["Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"]
year = int(input("Please enter a year:"))


if (year-2000) % 12 == 0:
    print("Dragon")
elif (year-2000) % 12 == 1:
    print("Snake")
elif (year-2000) % 12 == 2:
    print("Horse")
elif (year-2000) % 12 == 3:
    print("Sheep")
elif (year-2000) % 12 == 4:
    print("Monkey")
elif (year-2000) % 12 == 5:
    print("Rooster")
elif (year-2000) % 12 == 6:
    print("Dog")
elif (year-2000) % 12 == 7:
    print("Pig")
elif (year-2000) % 12 == 8:
    print("Rat")
elif (year-2000) % 12 == 9:
    print("Ox")
elif (year-2000) % 12 == 10:
    print("Tiger")
elif (year-2000) % 12 == 11:
    print("Hare")



