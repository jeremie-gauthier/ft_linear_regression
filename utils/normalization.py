def normalize(data, dataset):
    min_dataset = min(dataset)
    max_dataset = max(dataset)
    return (data - min_dataset) / (max_dataset - min_dataset)


def denormalize(data, dataset):
    min_dataset = min(dataset)
    max_dataset = max(dataset)
    return data * (max_dataset - min_dataset) + min_dataset
