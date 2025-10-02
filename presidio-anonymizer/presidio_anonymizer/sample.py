from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(text: str, start: int, end: int, new_value: str = "BIP"):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Run anonymization
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(
                entity_type="PERSON",
                start=start,
                end=end,
                score=0.8,
            )
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": new_value})},
    )

    return result


if __name__ == "__main__":
    # Example input
    text = "My name is Bond."
    start = 11
    end = 15

    result = sample_run_anonymizer(text, start, end, "BIP")

    # Print exactly as required
    print("text:", result.text)
    print("items:")
    print(result.items)
