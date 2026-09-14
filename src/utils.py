# Build: 21bbd5211cfc64b9ca0a8e8d10740c24

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
