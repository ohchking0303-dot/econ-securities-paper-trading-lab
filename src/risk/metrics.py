def max_drawdown(equity_curve):
    """
    Calculate maximum drawdown from an equity curve.

    Parameters
    ----------
    equity_curve : list[float]
        Simulated portfolio value over time.

    Returns
    -------
    float
        Maximum drawdown as a negative decimal value.
    """
    if not equity_curve:
        return 0.0

    peak = equity_curve[0]
    max_dd = 0.0

    for value in equity_curve:
        peak = max(peak, value)
        drawdown = (value - peak) / peak
        max_dd = min(max_dd, drawdown)

    return max_dd


def simple_return(start_value, end_value):
    """
    Calculate simple return.
    """
    if start_value == 0:
        return 0.0
    return (end_value - start_value) / start_value
