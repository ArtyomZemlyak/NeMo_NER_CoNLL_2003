import os
from tqdm import tqdm


DATA_DIR = "./data"
TRAIN_PATH = os.path.join(DATA_DIR, "eng.testa")
TEST_PATH = os.path.join(DATA_DIR, "eng.train")


def read_data(file):
    lines = open(file, "r").readlines()
    data = {"sentences": [], "labels_per_sent": []}
    sentence, labels = [], []

    for line in tqdm(lines):
        line = line.strip()

        if not line:
            if sentence and labels:
                assert len(sentence) == len(labels)
                data["sentences"].append(" ".join(sentence))
                data["labels_per_sent"].append(" ".join(labels))
                sentence, labels = [], []
            continue

        if line.startswith("-DOCSTART-"):
            continue
        else:
            values = line.split(" ")
            try:
                token, _, _, label = values
                sentence.append(token)
                if label != "O":
                    labels.append(label.split("-")[-1])
                else:
                    labels.append(label)

            except Exception as e:
                print(f"Error has occur: {e}")
                continue

    data["sentences"].append("")
    data["labels_per_sent"].append("")

    return "\n".join(data["sentences"]), "\n".join(data["labels_per_sent"])


x_train, y_train = read_data(TRAIN_PATH)
x_test, y_test = read_data(TEST_PATH)


with open(os.path.join(DATA_DIR, "text_train.txt"), "w") as f:
    f.write(x_train)

with open(os.path.join(DATA_DIR, "labels_train.txt"), "w") as f:
    f.write(y_train)

with open(os.path.join(DATA_DIR, "text_dev.txt"), "w") as f:
    f.write(x_test)

with open(os.path.join(DATA_DIR, "labels_dev.txt"), "w") as f:
    f.write(y_test)
