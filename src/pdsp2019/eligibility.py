from pdsp2019.ranking import *


def verify_eligibility():
    #### Get the portfolios and instruments to check
    ch_pf, eu_pf, eu_pf_with_chf, intl_pf = load_instruments()

    #### Check if the portfolios are restricted by regulatory definition
    verify_regulatory_definition(ch_pf, eu_pf, eu_pf_with_chf, intl_pf)

    #### Use the portfolios that are now prechecked and not restricted to test for their instruments
    print("European mandator portfolio with swiss currency:", eu_pf_with_chf)
    print("Swiss mandator portfolio:", ch_pf)

    #### Instrument ranking for non swiss client
    eu_pf_with_chf_instr = load_eu_portfolio_instruments()
    verify_eu_portfolio_instruments(eu_pf_with_chf_instr)

    #### Instrument ranking for swiss client
    ch_pf_instr = load_ch_portfolio_instruments()
    verify_ch_portfolio_instruments(ch_pf_instr)


def verify_ch_portfolio_instruments(ch_pf_instr):
    ranking = compute_instrument_ranks(ch_pf_instr, ch_cl=True)
    print("Ranking of CH portfolio is", ranking, "and eligible for new investments")
    return ranking


def verify_eu_portfolio_instruments(eu_pf_with_chf_instr):
    ranking = compute_instrument_ranks(eu_pf_with_chf_instr, ch_cl=False)
    print("Ranking of EU portfolio is", ranking, "and to high for new investments")
    return ranking


def verify_regulatory_definition(ch_pf, eu_pf, eu_pf_with_chf, intl_pf):
    print("International mandator portfolio restricted:", is_restricted(intl_pf))
    print("European mandator portfolio restricted:", is_restricted(eu_pf))
    print("European mandator portfolio with swiss currency restricted:", is_restricted(eu_pf_with_chf))
    print("Swiss mandator portfolio restricted:", is_restricted(ch_pf))


def load_ch_portfolio_instruments():
    ch_pf_instr = [
        {"currency": "CHF", "ignore": False, "expired": False},
        {"currency": "EUR", "ignore": False, "expired": False},
    ]
    return ch_pf_instr


def load_eu_portfolio_instruments():
    eu_pf_with_chf_instr = [
        {"currency": "CHF", "ignore": False, "expired": False},
        {"currency": "EUR", "ignore": True, "expired": False},
    ]
    return eu_pf_with_chf_instr


def load_instruments():
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
    return ch_pf, eu_pf, eu_pf_with_chf, intl_pf