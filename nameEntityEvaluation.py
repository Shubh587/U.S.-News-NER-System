def extract_entities(file_path):
    entities = []
    current_entity = []
    current_tag = None
    
    with open(file_path, 'r') as file:   # Read file
        data = file.read().splitlines()
    for line in data:
        if line.strip() in ['<s>', '</s>'] or not line.strip():
            continue
        word, tag = line.strip().split()
        if 'B-' in tag:
            if current_entity:
                entities.append((current_tag, ' '.join(current_entity)))
                current_entity = []
            current_tag = tag[2:]  # Strip the B- prefix
            current_entity.append(word)
        elif 'I-' in tag:
            if tag[2:] == current_tag:
                current_entity.append(word)
        else:
            if current_entity:
                entities.append((current_tag, ' '.join(current_entity)))
                current_entity = []
                current_tag = None
    
    # Capture any entity that might be at the end of the sentence
    if current_entity:
        entities.append((current_tag, ' '.join(current_entity)))
    
    return entities

def compute_metrics(true_entities, pred_entities):
    true_positives = 0
    false_positives = 0
    false_negatives = 0
    
    true_entities_set = set(true_entities)
    pred_entities_set = set(pred_entities)
    
    true_positives = len(true_entities_set & pred_entities_set)
    false_positives = len(pred_entities_set - true_entities_set)
    false_negatives = len(true_entities_set - pred_entities_set)
    
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return precision, recall, f1_score



# Extract entities from predicted and true sets
pred_entities = extract_entities('data/predictDataSmall.txt')
true_entities = extract_entities('data/trueDataSmall.txt')

# Compute metrics
precision, recall, f1_score = compute_metrics(true_entities, pred_entities)

print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1 Score: {f1_score:.3f}")