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
  index = eval(input("please choose the index of the tab you want to close:"))
  if not index:
    index = -1
  if 0 <= index < len(tabs):
    close_tab = tabs.pop(index)
    print("the tab " + close_tab["title"] + " has been closed!")
  else:
    print("No tab found at the index you provided!")

def switchTab():
  pass

def displayAllTabs():
  pass

def openNestedTabs():
  pass

def clearAllTabs():
  pass

def saveTabs():
  pass

def importTabs():
  pass


def main():
    print("Welcome to my cutting-edge browser!")

    while True:
      displayMenu()

      choice = eval(input("Please enter a choice from 1 to 9:"))

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