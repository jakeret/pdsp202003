from pdsp import eligibility


class TestEligibility:

    def test_verify_regulatory_definition(self):
        ch_pf, eu_pf, eu_pf_with_chf, intl_pf = eligibility.load_instruments()
        eligibility.verify_regulatory_definition(ch_pf, eu_pf, eu_pf_with_chf, intl_pf)

        assert "prechecked" not in intl_pf
        assert "prechecked" not in eu_pf
        assert "prechecked" in eu_pf_with_chf
        assert "prechecked" in ch_pf

    def test_verify_ch_portfolio_instruments(self):
        ch_pf_instr = eligibility.load_ch_portfolio_instruments()
        ranking = eligibility.verify_ch_portfolio_instruments(ch_pf_instr)
        assert 7 == ranking

    def test_verify_eu_portfolio_instruments(self):
        eu_pf_with_chf_instr = eligibility.load_eu_portfolio_instruments()
        ranking = eligibility.verify_eu_portfolio_instruments(eu_pf_with_chf_instr)
        assert 200 == ranking
