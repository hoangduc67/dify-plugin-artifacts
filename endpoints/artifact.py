from werkzeug import Request, Response
from dify_plugin import Endpoint
import os

class ArtifactEndpoint(Endpoint):
    def _invoke(self, r: Request, values, settings) -> Response:
        try:
            html_path = os.path.join(os.path.dirname(__file__), "artifact.html")
            
            if not os.path.exists(html_path):
                return Response(
                    f"File does not exist: {html_path}",
                    status=404
                )
                
            with open(html_path, "r", encoding="utf-8") as f:
                html_content = f.read()
                
            html_content = html_content.replace("{{ bot_name }}", settings.get("bot_name", "Candy"))
                
            return Response(
                html_content,
                status=200,
                content_type="text/html"
            )
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(f"[ERROR] {error_msg}")
            return Response(error_msg, status=500)
