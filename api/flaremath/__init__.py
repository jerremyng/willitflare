import logging
from pydoc import plainpager

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # plane = req.params.get('plane')
    # flare = req.params.get('flare')

    # return func.HttpResponse(
    #         f"Your plane is {plane} and flare is {flare}",
    #         status_code=200
    #     )


    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        # return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
        return func.HttpResponse(
        f"Your plane is {name} and flare is {name}",
        status_code=200
        )
    else:
        return func.HttpResponse(
            f"{name}",
            status_code=200
        )
