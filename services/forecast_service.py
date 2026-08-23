def calculate_pipeline_value(opportunities):
    """
    Calculate total value of open opportunities.
    """

    return sum(
        opportunity.deal_value or 0
        for opportunity in opportunities
        if opportunity.status == "Open"
    )


def calculate_weighted_forecast(opportunities):
    """
    Calculate weighted revenue forecast.

    Formula:

    Deal Value × Probability / 100
    """

    forecast = sum(
        (opportunity.deal_value or 0)
        *
        ((opportunity.probability or 0) / 100)
        for opportunity in opportunities
        if opportunity.status == "Open"
    )

    return round(forecast, 2)


def calculate_won_revenue(opportunities):
    """
    Calculate revenue generated from won opportunities.
    """

    return sum(
        opportunity.deal_value or 0
        for opportunity in opportunities
        if opportunity.status == "Won"
    )


def calculate_lost_value(opportunities):
    """
    Calculate value of lost opportunities.
    """

    return sum(
        opportunity.deal_value or 0
        for opportunity in opportunities
        if opportunity.status == "Lost"
    )