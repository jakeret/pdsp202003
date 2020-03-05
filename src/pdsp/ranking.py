from enum import Enum


class CurrencyRating(Enum):
    USD = 7
    EUR = 6
    GDP = 5
    CHF = 1
    RATING_NON_SWISS = 100


def compute_instrument_rank_for_non_swiss_clients(instruments):
    rating = len(instruments) * CurrencyRating.RATING_NON_SWISS.value
    return rating


def compute_instrument_ranks_for_swiss_clients(instruments):
    rating = 0
    for instrument in instruments:
        rating += lookup_instrument_rating(instrument)
    return rating


def lookup_instrument_rating(instrument):
    if is_ignored(instrument) or is_expired(instrument):
        instrument_rating = 0
    else:
        instrument_rating = CurrencyRating[instrument["currency"]].value
    return instrument_rating


def is_ignored(instrument):
    return instrument["ignore"]


def is_expired(instrument):
    return instrument["expired"]


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
