#!/bin/bash


DATA_DIR="data"
TRAIN_PATH="$DATA_DIR/eng.testa"
TEST_PATH="$DATA_DIR/eng.train"


for ARG in "$@"
do
    key=$(echo $ARG | cut -f1 -d=)
    value=$(echo $ARG | cut -f2 -d=)

    if [[ $key == *"--"* ]]; then
        v="${key/--/}"
        declare $v="${value}"
    fi
done


echo "DATA_DIR = $DATA_DIR"
echo "TRAIN_PATH = $TRAIN_PATH"
echo "TEST_PATH = $TEST_PATH"


if [[ -z $TRAIN_PATH ]] || [[ -z $TEST_PATH ]] || [[ -z $DATA_DIR ]]; then
  echo "Usage: $(basename "$0")
  --TRAIN_PATH=[path to save train part of dataset]
  --TEST_PATH=[path to save test part of dataset]
  --DATA_DIR=[path to save dataset]"
  exit 1
fi


mkdir -p $DATA_DIR


# Load dataset:
wget https://raw.githubusercontent.com/synalp/NER/master/corpus/CoNLL-2003/eng.train -O $TRAIN_PATH
wget https://raw.githubusercontent.com/synalp/NER/master/corpus/CoNLL-2003/eng.testa -O $TEST_PATH
