LOG_FILE = 'LogFile-{%}.log'
BATCH_SIZE = 64

# Glove and Embedding Constants
GLOVE = '../glove/glove.6B.50d.txt'
GLOVE_SAVE = '../glove/loaded.pkl'
GLOVE_TOKENS = 6  # Billion
EMBEDDING_SIZE = 50  # Dimensions
TOKEN_TO_IDX_SAVE = '../data/token_to_index.pkl'
UNK_TOKEN = '<UNK>'
BEG_TOKEN = '<BEG'
END_TOKEN = '<END>'
UNK_IDX = 0
BEG_IDX = 1
END_IDX = 2

# Data Constants
DATA_DIR = '../data/'

# Debug Constants
DEBUG_DATA_SIZE = 1000
DEBUG_BATCH_SIZE = 16