from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Check anonymized text
    assert result.text == "My name is BIP."

    # Check there is exactly one replacement item
    assert len(result.items) == 1

    # Convert OperatorResult object to dict
    item = result.items[0].to_dict()

    # Check start and end positions
    assert item["start"] == 11
    assert item["end"] == 14
    assert item["entity_type"] == "PERSON"
    assert item["text"] == "BIP"
    assert item["operator"] == "replace"
