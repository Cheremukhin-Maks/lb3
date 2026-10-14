"""Парасольковий модуль (umbrella module) для доменних винятків.

Цей модуль реекспортує публічні винятки додатка для зручного імпорту.
"""
from app_package.exceptions.domain import ValidationError

__all__ = ["ValidationError"]
 
