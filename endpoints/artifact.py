from werkzeug import Request, Response
from dify_plugin import Endpoint

class ArtifactEndpoint(Endpoint):
    def _invoke(self, r: Request, values, settings) -> Response:
        return Response(
            "Redirecting to /asset/artifact.html",
            status=302,
            headers={"Location": "/asset/artifact.html"},
        )
