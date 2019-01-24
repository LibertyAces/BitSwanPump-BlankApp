#!/usr/bin/env python3
import logging
import asyncio
import asab
import bspump
import bspump.file
import bspump.common
import bspump.trigger
from  bspump.abc.processor import Processor

###

L = logging.getLogger(__name__)

###

class SamplePipeline(bspump.Pipeline):

	def __init__(self, app, pipeline_id):
		super().__init__(app, pipeline_id)

		source_config = {'path': 'sample.csv', 'delimiter': ','}
		source_trigger = bspump.trigger.RunOnceTrigger(app)

		self.build(
			bspump.file.FileCSVSource(app, self, config=source_config).on(source_trigger),
			AliasEnricher(app, self),
			bspump.common.PPrintSink(app, self)
		)



class AliasEnricher(Processor):

	def process(self, context, event):
		alias = event ['name'][0] + event['surname']
		event['alias'] = alias.lower ()

		return event


if __name__ == '__main__':
	app = bspump.BSPumpApplication()

	svc = app.get_service("bspump.PumpService")

	# Construct and register Pipeline
	pl = SamplePipeline(app, 'SamplePipeline')
	svc.add_pipeline(pl)

	app.run()
