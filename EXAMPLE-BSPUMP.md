# BSPump sample

### Prerequisites
 - python3
 - pip

Note that if you have multiple python installations, it is recommanded to use ```pip3 install``` instead.

### Installation
Install required libraries
```bash
$ pip install asab bspump 
```
Clone git repository to your work directory
```bash
$ git clone https://github.com/TeskaLabs/bspump-example.git
```

### Creating pipleine
Every pipeline is composed of source, sink and optionaly any number of processors.
See ```bspump-example.py``` for more details on application setup.
```python
class SamplePipeline(bspump.Pipeline):

	def __init__(self, app, pipeline_id):
		super().__init__(app, pipeline_id)

		source_config = {'path': 'sample.csv', 'delimiter': ','}
		source_trigger = bspump.trigger.RunOnceTrigger(app)

		self.build(
			bspump.file.FileCSVSource(app, self, config=source_config).on(source_trigger),
			bspump.common.PPrintSink(app, self)
		)

```

### Creating custom processor
You can use existing, or create your own processor.
```python
class AliasEnricher(Processor):

	def process(self, context, event):
		alias = event ['name'][0] + event['surname']
		event['alias'] = alias.lower ()

		return event

```

Than you have to add it in to your pipeline between source and sink.
```python
		self.build(
			bspump.file.FileCSVSource(app, self, config=source_config).on(source_trigger),
			AliasEnricher(app, self),
			bspump.common.PPrintSink(app, self)
		)
```

Of course you can align as many processors as you want in to the pipeline.


### Running via docker
Move to the directory with a ```Dockerfile``` (it is ```bspump-example``` in our case). Than you can build your docker image.
```bash
$ docker build -t bspump-example .
```
Than you can run it in a container.
```bash
$ docker run bspump-example
```


### More Sinks and sources
Instead of csv source you can connect your pipeline to json file source, or elasticsearch, influxdb, kafka, mysql and many others. Same goes for sinks.

See readme and examples at https://github.com/TeskaLabs/bspump for more details.

