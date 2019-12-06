import asab
import asab.web
import asab.web.rest


class BlankHandler(object):

	def __init__(self, app, svc):
		self.BlankService = svc

		# Create a web container and add a route
		web_app = app.WebContainer.WebApp
		web_app.router.add_get("/blank", self.blank_get)  # Try with curl http://localhost:8080/blank?message=die

	async def blank_get(self, request):
		query = request.rel_url.query
		message = query.getone("message", "be")

		data = await self.BlankService.get_data(message)
		return asab.web.rest.json_response(request, data)
