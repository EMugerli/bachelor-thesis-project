# Hyperparameters

WORDS = ['backward', 'bed', 'bird', 'cat', 'dog', 'down', 'eight', 'five', 'follow', 'forward', 'four', 'go', 'happy', 'house', 'learn', 'left', 'marvin', 'nine', 'no', 'off', 'on', 'one', 'right', 'seven', 'sheila', 'six', 'stop', 'three', 'tree', 'two', 'up', 'visual', 'wow', 'yes', 'zero']

NUM_CLASSES = len(WORDS)
TEST_SIZE = 0.1
VALIDATION_SIZE = 0.1
EPOCHS = 20
BATCH_SIZE = 100
LEARNING_RATE = 0.0001
PATIENCE = 5
DROPOUT = 0.2

SAMPLE_RATE = 16000
MEL_BINS = 26
NUM_MFCC = 13
FFT_SIZE = 2048
HOP_SIZE = 512
