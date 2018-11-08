from __future__ import print_function

import tensorflow as tf

#HelloWorld
hello = tf.constant('Hello, TensorFlow!')
sess2 = tf.Session()
print(sess2.run(hello))

#Leah's code here
file = open("./kafka.data", "r")
labels_arr = []
lineCounter = 0

for line in file:
  start = 0 #reset start of line range
  for symbol in range(0, len(line)-1):
    if(symbol == 161):
      letter = line[162:len(line)-1]
      labels_arr.append(letter)
  lineCounter += 1 #we are on the next line for reading

print(labels_arr, " ")
remove_dups_labels_arr = set(labels_arr)
print(remove_dups_labels_arr)

filenames = tf. train.string_input_producer(["./k3.csv"]);
reader = tf.TextLineReader()
key, value = reader.read(filenames)


# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
r = [[1.0]]*27;
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22, col23, col24, col25,  col26, col27 = tf.decode_csv(value, record_defaults=r, field_delim=' ')
features = tf.stack([col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22, col23, col24, col25,  col26, col27])

with tf.Session() as sess:
  # Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)

  for i in range(50):
    # Retrieve a single instance:
    example, label = sess.run([features, col27]) #change col27 with a different list of the labels

  coord.request_stop()
  coord.join(threads)

  print("rly go fuck yourself")

