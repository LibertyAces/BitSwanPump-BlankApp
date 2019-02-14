# Creating blank BitSwan BSPump application

## Prerequisites
 - python3
 - pip
 - docker



## Install
Install required libraries:
```bash
$ pip install asab bspump 
```
Clone git repository to your work directory:
```bash
$ git clone git@github.com:LibertyAces/BitSwanPump-BlankApp.git bspump-blank-app
```


## Run in docker
Move to the directory (it is `bspump-blank-app` in our case):
```bash
$ cd bspump-blank-app
```
Then you can build your docker image:
```bash
$ docker build -t bspump-blank-app .
```
Once you have your docker image built, run it in a container:
```bash
$ sudo docker run -p 8888:8888 bspump-blank-app
```
*We use port 8888 for TCP Sink in sample pipeline.*


## Test it works
In new terminal use netCat to connect to TCPSink:
```bash
nc -v localhost 8888
```
Now write any messge, "test" for example. You should see your message enriched in docker container `stderr`.


## Customize
From here you should have your BSPump application up and running. You may go on and customize it to your needs. 
Basic pipline structure is defined in pipeline init:
```python
    self.build(
        bspump.socket.TCPSource(app, self, config={"host":"0.0.0.0", "port": 8888}),
        ShakespeareanEnricher(app, self),
        bspump.common.PPrintSink(app, self, stream=sys.stderr)
    )
```
You can see the `TCPSource` at the beginning, followed by any number of processors, ending with sink. To customize the pipline simply replace any part of it by your own alternative.

You can find more information about available sources, sinks and processors at https://github.com/LibertyAces/BitSwanPump
