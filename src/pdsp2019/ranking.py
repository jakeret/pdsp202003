

def compute_instrument_ranks(instruments, ch_cl=False):
    rating = 0

    #check if swiss client
    if ch_cl:
        for instrument in instruments:
            if not instrument["ignore"]:
                if not instrument["expired"]:

                    instr_curr = instrument["currency"]

                    if instr_curr == 'USD':
                        rating += 7
                    elif instr_curr == 'EUR':
                        rating += 6
                    elif instr_curr == 'GBP':
                        rating += 5
                    else:
                        rating += 1
    else:
        rating = len(instruments) * 100

    return rating


def is_restricted(portfolio):
    result = (portfolio["mandator"] == "INTL" or portfolio["mandator"] == "EU") and portfolio[
        "currency"] != "CHF"

    # if not restricted then set the prechecked flag
    if result == False:
        portfolio["prechecked"] = True

    return result
