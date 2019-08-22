import bspump


class ShakespeareanEnricher(bspump.Processor):

	def process(self, context, event):
		msg = event.decode("utf-8").replace('\n','')
		return 'To {0}, or not to {0}?'.format(msg)
