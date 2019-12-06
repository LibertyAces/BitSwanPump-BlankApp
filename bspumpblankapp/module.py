import asab

from .handler import BlankHandler
from .service import BlankService


class BlankModule(asab.Module):
	def __init__(self, app):
		super().__init__(app)

		self.BlankService = BlankService(app)
		self.BlankHandler = BlankHandler(app, self.BlankService)
