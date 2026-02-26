"""
Consolidated Tool Registry — defines both schemas and implementations for the Shopping Agent.
"""
import json
import logging
from catalog_service import catalog_service
from payment_service import payment_service

logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────────────────────────────────────
# TOOLS SCHEMA
# ──────────────────────────────────────────────────────────────────────────────

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "search_products",
            "description": "Search for products (shoes, books, etc.) in the catalog. Prerequisite for buying.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search term, e.g. 'Brooks shoe'"},
                    "category": {"type": "string", "enum": ["shoes", "books"], "description": "Optional category filter"},
                    "size": {"type": "string", "description": "Shoe size (optional)"},
                    "max_price": {"type": "number", "description": "Maximum price limit (optional)"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_best_offer",
            "description": "Get the best price for a specific product. Prerequisite for checkout.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {"type": "string", "description": "The product ID, e.g. 'brooks_ghost'"},
                    "quantity": {"type": "integer", "description": "Units to purchase (default 1)", "minimum": 1}
                },
                "required": ["product_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "initiate_checkout",
            "description": "Triggers the secure payment UI. Call this IMMEDIATELY when the user confirms they want to buy.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {"type": "string", "description": "The product ID to purchase"},
                    "quantity": {"type": "integer", "description": "Units to purchase", "minimum": 1}
                },
                "required": ["product_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "process_payment",
            "description": "Process payment if user provides card details in chat.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {"type": "number"},
                    "card_type": {"type": "string", "enum": ["Visa", "Mastercard"]},
                    "card_number": {"type": "string"},
                    "card_expiry": {"type": "string"},
                    "card_cvc": {"type": "string"}
                },
                "required": ["amount", "card_type", "card_number", "card_expiry", "card_cvc"]
            }
        }
    }
]

# ──────────────────────────────────────────────────────────────────────────────
# TOOLS IMPLEMENTATION
# ──────────────────────────────────────────────────────────────────────────────

def search_products(query: str, category: str = None, size: str = None, max_price: float = None, **kwargs) -> dict:
    if max_price is not None:
        try:
            max_price = float(max_price)
        except (ValueError, TypeError):
            max_price = None
            
    results = catalog_service.search(query, category=category, size=size, max_price=max_price)
    if not results:
        return {"found": False, "message": f"No products found matching '{query}'."}

    return {
        "found": True,
        "count": len(results),
        "products": [
            {
                "id": r["id"],
                "name": r["name"],
                "brand": r["brand"],
                "category": r["category"],
                "description": r["description"],
                "base_price": r["base_price"],
                "image_url": r.get("image_url"),
            }
            for r in results
        ]
    }

def get_best_offer(product_id: str, quantity: int = 1, **kwargs) -> dict:
    # Ensure quantity is an integer
    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        quantity = 1
        
    offers = catalog_service.get_vendor_prices(product_id, quantity=quantity)
    if not offers:
        return {"found": False, "message": "No offers available."}

    best = min(offers, key=lambda x: x["unit_final_price"])
    return {"found": True, "best_offer": best}

def initiate_checkout(product_id: str, quantity: int = 1, **kwargs) -> dict:
    # Ensure quantity is an integer
    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        quantity = 1
    
    # Get the best offer to ensure we have the current offer details
    offers = catalog_service.get_vendor_prices(product_id, quantity=quantity)
    if not offers:
        return {"success": False, "message": "No offers available for checkout."}
    
    # Find the best offer by unit_final_price
    best = min(offers, key=lambda x: x["unit_final_price"])
    return {
        "success": True, 
        "message": f"✅ Checkout UI triggered for {quantity} unit(s) of '{product_id}'.",
        "checkout_details": {"product_id": product_id, "quantity": quantity},
        "offer_details": best  # Include offer details for frontend
    }

def process_payment(**kwargs) -> dict:
    return payment_service.process_payment(**kwargs)

# ──────────────────────────────────────────────────────────────────────────────
# EXECUTION ENGINE
# ──────────────────────────────────────────────────────────────────────────────

TOOL_MAP = {
    "search_products": search_products,
    "get_best_offer": get_best_offer,
    "initiate_checkout": initiate_checkout,
    "process_payment": process_payment,
}

def execute_tool(name: str, arguments: dict) -> dict:
    func = TOOL_MAP.get(name)
    if not func:
        return {"error": f"Tool '{name}' not found."}
    try:
        if isinstance(arguments, str):
            arguments = json.loads(arguments)
        return func(**arguments)
    except Exception as e:
        logger.error(f"Error executing tool {name}: {e}")
        return {"error": str(e)}
