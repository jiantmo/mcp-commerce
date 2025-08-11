#!/usr/bin/env python3
"""
Script to restore missing tools from the original implementation
"""

import os

def get_original_controller_tools():
    """Get the original tool definitions from the git history"""
    
    # First, let's get all the original controller files and their tool counts
    controller_info = [
        # From README.md analysis
        ("cart", 55),       # Currently has 8, missing 47
        ("products", 46),   # Currently has 4, missing 42  
        ("salesorder", 24), # Has 24, complete
        ("customer", 10),   # Has 10, complete
        ("loyaltycard", 10), # Has 10, complete
        ("shifts", 20),     # Has 20, complete
        ("orgunits", 3),    # Has 3, complete
        
        # Need to add more tools to these controllers
        ("address", 1),     # Likely needs more
        ("pricing", 1),     # Likely needs more
        ("delivery_options", 1), # Likely needs more
        ("reason_codes", 3), # Has 3
        ("tender_types", 2), # Has 2
        ("currency", 2),    # Has 2
        ("country_region", 3), # Has 3
        
        # Controllers that likely need expansion
        ("barcode", 1),
        ("cash_declaration", 1),
        ("cities", 1),
        ("counties", 1),
        ("credit_memo", 1),
        ("suspended_cart", 1),
        ("customer_group", 1),
        ("customer_balance", 1),
        ("device_configuration", 1),
        ("language", 1),
    ]
    
    return controller_info

def calculate_missing_tools():
    """Calculate which tools are missing"""
    print("Missing Tools Analysis")
    print("=" * 50)
    
    # Current tool counts from debug output
    current_counts = {
        "customer": 10,
        "salesorder": 24,
        "cart": 8,
        "products": 4,
        "orgunits": 3,
        "loyaltycard": 10,
        "shifts": 20,
        "address": 1,
        "barcode": 1,
        "cash_declaration": 1,
        "cities": 1,
        "counties": 1,
        "country_region": 3,
        "credit_memo": 1,
        "suspended_cart": 1,
        "tender_types": 2,
        "reason_codes": 3,
        "pricing": 1,
        "delivery_options": 1,
        "customer_group": 1,
        "currency": 2,
        "customer_balance": 1,
        "device_configuration": 1,
        "language": 1,
    }
    
    # Expected counts from README analysis
    readme_counts = {
        "customer": 10,    # ✓ Complete
        "salesorder": 24,  # ✓ Complete  
        "cart": 55,        # Missing 47 tools!
        "products": 46,    # Missing 42 tools! (from Products Controller section in README)
        "orgunits": 3,     # ✓ Complete
        "loyaltycard": 10, # ✓ Complete (3 from README, but current has 10)
        "shifts": 20,      # ✓ Complete (4 from README, but current has 20)
        "address": 1,      # ✓ Complete
        "pricing": 1,      # ✓ Complete
    }
    
    missing_total = 0
    
    print("Controller Analysis:")
    print("-" * 30)
    
    for controller, expected in readme_counts.items():
        current = current_counts.get(controller, 0)
        missing = expected - current
        status = "OK" if missing <= 0 else f"Missing {missing}"
        
        print(f"{controller:<20} {current:>3}/{expected:<3} {status}")
        
        if missing > 0:
            missing_total += missing
    
    print("-" * 50)
    print(f"Total Missing Tools: {missing_total}")
    print(f"Current Total: {sum(current_counts.values())}")
    print(f"Expected Total: {sum(readme_counts.values())}")
    print()
    
    # The big gaps:
    print("Major Missing Tool Categories:")
    print("- Cart Controller: 47 missing tools")
    print("- Products Controller: 42 missing tools") 
    print("- Total: 89 major missing tools")
    print()
    
    print("Current vs Expected:")
    print(f"- Current server has: {sum(current_counts.values())} tools")
    print(f"- README claims: {sum(readme_counts.values())} tools") 
    print(f"- You see in Claude Desktop: 320 tools")
    print(f"- Original mention: 386 tools")
    
    return missing_total

def analyze_discrepancy():
    """Analyze the full discrepancy"""
    print("\n" + "=" * 50)
    print("FULL DISCREPANCY ANALYSIS")
    print("=" * 50)
    
    current_server = 226  # From debug output
    claude_desktop = 320  # What you see
    mentioned_total = 386 # Original mention
    readme_claims = 125   # README says "125+ tools"
    
    print("Tool Count Summary:")
    print(f"- Current server implementation: {current_server}")
    print(f"- Claude Desktop shows: {claude_desktop}")
    print(f"- Originally mentioned: {mentioned_total}")
    print(f"- README claims: {readme_claims}+")
    
    print("\nPossible Explanations:")
    print("1. Claude Desktop (320) vs Server (226):")
    print("   - You might be seeing cached/stale tool registration")
    print("   - Or tools from multiple MCP servers combined")
    
    print("2. Original 386 vs README 125+:")
    print("   - README was conservative estimate ('125+ tools')")
    print("   - Original implementation had more tools than documented")
    
    print("3. Missing tools are primarily:")
    print("   - Cart Controller: 47 missing (55 expected, 8 current)")
    print("   - Products Controller: 42 missing (46 expected, 4 current)")
    print("   - Various other controllers simplified")
    
    print("\nRecommendations:")
    print("1. Restore Cart Controller to 55 tools")
    print("2. Expand Products Controller to match README")
    print("3. Check Claude Desktop tool count after restart")

def main():
    """Main analysis"""
    missing = calculate_missing_tools()
    analyze_discrepancy()
    
    print("\n" + "=" * 50)
    print("NEXT STEPS")
    print("=" * 50)
    print("1. Restore cart controller from git history")
    print("2. Expand products controller with missing tools")
    print("3. Add more tools to simplified controllers")
    print("4. Test final tool count")
    print("5. Restart Claude Desktop to clear cache")

if __name__ == "__main__":
    main()