text = ("ability")
def check_string(text):
    text = text.lower()
    text = text.upper()
 
    result = text.startswith("a") or text.endswith("a")
    return result

if text.startswith("a") or text.endswith("a"):
    print("True")
