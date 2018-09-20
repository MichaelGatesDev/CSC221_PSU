#!/usr/bin/env python3

# Michael Gates
# 19 September 2017
# Calculates reactor meltdown and cooldown times


print("== Running Meltdown Calculator ==")

# the starting temperature of the reactor
currentTemp = int(input("What is the current temperature? "))

# the percentage of increase per minute as a decimal (i.e. “0.04” for 4%)
increasePerMinute = float(input("What is the percentage rate of increase? "))

# the temperature at which the reactor will meltdown.
meltdownTemp = int(input("What is the point of meltdown? "))


minutes = 0
while(currentTemp < meltdownTemp):
    currentTemp = currentTemp * (1 + increasePerMinute)
    minutes += 1
    print("Minute: " + str(minutes)  + " The current temperature is " + str(int(currentTemp)))

print("After " + str(minutes) + " minutes, the reactor will melt down!")


# COOLDOWN 

print("== Running Cooldown Calculator ==")


# the starting temperature of the reactor
currentTemp = int(input("What is the current temperature? "))

# the percentage of decrease per minute as a decimal (i.e. “0.04” for 4%)
decreasePerMinute = float(input("What is the percentage rate of decrease? "))

# the temperature at which the reactor will meltdown.
safeTemp = int(input("What is the safe temperature? "))


minutes = 0
while(currentTemp > safeTemp):
    currentTemp = currentTemp / (1 + decreasePerMinute)
    minutes += 1
    print("Minute: " + str(minutes)  + " The current temperature is " + str(int(currentTemp)))

print("After " + str(minutes) + " minutes, the reactor will be cooled down!")
