#!/usr/bin/env python3

# Michael Gates
# 12 September 2017
# Calculates year of birth

name = input("What is your name? ")

raw_age = input("Hello, " + name + ". How old are you? ")
age = int(raw_age)

raw_had_birthday = input("Have you had a birthday yet this year? (y/n) ").lower()
had_birthday = raw_had_birthday == "y"

current_year = 2017
birth_year = current_year - age - (0 if had_birthday else 1)

print("You were born in " + str(birth_year))
