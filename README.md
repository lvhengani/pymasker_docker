# Pymasker_Docker

This is a docker for running Pymasker. Pymasker is a python package to generate various masks from the Landsat 8 Quality Assessment band and MODIS land products.
The original pymasker together with documentation can be found at [**pymasker**](https://github.com/haoliangyu/pymasker)

## Usage

### Get The Docker Files into Your PC

Assuming that git is installed on you compouter, clone the repository to your computer using the command `git clone https://github.com/lvhengani/pymasker_docker.git`.

### Configurations

On the `docker-compose.yml` file edit the path `~/docker_landsat8_ba_c1/temp`, this is a full path to a directory with all your (extracted) Landsat-8 scenes.

### Build the Docker Image

To build the docker image run the command `./build` or in full `docker-compose -f docker-compose.yml build`
This must be run inside the directory pulled from github.

### Run Pymasker

To run pymasker run the command `./pymasker` as shown below:

```
./pymakser [source] [inpu.tif] [output.tif] [options]
```

Refer to [**pymasker**](https://github.com/haoliangyu/pymasker) for more information on how to use pymasker.

### Generate A Landsat Cloud Mask Using A Wrapper

The `landsat_cloud.py` wrapper was created to specifically run Landsat cloud masks.

```
./landsat_cloud [-h] [-C {0,1}] [--shadow] [scene] [confidence {none,undefined,low,medium,high}]

```

Example:

```
./landsat_cloud LC08_L1TP_168078_20170619_20170629_01_T1 medium -C 1 --shadow
where:
scene = LC08_L1TP_168078_20170619_20170629_01_T1
Confidence = medium
Landsat Collection [-C] = 1
--Shadow is a flag indicating that a cloud-shadow mask should also be generated 

```
After running, two files `LC08_L1TP_168078_20170619_20170629_01_T1_bqa_cloud_mask.TIF` and `LC08_L1TP_168078_20170619_20170629_01_T1_bqa_cloud_shadow_mask.TIF` will be saved in the folder `LC08_L1TP_168078_20170619_20170629_01_T1`.
 
### 


