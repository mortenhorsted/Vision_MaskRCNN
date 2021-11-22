import pixellib
from pixellib.custom_train import instance_custom_training

#vis_img = instance_custom_training()
#vis_img.load_dataset("datasetSG")
#vis_img.visualize_sample()

#import warnings
#warnings.filterwarnings('ignore')


###Training Code###

import pixellib
from pixellib.custom_train import instance_custom_training


#train_maskrcnn = instance_custom_training()
#train_maskrcnn.modelConfig(network_backbone = "resnet101", num_classes= 2)
#train_maskrcnn.load_dataset("datasetSG")
#train_maskrcnn.evaluate_model("mask_rccn_models/mask_rcnn_model.023-0.141302.h5")



######### WORKING !!!!!!!!!!!!!!!!

# import pixellib
# from pixellib.instance import custom_segmentation
#
# segment_image = custom_segmentation()
# segment_image.inferConfig(num_classes= 2, class_names= ["BG", "indicator", "glass"])
# segment_image.load_model("mask_rcnn_models/mask_rcnn_model.040-0.132847.h5")
# segment_image.segmentImage("Testing1.jpg", show_bboxes=True, output_image_name="Testing1_out.jpg")
# segment_image.segmentImage("Testing2.jpg", show_bboxes=True, output_image_name="Testing2_out.jpg")

#################################

import pixellib
from pixellib.instance import custom_segmentation

segment_image = custom_segmentation()
segment_image.inferConfig(num_classes= 2, class_names= ["BG", "indicator", "glass"])
segment_image.load_model("mask_rcnn_models/mask_rcnn_model.040-0.132847.h5")
segment_image.segmentImage("sample1.jpg", show_bboxes=True, output_image_name="output_sample1.jpg",
extract_segmented_objects= True, save_extracted_objects=True)