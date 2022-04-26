import logging

import azure.functions as func

from urllib.parse import parse_qs


def main(req: func.HttpRequest) -> func.HttpResponse:
    # This function will parse the response of a form submitted using the POST method
    # The request body is a Bytes object
    # You must first decode the Bytes object to a string
    # Then you can parse the string using urllib parse_qs

    logging.info("Python HTTP trigger function processed a request.")
    req_body_bytes = req.get_body()
    logging.info(f"Request Bytes: {req_body_bytes}")
    req_body = req_body_bytes.decode("utf-8")
    logging.info(f"Request: {req_body}")

    plane = parse_qs(req_body)["plane"][0]
    flare = parse_qs(req_body)["flare"][0]

    return func.HttpResponse(
        f"You submitted this information: {plane} {flare}",
        status_code=200,
    )