# Convert dollar in EURO

def convert_dollar(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

amount_in_dollars = 2200
exchange_rate = 0.92 # Exemple de taux de change pour convertir des dollars en euros

amount_in_euros = convert_dollar(amount_in_dollars, exchange_rate)
print(f"{amount_in_dollars} dollars équivalent à {amount_in_euros} euros")