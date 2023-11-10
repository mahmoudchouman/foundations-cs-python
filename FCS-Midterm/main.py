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
  title = input("Please enter the title of the website:")
  url = input("Please enter the url of the website:")

  tab = {"title": title, "url": url, "nested_tabs": []}

  tabs.append(tab)
  print("Tab " + title + " opened successfully")

def closeTab():
  pass

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