# Delivery

## Fetching Delivery Data

```python
from crux import Crux

conn = Crux()

dataset = conn.get_dataset("A_DATASET_ID")
delivery = dataset.get_delivery("A_DELIVERY_ID")

if delivery.status == "DELIVERY_SUCCEEDED":
    for file in delivery.get_data()
        print(resource.id)
        file.download("/tmp/{}".format(resource.name))
```
## Fetching Delivery Raw Data

```python
from crux import Crux

conn = Crux()

dataset = conn.get_dataset("A_DATASET_ID")
delivery = dataset.get_delivery("A_DELIVERY_ID")

for file in delivery.get_raw()
    print(resource.id)
    file.download("/tmp/{}".format(resource.name))
```

## Fetching Ingestions

```python
from crux import Crux

conn = Crux()

dataset = conn.get_dataset("A_DATASET_ID")
ingestions = dataset.get_ingestions()

ingestion = next(ingestions)

# Get the DELTA data from the latest version of ingestion
for file in ingestion.get_data(accepted_status=["DELIVERY_SUCCEEDED"])
    print(resource.id)
    file.download("/tmp/{}".format(resource.name))

# Get the RAW data from the latest version of ingestion
for file in ingestion.get_raw()
    print(resource.id)
    file.download("/tmp/{}".format(resource.name))
```