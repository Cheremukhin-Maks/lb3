"""
Парасольковий модуль (umbrella module) додатка.

Реекспортує публічні винятки та сервісні функції для зручного зовнішнього імпорту.
"""

from .exceptions.domain import (
    BaseError,
    ValidationError,
    ResourceError,
    BusinessLogicError,
)
from .services.processors import check_balance, load, payment

__all__ = [
    "BaseError",
    "ValidationError",
    "ResourceError",
    "BusinessLogicError",
    "check_balance",
    "load",
    "payment",
]
 
