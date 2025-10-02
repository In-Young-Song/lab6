from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    text = "My name is Bond."
    start = 11
    end = 15

    result = sample_run_anonymizer(text, start, end)

    # Check anonymized text
    assert result.text == "My name is BIP."

    # Check there is exactly one replacement item
    assert len(result.items) == 1

    item = result.items[0].to_dict()
    assert item["start"] == 11
    assert item["end"] == 14
    assert item["entity_type"] == "PERSON"
    assert item["text"] == "BIP"
    assert item["operator"] == "replace"
