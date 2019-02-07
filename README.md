# Creating blank BSPump application

## Prerequisites
 - python3
 - pip
 - docker

Note that if you have multiple python installations, it is recommended to use ```pip3 install``` instead.



## Installation
Install required libraries:
```bash
$ pip install asab bspump 
```
Clone git repository to your work directory:
```bash
$ git clone https://github.com/TeskaLabs/bspump-blank-app.git
```



## Running via docker
Move to the directory (it is `bspump-blank-app` in our case):
```bash
$ cd bspump-blank-app
```
Then you can build your docker image:
```bash
$ docker build -t bspump-your-app .
```
Once you have your docker image built, run it in a container:
```bash
$ docker run bspump-your-app
```


## Customization
From here you should have working BSPump application up and running. You may go on and customize it to your needs. 


## Additional information
To see more information about available sources, sinks and processors go to  https://github.com/TeskaLabs/bspump.




<!---
### Creating a pipeline
Every pipeline is composed of a source, sink and optionally any number of processors.
See ```bspump-blank-app.py``` for more details on application setup.
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

Then you have to add it into your pipeline between source and sink.
```python
        self.build(
            bspump.file.FileCSVSource(app, self, config=source_config).on(source_trigger),
            AliasEnricher(app, self),
            bspump.common.PPrintSink(app, self)
        )
```

Of course, you can align as many processors as you want into the pipeline.
--->