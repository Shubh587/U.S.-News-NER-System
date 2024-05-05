

def extract_tokens_and_labels(file_path):
    with open(file_path, 'r') as file:   # Read file
        data = file.read().splitlines()

    tokens_labels = []
    for line in data:
        line = line.strip()
        if line and line not in ['<s>', '</s>']:
            parts = line.split()
            if len(parts) == 2:
                tokens_labels.append(tuple(parts))
    return tokens_labels

def compute_token_level_metrics(predicted_data, true_data):
    predicted_tokens_labels = extract_tokens_and_labels(predicted_data)
    true_tokens_labels = extract_tokens_and_labels(true_data)
    
    predicted_tokens = {tpl for tpl in predicted_tokens_labels}
    true_tokens = {tpl for tpl in true_tokens_labels}

    true_positives = len(predicted_tokens & true_tokens)
    false_positives = len(predicted_tokens - true_tokens)
    false_negatives = len(true_tokens - predicted_tokens)

    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return precision, recall, f1_score

# Calculate the token level metrics
precision, recall, f1_score = compute_token_level_metrics('data/predictDataSmall.txt', 'data/trueDataSmall.txt')
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1 Score: {f1_score:.3f}")