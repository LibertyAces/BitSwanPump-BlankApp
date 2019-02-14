#!/usr/bin/env python3
import sys
import asyncio
import bspump
import bspump.common
import bspump.socket


class MyPipeline(bspump.Pipeline):

	def __init__(self, app, pipeline_id):
		super().__init__(app, pipeline_id)

		self.build(
			bspump.socket.TCPSource(app, self, config={"host":"0.0.0.0", "port": 8888}),
			ShakespeareanEnricher(app, self),
			bspump.common.PPrintSink(app, self, stream=sys.stderr)
		)


class ShakespeareanEnricher(bspump.Processor):

	def process(self, context, event):
		msg = event.decode("utf-8").replace('\n','')
		return 'To {0}, or not to {0}?'.format(msg)


if __name__ == '__main__':
	app = bspump.BSPumpApplication()

	svc = app.get_service("bspump.PumpService")

	pl = MyPipeline(app, 'MyPipeline')
	svc.add_pipeline(pl)

	app.run()
