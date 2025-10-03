import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("यह Azure Function चालू हो गया है।")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get("name")

    if name:
        return func.HttpResponse(f"नमस्ते, {name}!", status_code=200)
    else:
        return func.HttpResponse(
            "कृपया 'name' भेजें ताकि मैं नमस्ते कह सकूं।",
            status_code=400
        )
