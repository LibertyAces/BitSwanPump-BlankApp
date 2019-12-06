import bspump


class ShakespeareanEnricher(bspump.Processor):

	def process(self, context, event):
		if isinstance(event, bytes):
			event = event.decode("utf-8").replace('\r', '').replace('\n', '')
		return 'To {0}, or not to {0}?'.format(event)
