import asab

from .pipeline import TCPPipeline


class BlankService(asab.Service):

	def __init__(self, app, service_name="blank.BlankService"):
		super().__init__(app, service_name)

	async def initialize(self, app):
		svc = app.get_service("bspump.PumpService")

		# Create and register all connections here

		# Create and register all matrices here

		# Create and register all lookups here

		# Create and register all pipelines here

		self.TCPPipeline = TCPPipeline(app, "TCPPipeline")
		svc.add_pipeline(self.TCPPipeline)

		await svc.initialize(app)

	async def get_data(self, message="be"):
		await self.TCPPipeline.process(message)
		return "Check stdout"
