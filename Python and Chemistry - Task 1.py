"""     @author: Vedang Mahajan       """

# Oxygen, Carbon, Hydrogen and Chlorine

import sys

substances = ["Oxygen - O", "Carbon - C", "Hydrogen - H", "Chlorine - Cl"]

def printSubstances():
    print("----------------")
    
    for substance in substances:
        print(str(substances.index(substance) + 1) + " | " + substance)
        
    print("----------------")
    
printSubstances()

def removeElement(removeElement):
    substances.remove(removeElement)
    
    printSubstances()

substance_1 = input("Select the 1st element/molecule you want to combine from the above list (Type only the symbol): ").lower()

if substance_1 == "oxygen" or substance_1 == "o":
    removeElement("Oxygen - O")
    substance_2 = input("Select the 2nd element/molecule you want to combine from the above list (Type only the symbol): ").lower()
elif substance_1 == "c" or substance_1 == "carbon":
    removeElement("Carbon - C")
    substance_2 = input("Select the 2nd element/molecule you want to combine from the above list (Type only the symbol): ").lower()
elif substance_1 == "h" or substance_1 == "hydrogen":
    removeElement("Hydrogen - H")
    substance_2 = input("Select the 2nd element/molecule you want to combine from the above list (Type only the symbol): ").lower()
elif substance_1 == "chlorine" or substance_1 == "cl":
    removeElement("Chlorine - Cl")
    substance_2 = input("Select the 2nd element/molecule you want to combine from the above list (Type only the symbol): ").lower()
else:
    print(" ")
    print("Wrong Entry! Please try later")
    sys.exit()
    
if substance_2 == "o" or substance_2 == "c" or substance_2 == "cl" or substance_2 == "h":
    print("You have combined " + substance_1 + " and " + substance_2 + " and have obtained " + substance_1 + substance_2)
else:
    print(" ")
    print("Wrong Entry! Please try later")
