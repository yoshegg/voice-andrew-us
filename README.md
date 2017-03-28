# voice-andrew-us

| Voicebuilding for Text-to-speech Synthesis (WS 2016/17) |
| ------------------------------------------------------- |
| Group 1                                                 |
| Christophe Biwer, Dana Ruiter, Andrew Johnson           |

## Report
Notes for the group report can be found [here](https://hackmd.io/OwMxGMCMCYDYFMC0AOAjMALIjAGewUBWATgJGmGkNWhwGYdl4g==) (registration required to edit).

## Dependencies
In order to work with this voice, the following command must be executed (on ubuntu) to get the desired dependencies:
```
sudo apt get sox praat speech-tools
```
There may be other requirements which need to be obtained via `apt`.

## Installation of the unit selection based voice
Run 
```
./gradlew legacyInit
```
followed by 
```
./gradlew build
```

To actually test the voice, enter
```
./gradlew run
```
and go to [http://localhost:59125](localhost:59125).

## Installation of the HMM based voice
### Install docker
... as explained [here](https://docs.docker.com/engine/installation/)

### Install the required container / image
Execute the dockerfile contained in the root folder of the projet (which originates from [https://github.com/psibre/marytts-dockerfiles](https://github.com/psibre/marytts-dockerfiles)) and run it with
```
docker build --build-arg HTKUSER=***** --build-arg HTKPASSWORD=***** -t marytts-builder-hsmm .
```
replace `HTKUSER` and `HTKPASSWORD` with the desired credentials ([Registration](http://htk.eng.cam.ac.uk/register.shtml) needed).

*I guess the unit selection based voice must already be installed to continue!*

### Meanwhile, because downloading the docker files may take some time, you can do the following:

Download the [MaryTTS Builder](https://github.com/marytts/marytts/releases/download/v5.2/marytts-builder-5.2.zip) and unpack it to *some location*

Go to the build directory of this project and run *some location*`/bin/voiceimport.sh`. Click on `Settings` and set `db.marybase` to `/marytts`. Don't forget to **save**.

Run the `HMMVoiceFeatureSelection` component.

### After docker has been installed:

Go to the build folder and start the docker container. By using the following command, you automatically execute the needed tasks:
```
sudo docker run -v `pwd`:`pwd` -w `pwd` -it 5.2 /bin/bash 'dockerScript.sh'
```
(the `dockerScript.sh` contained in the root folder of the project is the one that is tracked by git. Running `./gradlew legacyInit` copies it to the build folder)
