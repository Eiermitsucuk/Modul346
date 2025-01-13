import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="fizzbuzz")
def fizzbuzz(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing FizzBuzz request.')

    try:
        number = int(req.params.get('number'))
    except (ValueError, TypeError):
        return func.HttpResponse(
            "Invalid input. Please provide an integer in the query string, e.g., ?number=15",
            status_code=400
        )

    if number % 3 == 0 and number % 5 == 0:
        result = "FizzBuzz"
    elif number % 3 == 0:
        result = "Fizz"
    elif number % 5 == 0:
        result = "Buzz"
    else:
        result = str(number)

    return func.HttpResponse(
        f"The result for {number} is: {result}",
        status_code=200
    )
