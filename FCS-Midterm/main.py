import json
import os

tabs = []
def displayMenu():
  print("Menu")
  print("1-Open Tab")
  print("2-Close Tab")
  print("3-Switch Tab")
  print("4-Display All Tabs")
  print("5-Open Nested Tabs")
  print("6-Clear All Tabs")
  print("7-Save Tabs")
  print("8-Import Tabs")
  print("9-Exit")

def openTab():
  #first of all we ask the user to input a tab title and a tab url
  #then we make a dictionary called tab that contains 3 key/value pairs that uses the input title and url
  #we make "nested tabs" and keep the list empty so we can fill it later in the nested tabs function
  #we also make a checker for the URL to be correctly provided
  #we append the tab to the global tabs list
  title = input("Please enter the title of the website:")
  url = input("Please enter the url of the website:")

  if url.startswith("http://") or url.startswith("https://"):
    tab = {"title": title, "url": url, "nested_tabs": []}
    tabs.append(tab)
    print("Tab " + title + " opened successfully")
  else:
    print("Invalid URL! Please insert a valid URL starting with http or https")



def closeTab():
  #defined a variable called index that takes the index input from the user
  #made an if statement for if the user didnt input an index to close the last tab in the list of tabs
  #made a variable called close_tab that uses the pop function to close the tab at the assigned index
  index = input("please choose the index of the tab you want to close:")
  if not index:
    close_tab = tabs.pop(len(tabs) - 1)
    print("the tab " + close_tab["title"] + " has been closed!")
  else:
    index = int(index)
    if 0 <= index < len(tabs):
      close_tab = tabs.pop(index)
      print("the tab " + close_tab["title"] + " has been closed!")
    else:
      print("No tab found at the index you provided!")

def switchTab():
  pass

def displayAllTabs():
  #looping through the tabs list and printing tab titles
  #then we loop through the nested tabs list that is within tabs list
  #added spaces for printing the nested titles to display it in a hierarchically manner
  if tabs:
    for tab in tabs:
      print(tab["title"])
      for nested in tab["nested_tabs"]:
        print("      " + nested["title"])
  else:
    print("There are no tabs open!")

def openNestedTabs():
  parent_index = int(input("Please enter the index of the parent tab: "))
  if 0 <= parent_index < len(tabs):
    title = input("Please enter the title of the tab: ")
    url = input("Please enter the url of the website:")

    if url.startswith("http://") or url.startswith("https://"):
      nested_tab = {"title": title, "url": url}
      tabs[parent_index]["nested_tabs"].append(nested_tab)
      print(title + "has been opened successfully in " + tabs[parent_index]["title"])
    else:
      print("Invalid URL! Please insert a valid URL starting with http or https")
  else:
    print("this parent tab doesnt exist!")

def clearAllTabs():
  global tabs
  tabs = []
  print("All Tabs Are Cleared!")

def saveTabs():
  #imported json and made the saveTabs function using the json.dump method
  #openned a file using the with open method and told it to write ("w") to the file
  #imported OS to fix the issue of duplicate names for the files by checking if that file path exists

  file_path = input("Please enter a file path: ")
  if os.path.exists(file_path):
    print("a file with the name you entered already exists!try a different name.")
  else:
    with open(file_path , "w") as file:
      json.dump(tabs , file)
    print("tabs saved to " + file_path)

def importTabs():
  file_path = input("Please enter a file path: ")
  try:
    with open(file_path , "r") as file:
      tabs = json.load(file)
    print(json.dumps(tabs , indent=2))
    print("tabs imported from " + file_path)
  except FileNotFoundError:
    print("File not found!")


def main():
    print("Welcome to my cutting-edge browser!")

    while True:
      displayMenu()

      choice = int(input("Please enter a choice from 1 to 9:"))

      if choice == 1:
        openTab()
      elif choice == 2:
        closeTab()
      elif choice == 3:
        switchTab()
      elif choice == 4:
        displayAllTabs()
      elif choice == 5:
        openNestedTabs()
      elif choice == 6:
        clearAllTabs()
      elif choice == 7:
        saveTabs()
      elif choice == 8:
        importTabs()
      elif choice == 9:
        print("Exiting the program.Goodbye!")
        break
      else:
        print("Invalid input.Please enter a number between 1 and 9")





main()