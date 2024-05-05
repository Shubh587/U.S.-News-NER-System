def extract_named_entities(file_path):
    with open(file_path, 'r') as file:   # Read file
        data = file.read().splitlines()

    entities = []
    current_entity = []
    current_tag = None
    
    for line in data:
        line = line.strip()
        if line and line not in ['<s>', '</s>']:
            word, tag = line.split()
            if 'B-' in tag:
                if current_entity:
                    entities.append((current_tag, ' '.join(current_entity)))
                    current_entity = []
                current_tag = tag[2:]  # Get the type of the entity
                current_entity.append(word)
            elif 'I-' in tag:
                if current_tag == tag[2:]:
                    current_entity.append(word)
            else:
                if current_entity:
                    entities.append((current_tag, ' '.join(current_entity)))
                    current_entity = []
                    current_tag = None
    if current_entity:
        entities.append((current_tag, ' '.join(current_entity)))
    return entities

def compute_named_entity_metrics(predicted_data, true_data):
    true_entities = extract_named_entities(true_data)
    predicted_entities = extract_named_entities(predicted_data)
    
    true_entities_set = set(true_entities)
    predicted_entities_set = set(predicted_entities)
    
    true_positives = len(predicted_entities_set & true_entities_set)
    false_positives = len(predicted_entities_set - true_entities_set)
    false_negatives = len(true_entities_set - predicted_entities_set)
    
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return precision, recall, f1_score

# Calculate the named entity level metrics

precision, recall, f1_score = compute_named_entity_metrics('data/predictDataSmall.txt', 'data/trueDataSmall.txt')
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1 Score: {f1_score:.3f}")





