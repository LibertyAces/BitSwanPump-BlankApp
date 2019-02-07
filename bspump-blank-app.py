#!/usr/bin/env python3
import sys

import logging
import asyncio
import asab
import bspump
import bspump.socket
import bspump.common
import bspump.trigger
from  bspump.abc.processor import Processor

###

L = logging.getLogger(__name__)

###

class BlankPipeline(bspump.Pipeline):

	def __init__(self, app, pipeline_id):
		super().__init__(app, pipeline_id)

		# source_config = {'path': 'sample.csv', 'delimiter': ','}

		self.build(
			bspump.socket.TCPSource (app, self, config={"host":"0.0.0.0", "port": 8888}),
			ShakespeareanEnricher(app, self),
			bspump.common.PPrintSink(app, self)
		)



class ShakespeareanEnricher(Processor):

	def process(self, context, event):

		msg = event.decode("utf-8").replace ('\n','')
		s_msg = 'To {0}, or not to {0}?'.format (msg)
		return s_msg




if __name__ == '__main__':
	app = bspump.BSPumpApplication()

	svc = app.get_service("bspump.PumpService")

	# Construct and register Pipeline
	pl = BlankPipeline(app, 'blank_pipeline')
	svc.add_pipeline(pl)

	app.run()
