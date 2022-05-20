from time import sleep
from PROJECT_FUNCTIONS import *
import os


modifications = [
    ["Standard", "Modified", "Detailing"],
        [0, 370.50, 1257.99  ]
                ]


features =  [
    ["Stereo", "Leather", "GPS" ],
        [30.50, 530.99, 301.90 ] 
            ]

mod_basket = []

mod_prices = []

feature_basket = []

feature_prices = []


def main():
    
    while True:
        try:
            basic_price = int(input("What is the price of this vehicle? "))
            if isinstance(basic_price, int):
                break
        except ValueError:
            print("Invalid input, Please enter a number!")
            continue
    print("                                                              ")
    while True:
        try:
            print("                                                              ")
            trade_in_allowance = int(input("What is the customers trade in allowance? ") or 0)
            if isinstance(trade_in_allowance, int):
                break
        except ValueError:
            print("Invalid input, please enter a number!")
            continue

    car_price(basic_price, trade_in_allowance)
           
    print("                                                              ")           
    input("We will now take you to the Modifications page... ")
    print("                                                              ")
    print("|------------------------------------------------------------|")
    print("  MODIFICATIONS                           |                   ")
    print("                                          |                   ")
    print("  0-Standard:-----------------------------|      £0           ")
    print("                                          |                   ")
    print("  1-Modified:-----------------------------|      £370.50      ")
    print("                                          |                   ")
    print("  2-Customized Detailing:-----------------|      £1257.99     ")
    print("|------------------------------------------------------------|")
    print("  ADDTIONAL OPTIONS                                           ")
    print("                                                              ")
    print("  3-Reset                                                     ")
    print("                                                              ")
    print("  4-Clear Screen                                              ")
    print("                                                              ")
    print("  5-Exit                                                      ")
    print("|------------------------------------------------------------|")
    print("                                                              ")
    print("Customer is subject to 6 percent sales tax")
    print("                                                              ")

    while True:
        try:
            choice = int(input("What Item would you like to add? "))
            if isinstance(choice, int):
                break
        except ValueError:
            print("Invalid input, please enter a number!")
            continue
                
    if choice == 3:
        main()

    if choice == 4:
        print("The screen will now be cleared in 3 seconds")
        print("\033[2J")
        main()

    if choice == 5:
        print("GoodBye!")
        quit()       
        
    menu1(choice, modifications, mod_basket)
    mod_price_add(choice, modifications, mod_prices)
    print(mod_basket)
    print(mod_prices)

    while True:   
        while True:
            answer_2 = str(input("Would you like to add additional features? y/n "))
            print("                                                              ")
            if answer_2 in ("y" "n"):
                break 
            print("Invalid input, please enter y/n!")

        if answer_2 == "y":
            print("                                                              ")
            print("We will now take you to the additional features page.")
            print("                                                              ")
            print("|--------------------------------------------------------------|")
            print(" FEATURES                                  |                  ")
            print("                                           |                  ")
            print(" 0-Stereo system:--------------------------|    £",features[1][0])
            print("                                           |                  ")
            print(" 1-leather Interior:-----------------------|    £",features[1][1])
            print("                                           |                  ")
            print(" 2-Global Positioning System (GPS):--------|    £",features[1][2])
            print("|--------------------------------------------------------------|")
            print(" ADDTIONAL OPTIONS                                            ")
            print("                                                              ")
            print(" 3-Change Prices                                              ")
            print("                                                              ")
            print(" 4-Reset                                                      ")
            print("                                                              ")
            print(" 5-Clear Screen                                               ")
            print("                                                              ")
            print(" 6-Exit                                                       ")
            print("|--------------------------------------------------------------|")   
            print("                                                              ")   
            print("                                                              ")                    
            print("Customer is subject to 6 percent sales tax")
            
            while True:
                try:
                    choice_2 = int(input("What item would you like to add? "))
                    if isinstance(choice_2, int):
                        break
                except ValueError:
                    print("Invalid input, please enter a number!")

            if choice_2 == 3: 
                print("|--------------------------------------------------------------|")
                print(" FEATURES                                  |                  ")
                print("                                           |                  ")
                print(" 0-Stereo system:--------------------------|    £",features[1][0])
                print("                                           |                  ")
                print(" 1-leather Interior:-----------------------|    £",features[1][1])
                print("                                           |                  ")
                print(" 2-Global Positioning System (GPS):--------|    £",features[1][2])
                print("|--------------------------------------------------------------|")
                print("                                                                ")
                change = input("What item would you like to change? ")
                print("                                                                ")
                if change.isdigit():
                    change_2 = int(input("What is the new price? £"))
                    features[1][int(change)] = change_2
                    print("The price has been updated.")
                    continue
            
            if choice_2 == 4:
                main()
            
            if choice_2 == 5:
                print("The screen will be cleared in 3 seconds!")
                sleep(3)
                os.system('cls')
                main()
            
            if choice_2 == 6:
                print("Goodbye!")
                quit()

            menu2(choice_2, features, feature_basket)
            feature_price_add(choice_2, features, feature_prices)
            print (feature_basket)
            print(feature_prices)
            continue
            
        else: 
            answer_2 == "n"      
            sumofprices = int(sum(mod_prices) + sum(feature_prices))
            total = int(sumofprices + car_price(basic_price, trade_in_allowance) * 1.06)
            print("                                                              ")
            print("Current order(including 6% sales tax): £", total)
            print("                                                              ")
            print("TOTAL : ", total)

            while True:
                print("                                                              ")
                choice_3 = input("Would you like to make a new order? (y/n): ")
                if choice_3 in ['y', 'n']:
                    break
                print("                                                              ")
                print("Invalid input, please enter y/n!")

            if choice_3 == "y":
                os.system('cls')
                main()
            else:
                choice_3 == "n"
                print("                                                              ")
                print("Goodbye!")
                exit()
main()