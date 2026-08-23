def calculate_sales_target(target_amount, achieved_amount):
    """
    Calculate remaining sales target.
    """

    target_amount = target_amount or 0
    achieved_amount = achieved_amount or 0

    remaining = target_amount - achieved_amount

    return max(remaining, 0)


def calculate_target_achievement(
    target_amount,
    achieved_amount
):
    """
    Calculate sales target achievement percentage.
    """

    target_amount = target_amount or 0
    achieved_amount = achieved_amount or 0

    if target_amount <= 0:
        return 0

    percentage = (
        achieved_amount / target_amount
    ) * 100

    return round(percentage, 2)


def calculate_total_target(targets):
    """
    Calculate total target amount.
    """

    return sum(
        target.target_amount or 0
        for target in targets
    )


def calculate_total_achieved(targets):
    """
    Calculate total achieved amount.
    """

    return sum(
        target.achieved_amount or 0
        for target in targets
    )