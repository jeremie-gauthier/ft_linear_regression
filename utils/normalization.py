def normalize(data):
    min_data = min(data)
    max_data = max(data)
    return map(lambda d: (d - min_data) / (max_data - min_data), data)


def denormalize(data, ref):
    min_data = min(ref)
    max_data = max(ref)
    return map(lambda d: (d * (max_data - min_data) + min_data), data)
