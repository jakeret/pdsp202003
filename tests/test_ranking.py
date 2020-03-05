from pdsp import ranking


class TestComputeInstrumentRanks:

    def test_compute_instrument_ranks_swiss_client_empty_instruments(self):
        rating = ranking.compute_instrument_ranks_for_swiss_clients([])
        assert 0 == rating

    def test_compute_instrument_ranks_swiss_client(self):
        instruments = [
            dict(currency="CHF", ignore=False, expired=False),
            dict(currency="EUR", ignore=False, expired=False),
        ]
        rating = ranking.compute_instrument_ranks_for_swiss_clients(instruments)
        assert 7 == rating

    def test_compute_instrument_ranks_swiss_client_ignored_instruments(self):
        instruments = [
            dict(currency="CHF", ignore=False, expired=False),
            dict(currency="EUR", ignore=True, expired=False),
        ]
        rating = ranking.compute_instrument_ranks_for_swiss_clients(instruments)
        assert 1 == rating

    def test_compute_instrument_ranks_swiss_client_expired_instruments(self):
        instruments = [
            dict(currency="CHF", ignore=False, expired=False),
            dict(currency="EUR", ignore=False, expired=True),
        ]
        rating = ranking.compute_instrument_ranks_for_swiss_clients(instruments)
        assert 1 == rating

    def test_compute_instrument_ranks_swiss_client_ignored_and_expired_instruments(self):
        instruments = [
            dict(currency="CHF", ignore=False, expired=False),
            dict(currency="CHF", ignore=True, expired=False),
            dict(currency="CHF", ignore=False, expired=True),
            dict(currency="EUR", ignore=True, expired=True),
        ]
        rating = ranking.compute_instrument_ranks_for_swiss_clients(instruments)
        assert 1 == rating

    def test_compute_instrument_ranks_non_swiss_client_empty_instruments(self):
        rating = ranking.compute_instrument_rank_for_non_swiss_clients([])
        assert rating == 0

    def test_compute_instrument_ranks_non_swiss_client(self):
        instruments = [
            dict(currency="CHF", ignore=False, expired=False),
            dict(currency="EUR", ignore=False, expired=False),
        ]
        rating = ranking.compute_instrument_rank_for_non_swiss_clients(instruments)
        assert 200 == rating

    def test_compute_instrument_ranks_non_swiss_client_ignored_instruments(self):
        instruments = [
            dict(currency="CHF", ignore=False, expired=False),
            dict(currency="EUR", ignore=True, expired=False),
        ]
        rating = ranking.compute_instrument_rank_for_non_swiss_clients(instruments)
        assert 200 == rating


class TestIsRestricted:

    def test_is_restricted_international_mandator(self):
        portfolio = dict(mandator="INTL", currency="USD")
        assert ranking.is_restricted(portfolio) == True
        assert "prechecked" not in portfolio

    def test_is_restricted_non_swiss_mandator_swiss_currency(self):
        portfolio = dict(mandator="EU", currency="CHF")
        assert ranking.is_restricted(portfolio) == False

    def test_is_restricted_eu_mandator(self):
        portfolio = dict(mandator="EU", currency="USD")
        assert ranking.is_restricted(portfolio) == True
        assert "prechecked" not in portfolio

    def test_is_restricted_eu_mandator_swiss_portfolio(self):
        portfolio = dict(mandator="CH", currency="CHF")
        assert ranking.is_restricted(portfolio) == False

