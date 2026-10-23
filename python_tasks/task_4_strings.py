# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    # TODO: Implement logic
    string_list = sku_string.split("-")
    cap_string = [s.capitalize() for s in string_list]
        
    return " ".join(cap_string)
    

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"
print(format_sku("brake-pads-ceramic"))