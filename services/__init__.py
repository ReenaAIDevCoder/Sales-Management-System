"""
Business logic and service layer
for the Sales Management System.
"""

from .sales_service import (
    calculate_sales_target,
    calculate_target_achievement
)

from .forecast_service import (
    calculate_pipeline_value,
    calculate_weighted_forecast
)

from .notification_service import (
    create_notification
)

from .analytics_service import (
    calculate_win_rate,
    calculate_total_revenue
)