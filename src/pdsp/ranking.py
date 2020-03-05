from enum import Enum


class CurrencyRating(Enum):
    USD = 7
    EUR = 6
    GDP = 5
    CHF = 1
    RATING_NON_SWISS = 100

def compute_instrument_ranks(instruments, ch_cl=False):
    rating = 0

    #check if swiss client
    if ch_cl:
        # iterate over all the instruments
        for instrument in instruments:

            # do not process insturments that should be ignored
            if not instrument["ignore"]:

                # skip all the expired instruments
                if not instrument["expired"]:

                    rating += CurrencyRating[instrument["currency"]].value

    else:
        rating = len(instruments) * CurrencyRating.RATING_NON_SWISS.value

    return rating


def is_restricted(portfolio):
    result = is_foreign_mandator(portfolio) and is_non_swiss_portfolio(portfolio)

    # if not restricted then set the prechecked flag
    if result == False:
        portfolio["prechecked"] = True

    return result


def is_non_swiss_portfolio(portfolio):
    return portfolio["currency"] != "CHF"


def is_foreign_mandator(portfolio):
    return (portfolio["mandator"] == "INTL" or portfolio["mandator"] == "EU")
