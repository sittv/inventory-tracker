# SITTV Inventory Tracker
# Written by Eric S. Londres in 2018
# Mostly an adapted rewrite of Jesse Stevenson's shirt tracker

import os
import sys

# File should be in formt [ID Location Name] with spaces separating

file = open("inventory.txt", "r")
inventory = []
content = file.readlines()
content = [x.strip() for x in content]
file.close()

class equipment:
    def __init__(self, Identity, Location, Name):
        self.ID = Identity
        self.location = Location
        self.name = Name
    def __str__(self):
        return self.ID + " " + self.location + " " + self.name

for line in content:
    line = line.split()
    member = equipment(line[0], line[1], line[2])
    inventory.append(member)

def writeOut():
    file = open("inventory.txt", "w")
    newInventory = ""
    for thing in inventory:
        newInventory += thing.__str__() + '\n'
    file.truncate()
    file.write(newInventory)

def listAllItems():
    for thing in inventory:
        print(thing)
    
def listItem():
    method = input("List by ID, name, or location? ")
    if method != "ID" and method != "name" and method != "location":
        print("Please specify a list method.")
        raise SystemExit
    else:
        if method == "ID":
            ident = input("Enter ID: ")
            for thing in inventory:
                if thing.ID == ident:
                    print(thing)
                    raise SystemExit
            print("ID not found.")
        elif method == "name":
            thename = input("Enter name: ")
            for thing in inventory:
                if thing.name == thename:
                    print(thing)
                    raise SystemExit
            print("Name not found.")
        else: # method == location
            alocation = input("Location: ")
            for thing in inventory:
                if thing.location == alocation:
                    print(thing)
    writeOut()

def deleteItem():
    method = input("Delete ID or name? ")
    if method == "ID":
        ident = input("ID: ")
        for thing in inventory:
            if thing.ID == ident:
                print("Deleted!")
                inventory.remove(thing)
    elif method == "name":
        thename = input("Name: ")
        for thing in inventory:
            if thing.name == thename:
                print("Deleted!")
                inventory.remove(thing)
    else:
        print("Please choose a valid lookup method.")
    writeOut()
        

def useItem():
    method = input("Select item by ID or name?  ")
    if method == "ID":
        ident = input("ID: ")
        for i in range(len(inventory)):
            if inventory[i].ID == ident:
                inventory[i].location = "inuse"
    elif method == "name":
        thename = input("Name: ")
        for i in range(len(inventory)):
            if inventory[i].name == thename:
                inventory[i].location = "inuse"
    else:
        print("Please choose a valid lookup method.")
    writeOut()

def addItem():
    newEquipment = equipment(input("ID: "), input("Location: "), input("Name: "))
    for i in range(len(inventory)):
        if newEquipment.ID == inventory[i].ID:
            print("ID already exists.")
            print(inventory[i])
            raise SystemExit
        elif inventory[i].name == newEquipment.name:
            print("Name already exists.")
            print(inventory[i])
            raise SystemExit
    inventory.append(newEquipment)
    writeOut()
            

def setLocation(newLocation):
    method = input("Change location by name or ID?")
    if method == "ID":
        ident = input("Enter ID: ")
        for i in range(len(inventory)):
            if ident == inventory[i].ID:
                inventory[i].location = newLocation
                print("Location changed.")
    elif method == "name":
        thename = input("Enter name: ")
        for i in range(len(inventory)):
            if thename == inventory[i].name:
                inventory[i].location = newLocation
    writeOut()

def all():
    raise SystemExit

def retag():
    raise SystemExit

while(True):
    function = input("\n\nAvailable commands:\nlist\nlistall\nadd\ndelete\nuse\nset\nquit\n\n")
    if function == "list":
        listItem()
    elif function == "listall":
        listAllItems()
    elif function == "add":
        addItem()
    elif function == "delete":
        deleteItem()
    elif function == "use":
        useItem()
    elif function == "set":
        setLocation(input("Enter a new location: "))
    elif function == "quit":
        raise SystemExit
    else:
        print("Please enter a valid command.")
