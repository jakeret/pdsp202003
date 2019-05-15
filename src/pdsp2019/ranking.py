RATING_NON_SWISS = 100
RATING_DEFAULT = 1
RATING_GDP = 5
CURRENCY_GDP = 'GBP'
RATING_EUR = 6
CURRENCY_EUR = 'EUR'
RATING_USD = 7
CURRENCY_USD = 'USD'


def compute_instrument_ranks(instruments, ch_cl=False):
    rating = 0

    #check if swiss client
    if ch_cl:
        for instrument in instruments:
            if not instrument["ignore"]:
                if not instrument["expired"]:

                    instr_curr = instrument["currency"]

                    if instr_curr == CURRENCY_USD:
                        rating += RATING_USD
                    elif instr_curr == CURRENCY_EUR:
                        rating += RATING_EUR
                    elif instr_curr == CURRENCY_GDP:
                        rating += RATING_GDP
                    else:
                        rating += RATING_DEFAULT
    else:
        rating = len(instruments) * RATING_NON_SWISS

    return rating


def is_restricted(portfolio):
    result = (portfolio["mandator"] == "INTL" or portfolio["mandator"] == "EU") and portfolio[
        "currency"] != "CHF"

    # if not restricted then set the prechecked flag
    if result == False:
        portfolio["prechecked"] = True

    return result
