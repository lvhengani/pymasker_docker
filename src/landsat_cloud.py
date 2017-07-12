import os
import argparse
import config
from pymasker import LandsatMasker
from pymasker import LandsatConfidence

# get the configuration
landsat_scenes_path = config.landsat_data_dir

# Get User Inputs
parser = argparse.ArgumentParser(description="A utility for generating landsat Cloud Mask")
parser.add_argument('scene', help='An input scene. Use original USGS scene and band identification format')
parser.add_argument('confidence', help='The confidence of the clouds/shadow', choices=['none', 'undefined', 'low', 'medium', 'high'])
parser.add_argument('-C', '--collection', help='The collection number of the scene, for pre-collection use 0', choices=[0, 1], type=int, default=1)
parser.add_argument('--shadow', help='Include cloud shadows', action='store_true')

args = parser.parse_args()
sceneID = args.scene
collection = args.collection
shadow = args.shadow

bqa_band_path = "{0}/{1}/{1}_BQA.TIF".format(landsat_scenes_path,sceneID)
output_cloud_mask_path = "{0}/{1}/{1}_bqa_cloud_mask.TIF".format(landsat_scenes_path,sceneID)
output_shadow_mask_path = "{0}/{1}/{1}_bqa_cloud_shadow_mask.TIF".format(landsat_scenes_path,sceneID) 

# load the QA band directly
#
# The "collection" parameter is required for landsat to specify the collection
# number. Acceptable number: 0 (pre-collection), 1 (collection-1)
#
masker = LandsatMasker(bqa_band_path, collection=1)

# algorithm has high confidence that this condition exists
# (67-100 percent confidence)
conf = LandsatConfidence.medium

# Get mask indicating cloud pixels with high confidence
cloud_mask = masker.get_cloud_mask(conf, cumulative=True)

# save the result
masker.save_tif(cloud_mask, output_cloud_mask_path)
if shadow:
    # Get mask indicating cloud pixels with high confidence
    cloud_shadow_mask = masker.get_cloud_shadow_mask(conf, cumulative=True)
    masker.save_tif(cloud_shadow_mask, output_shadow_mask_path)

# Done    