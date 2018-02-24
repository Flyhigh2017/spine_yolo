import os

#
# path and dataset parameter
#

DATA_PATH = '/Users/anekisei/Documents/spine/data/data_tracking_image_2'

LABEL_PATH = '/Users/anekisei/Documents/spine/data/label_02'


OUTPUT_DIR = os.path.join(DATA_PATH, 'output')

WEIGHTS_DIR = os.path.join(DATA_PATH, 'weights')

WEIGHTS_FILE = None
# WEIGHTS_FILE = os.path.join(DATA_PATH, 'weights', 'YOLO_small.ckpt')

CLASSES = {'bone' : '0'}
CLASSES_LIST = ['bone']

FLIPPED = True


#
# model parameter
#

ORI_HEIGHT = 600

ORI_WIDTH = 800

IMAGE_SIZE1 = 768

IMAGE_SIZE2 = 768

CELL_SIZE = 128

CELL_SIZE1 = 6

CELL_SIZE2 = 6

BOXES_PER_CELL = 1

ALPHA = 0.1

DISP_CONSOLE = True

OBJECT_SCALE = 1.0
NOOBJECT_SCALE = 1.0
CLASS_SCALE = 2.0
COORD_SCALE = 5.0


#
# solver parameter
#

GPU = ''

LEARNING_RATE = 0.0001

DECAY_STEPS = 30000

DECAY_RATE = 0.1

STAIRCASE = True

BATCH_SIZE = 50

MAX_ITER = 2

SUMMARY_ITER = 1

SAVE_ITER = 1000


#
# test parameter
#

THRESHOLD = 0.2

IOU_THRESHOLD = 0.5
