from decimal import Decimal, getcontext
from enum import Enum
from typing import List, Dict, Optional

# Set precision for Decimal operations to ensure accuracy in financial calculations.
# A precision of 18 is common for cryptocurrencies.
getcontext().prec = 18

# --- Enums ---
class Currency(Enum):
    """
    Defines the supported reward currencies for promotional bounties.
    """
    XDC = "XDC"
    ROXN = "ROXN"
    USDC = "USDC"