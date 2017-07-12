# Docker for Pymasker

This is a docker for running Pymasker.
Pymasker is a python package to generate various masks from the Landsat 8 Quality Assessment band and MODIS land products.
The original pymasker together with documentation can be found at [**pymasker**](https://github.com/haoliangyu/pymasker)

## Usage

### Get The Docker Files into Your PC

Pull the repository ..

### Configurations

On the `docker-compose.yml` file edit the path `~/docker_landsat8_ba_c1/temp`, this is s full path to a directory with landsat-8 scenes.

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
