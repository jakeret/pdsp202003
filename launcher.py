from pdsp2019.ranking import *
# Portfolio and Instrument risk assessment package

### Use the portfolio and instrument ranking package to verify if the customer is eligible for new investments

#### Get the portfolios and instruments to check

intl_pf = {
    "mandator": "INTL",
    "currency": "USD"
}

eu_pf = {
    "mandator": "INTL",
    "currency": "USD"
}

eu_pf_with_chf = {
    "mandator": "EU",
    "currency": "CHF"
}

ch_pf = {
    "mandator": "CH",
    "currency": "USD"
}


#### Check if the portfolios are restricted by regulatory definition
print("International mandator portfolio restricted:", is_restricted(intl_pf))
print("European mandator portfolio restricted:", is_restricted(eu_pf))
print("European mandator portfolio with swiss currency restricted:", is_restricted(eu_pf_with_chf))
print("Swiss mandator portfolio restricted:", is_restricted(ch_pf))

#### Use the portfolios that are now prechecked and not restricted to test for their instruments
print("European mandator portfolio with swiss currency:", eu_pf_with_chf)
print("Swiss mandator portfolio:", ch_pf)

eu_pf_with_chf_instr = [
    {"currency": "CHF", "ignore":False, "expired":False},
    {"currency": "EUR", "ignore":True, "expired":False},
]

ch_pf_instr = [
    {"currency": "CHF", "ignore":False, "expired":False},
    {"currency": "EUR", "ignore":False, "expired":False},
]

#### Instrument ranking for non swiss client
ranking = compute_instrument_ranks(eu_pf_with_chf_instr, ch_cl=False)
print("Ranking of EU portfolio is", ranking, "and to high for new investments")

#### Instrument ranking for swiss client
ranking = compute_instrument_ranks(ch_pf_instr, ch_cl=True)
print("Ranking of CH portfolio is", ranking, "and eligible for new investments")