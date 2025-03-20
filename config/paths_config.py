import os

####### DATA INGESTION ###########

RAW_DIR="artifacts/raw"
RAW_FILE_PATH=os.path.join(RAW_DIR,"raw.csv")
TRAIN_FILE_PATH=os.path.join(RAW_DIR,"train.csv")
TEST_FILE_PATH=os.path.join(RAW_DIR,"test.csv")

CONFIG_PATH = os.path.join("config", "config.yaml")

####### DATA PROCESSING ###########

PROCESSED_DIR="artifacts/processed"
ANIMELIST_CSV=r"artifacts\raw\animelist.csv"
ANIME_CSV=r"artifacts\raw\anime.csv"
ANIME_SYNOPSIS=r"artifacts\raw\anime_with_synopsis.csv"
X_TRAIN_ARRAY=os.path.join(PROCESSED_DIR,"X_train_array.pkl")
X_TEST_ARRAY=os.path.join(PROCESSED_DIR,"X_test_array.pkl")
Y_TRAIN=os.path.join(PROCESSED_DIR,"y_train.pkl")
Y_TEST=os.path.join(PROCESSED_DIR,"y_test.pkl")

RATINF_DF=os.path.join(PROCESSED_DIR,"rating_df.csv")
DF=os.path.join(PROCESSED_DIR,"anime_df.csv")
SYNOPSIS_DF=os.path.join(PROCESSED_DIR,"synopsis_df.csv")

USER2USER_ENCODED = r"artifacts/processed/user2user_encoded.pkl"
USER2USER_DECODED = r"artifacts/processed/user2user_decoded.pkl"

ANIME2ANIME_ENCODED = r"artifacts/processed/anime2anime_encoded.pkl"
ANIME2ANIME_DECODED = r"artifacts/processed/anime2anime_decoded.pkl"


####### MODEL TRAINING ###########


MODEL_DIR = "artifacts/model"
WEIGHTS_DIR = "artifacts/weights"
MODEL_PATH = os.path.join(MODEL_DIR,"model.h5")
ANIME_WEIGHTS_PATH = os.path.join(WEIGHTS_DIR,"anime_weights.pkl")
USER_WEIGHTS_PATH = os.path.join(WEIGHTS_DIR,"user_weights.pkl")
CHECKPOINT_FILE_PATH = "artifacts/model_checkpoint/weights.weights.h5"