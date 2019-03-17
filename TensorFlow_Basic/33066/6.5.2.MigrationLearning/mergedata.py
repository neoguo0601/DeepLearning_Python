import glob
import os.path
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

processed_data_1 = np.load("../../../Data/flower_photos/flower_processed_data_daisy.npy")
processed_data_2 = np.load("../../../Data/flower_photos/flower_processed_data_dandelion.npy")
processed_data_3 = np.load("../../../Data/flower_photos/flower_processed_data_roses.npy")
processed_data_4 = np.load("../../../Data/flower_photos/flower_processed_data_sunflowers.npy")
processed_data_5 = np.load("../../../Data/flower_photos/flower_processed_data_tulips.npy")

training_images = []
training_labels = []
testing_images = []
testing_labels = []
validation_images = []
validation_labels = []

process_data = [processed_data_1, processed_data_2, processed_data_3, processed_data_4, processed_data_5]

for data in process_data:
    data[0] = data[0][:300]
    training_images += data[0]

    data[1] = data[1][:300]
    training_labels += data[1]

    data[2] = data[2][:20]
    validation_images += data[2]

    data[3] = data[3][:20]
    validation_labels += data[3]

    data[4] = data[4][:20]
    testing_images += data[4]

    data[5] = data[5][:20] 
    testing_labels += data[5]


state = np.random.get_state()
np.random.shuffle(training_images)
np.random.set_state(state)
np.random.shuffle(training_labels)

result = np.asarray([training_images, training_labels,
validation_images, validation_labels,
testing_images, testing_labels])

np.save("../../../Data/flower_photos/flower_processed_data.npy", result)