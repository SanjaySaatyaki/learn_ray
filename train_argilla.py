from datasets import load_dataset
import requests
import zipfile

def download_from_argilla():
    body = {"workspace_name": "h2", "dataset_name": "tryout", "export_type": "full" }
    response = requests.post("http://localhost:6901/export/dataset/", json=body)
    with open("dataset.zip", "wb") as f:
        f.write(response.content)

# zipfile.ZipFile("dataset.zip").extractall("dataset")

# download_from_argilla()
dataset = load_dataset(path="dataset")
data = dataset['train'][0]
print(data)