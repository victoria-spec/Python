def check_positive(number):
    if number < 0:
        raise Exception ("create an error")  # Raising the exception type without a message
    return number

try:
    result = check_positive(-10)
except Exception as e:
   print(f"An exception occurred: The number must be non-negative. {e} "  )

