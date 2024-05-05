#Evaulation with precision, recall and F1-score


from collections import Counter

def read_data(file_path):
    """Read and process the NER data from a list of strings representing file content."""
    tokens, labels = [], []
    current_tokens, current_labels = [], []

    with open(file_path, 'r') as file:   # Read file
        data = file.read().splitlines()

    collecting = False
    for line in data:
        line = line.strip()
        print(line)
        if line == '<s>':
            collecting = True  # Start collecting tokens and labels
        elif line == '</s>':
            if collecting:
                # Append the collected tokens and labels to the main list
                tokens.append(current_tokens)
                labels.append(current_labels)
                current_tokens, current_labels = [], []
            collecting = False
        elif collecting:
            if line:
                parts = line.split()
                if len(parts) > 1:
                    token, label = parts[0], parts[-1]
                    current_tokens.append(token)
                    current_labels.append(label)
                else:
                    # This case handles lines that may not be properly formatted
                    current_tokens.append(line)
                    current_labels.append('O')  # Default label if none provided

    return tokens, labels

def compute_metrics(true_labels, pred_labels):
    """Compute precision, recall, and F1-score based on true and predicted labels."""
    tp, fp, fn = 0, 0, 0
    for true, pred in zip(true_labels, pred_labels):
        true_counter = Counter(true)
        pred_counter = Counter(pred)

        for key in pred_counter:
            if key in true_counter:
                tp += min(true_counter[key], pred_counter[key])
            fp += pred_counter[key]
        
        for key in true_counter:
            if key not in pred_counter:
                fn += true_counter[key]
            else:
                fn += max(0, true_counter[key] - pred_counter[key])

    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall = tp / (tp + fn) if tp + fn > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    return precision, recall, f1_score

# Paths to the files
predicted_file = 'data/predictDataLarge.txt'
true_file = 'data/trueDataLarge.txt'

# Read data
predicted_tokens, predicted_labels = read_data(predicted_file)
true_tokens, true_labels = read_data(true_file)

print('true label', true_labels)
print('predicted label', predicted_labels)

# Compute metrics
precision, recall, f1_score = compute_metrics(true_labels, predicted_labels)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1_score:.4f}")
