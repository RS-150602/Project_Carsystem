# CAR PRICE


def car_price(basic_price, trade_in_allowance):
    final_price = basic_price - trade_in_allowance
    print("                                         ")
    print("Your final price is: £" + str(final_price))
    return final_price


# FIRST MENU FUNCTIONS


def menu1(index, modifications, mod_basket):
    update = modifications[0][int(index)]
    mod_basket.append(update)
    return update

def mod_price_add(index, modifications, mod_prices):
    prices = modifications[1][int(index)]
    mod_prices.append(prices)
    return prices


# SECOND MENU FUNCTIONS


def menu2(index, features, feature_basket):
    change = features[0][int(index)]
    feature_basket.append(change)
    return change 



def feature_price_add(index, features, feature_prices):
    fet_price = features[1][int(index)]
    feature_prices.append(fet_price)
    return fet_price





    

