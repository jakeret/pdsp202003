from enum import Enum


class CurrencyRating(Enum):
    OTHER = 1
    USD = 7
    EUR = 6
    GDP = 5
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
                    rating += get_rating_for(instrument["currency"])

    else:
        rating = len(instruments) * CurrencyRating.RATING_NON_SWISS.value

    return rating


def get_rating_for(instrument_currency):
    try:
        return CurrencyRating[instrument_currency].value
    except KeyError:
        return CurrencyRating.OTHER.value


def is_restricted(portfolio):
    result = (portfolio["mandator"] == "INTL" or portfolio["mandator"] == "EU") and portfolio[
        "currency"] != "CHF"

    # if not restricted then set the prechecked flag
    if result == False:
        portfolio["prechecked"] = True

    return result
