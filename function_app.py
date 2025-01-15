import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="fizzbuzz")  # Behalte die bestehende Route
def fizzbuzz(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing Prime Factorization request.')

    try:
        # Hole den Parameter 'number'
        number = int(req.params.get('number'))
        
        # Validierung: Zahl muss positiv sein
        if number <= 0:
            return func.HttpResponse(
                "Invalid input. Please provide a positive integer in the query string, e.g., ?number=56",
                status_code=400
            )
        
        # Logik für die Primfaktorzerlegung
        factors = []
        divisor = 2
        while divisor ** 2 <= number:
            while number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            divisor += 1
        if number > 1:
            factors.append(number)

        # Rückgabe der Antwort
        return func.HttpResponse(
            f"The prime factors of {number} are: {factors}",
            status_code=200
        )
    
    except (ValueError, TypeError):
        return func.HttpResponse(
            "Invalid input. Please provide a valid integer in the query string, e.g., ?number=56",
            status_code=400
        )
