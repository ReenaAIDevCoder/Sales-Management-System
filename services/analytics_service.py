def calculate_total_revenue(opportunities):
    """
    Calculate revenue from won opportunities.
    """

    return sum(
        opportunity.deal_value or 0
        for opportunity in opportunities
        if opportunity.status == "Won"
    )


def calculate_total_opportunities(
    opportunities
):
    """
    Return total number of opportunities.
    """

    return len(opportunities)


def calculate_won_opportunities(
    opportunities
):
    """
    Return number of won opportunities.
    """

    return sum(
        1
        for opportunity in opportunities
        if opportunity.status == "Won"
    )


def calculate_lost_opportunities(
    opportunities
):
    """
    Return number of lost opportunities.
    """

    return sum(
        1
        for opportunity in opportunities
        if opportunity.status == "Lost"
    )


def calculate_win_rate(opportunities):
    """
    Calculate opportunity win rate.
    """

    total = len(opportunities)

    if total == 0:
        return 0

    won = sum(
        1
        for opportunity in opportunities
        if opportunity.status == "Won"
    )

    return round(
        (won / total) * 100,
        2
    )


def calculate_average_deal_value(
    opportunities
):
    """
    Calculate average deal value.
    """

    if not opportunities:
        return 0

    total_value = sum(
        opportunity.deal_value or 0
        for opportunity in opportunities
    )

    return round(
        total_value / len(opportunities),
        2
    )