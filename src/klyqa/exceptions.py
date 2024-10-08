"""Exceptions for Klyqa Lights."""


class KlyqaError(Exception):
    """Generic Klyqa Light exception."""


class KlyqaConnectionError(KlyqaError):
    """Klyqa Light connection exception."""


class KlyqaAuthenticationError(KlyqaError):
    """Klyqa Light Authentication exception."""

class KlyqaDeviceNotFoundError(KlyqaError):
    """Klyqa Cloud device not found exception."""
