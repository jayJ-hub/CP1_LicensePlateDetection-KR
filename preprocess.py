import os,sys, random
import cv2

import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import xml.etree.ElementTree as ET

cwd = os.getcwd()
root = cwd + r'\data_img'
folder = 'img_carWithLicense'
path = root + f'\{folder}'
file_list = [file for file in os.listdir(path) if file.endswith(".jpg")]
# print(file_list)

def load_img():
    images = []
    for file in file_list:
        img = cv2.imread(os.path.join(path, file))

        if img is not None:
            images.append(img)
    return images

def display_img(name, image):
    while True:
        cv2.imshow(name,image)
        cv2.waitKey(0)
        sys.exit() # to exit from all the processes
    
    cv2.destroyAllWindows() # destroy all windows


def resize_aug(xml_tree):
    size = xml_tree.findall("size")
    w = [x.findtext("width") for x in size]
    h = [y.findtext("height") for y in size]
    # print(w,h)
    
    if w >= h: #fit height
        return iaa.Resize({"height": "keep-aspect-ratio" , "width": 416})
        
    else : #fit  
        return iaa.Resize({"height": 416 , "width": "keep-aspect-ratio"})


def augmentate(index):
    ## call image
    img = cv2.imread(path + f'\{index}.jpg' , cv2.IMREAD_COLOR)
    ## parse xml file
    tree = ET.parse(path + f'\{index}.xml')
    ##call label
    label = tree.findall('object')
    label_true = [x.findtext("name") for x in label]
    # print(label_true[0])

    ##get bounding box value
    val = tree.findall("object/bndbox")
    xmin = [x.findtext("xmin")for x in val]
    ymin = [x.findtext("ymin")for x in val]
    xmax = [x.findtext("xmax")for x in val]
    ymax = [x.findtext("ymax")for x in val]
    box_val = [xmin,ymin,xmax,ymax]
    # print (box_val)
    
    ## draw bounding box to the image to augmentate
    input_img = img[np.newaxis, :, :, :]
    bbox = [ia.BoundingBox(x1=float(xmin[0]), y1=float(ymin[0]),
                       x2=float(xmax[0]), y2=float(ymax[0]),label=label_true[0])]
    # print(input_img.shape)


    #aug options
    seq = iaa.Sequential([
        resize_aug(tree),
        iaa.PadToSquare()
    ])

    #Aug image and bbox
    org = bbox[0].draw_on_image(input_img[0], size=5, color=[0, 255, 0])
    aug_img, aug_bbox = seq(images = input_img, bounding_boxes = bbox)
    draw = aug_bbox[0].draw_on_image(aug_img[0], size=5, color=[0, 255, 0])
    # print(org.shape, draw.shape)
    # print(bbox[0], aug_bbox[0])

    # ###view augmented
    # display_img(f'aug {index}', draw)
   
    return aug_img, box_val
    

def write_img(path):
    for image in images:
        cv2.imwrite(path, image)
    print("augmented images saved")
 
def image_aug_write(data):
    return [augmentate(d) for d in range(len(data))] #[img, bbox_value]


##get image list
data = load_img()

# ## for testing function
# index = random.randint(0, len(file_list))
# test_img = data[index]
# aug_img, box_val = augmentate(test_img)


data__img_bbx = image_aug_write(data)
# print(len(img_bbx))
# print(img_bbx[0])



