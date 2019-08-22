import sys

import bspump
import bspump.common
import bspump.socket

from .processor import ShakespeareanEnricher


class TCPPipeline(bspump.Pipeline):

	def __init__(self, app, pipeline_id):
		super().__init__(app, pipeline_id)

		self.build(
			bspump.socket.TCPSource(app, self, config={"host":"0.0.0.0", "port": 8888}),
			ShakespeareanEnricher(app, self),
			bspump.common.PPrintSink(app, self, stream=sys.stderr)
		)
