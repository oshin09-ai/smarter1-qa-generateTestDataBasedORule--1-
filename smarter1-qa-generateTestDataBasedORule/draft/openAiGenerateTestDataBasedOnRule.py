# import os
import openai
import json
from datetime import datetime

openai.api_key = "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"


def generate_test_data_based_on_rule_and_write_to_a_file(rule):
    # Format the current datetime in a Windows-friendly format
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Open the file containing the JSON data
    with open(f'rule-IS_OTC_DRUG.json', 'r') as f:
        # Load the JSON data from the file
        rules = json.load(f)

    prompt1 = f"Rules: {json.dumps(rules)}"
    prompt2 = """ 
        Instructions:

        1. **Test Case Objective**: Clearly indicate whether the generated test data should match:

        ### Parameter: "match"
        - **Only a specific rule** (`"match": "only_specific_rule"`): The test data must meet the criteria of exactly one rule while failing to meet the criteria for all other rules in the set. Ensure that, when the match type is specified as 'only_specific_rule', you generate at least one test case for each rule listed in the `rules[]` array, so that every rule is individually tested against the provided input data.
        - **Multiple rules** (`"match": "mix_rules"`): The test data must meet the criteria of multiple rules simultaneously.

        ### Parameter: "type"
        - **General Test Data** (`"type": "general"`): Continue to generate test data as before, without any specific focus on boundary conditions.
        - **Border Values Test Data** (`"type": "border_values"`): Focus on creating test cases that explore the boundary conditions of the rules. This involves looking at individual rules and, if there is a range involved, creating tests that test the border values of these ranges. This approach is particularly relevant for rules that specify numerical ranges, date ranges, or other scenarios where boundary values can be identified and tested.

        2. **Input Data Generation**:
        - Generate realistic input data relevant to the rule(s) being tested.
        - The input data should be placed within a `"request"` object for each test case.
        - Exclude any parameters named `"parameter"` from the `"request"` object, even if listed in the rule requirements.

        3. **Validation Information**:
        - Each test case object must include a `"validation"` object.
        - Within the `"validation"` object, include:
        - A `"rule_name"` field, which is an array containing the title(s) of the rule(s) the input data is intended to match. If the test data matches multiple rules, include all applicable rule titles.
        - An `"output_value"` field, indicating the expected output value of the rule(s) when evaluated against the provided test data.

        ### Example System Prompt:

        ```plaintext
        Generate test data for evaluating specific logic rules related to product classification. The test data should be structured in a JSON object array named `tests[]`, with each object representing a distinct test case. Ensure the test data is designed to either match a single rule or multiple rules as specified. Include realistic input data within a `"request"` object for each test case, and provide validation details in a `"validation"` object, specifying the rule(s) the test data is designed to match and the expected output value(s).
        ```

        ### Example Output Structure:

        ```json
        {
            "tests": [
                {
                "request": {
                    "intended_use": "Example Use",
                    "product_name": "Example Product",
                    "item_type": "Example Type",
                    "active_ingredient": "Example Ingredient"
                },
                "validation": {
                    "rule_name": ["Example Rule Title"],
                    "output_value": true/false
                }
            }
        ]
    }
    ```
    IMPORTANT: When outputting the test data, make sure to return only the json object and nothing else.
    """

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that takes rule data from json file and creates test data in structured json format."},
            {"role": "user", "content": prompt1},
            {"role": "user", "content": prompt2}
        ]
    )

    # Use the formatted timestamp in the filename
    with open(f"{rule}-testData-{timestamp}.json", 'w') as f:
    # with open(f"{rule}-testData-{datetime.now()}.json", 'w') as f:
        f.write(completion.choices[0].message.content)

    print(completion.choices[0].message.content)


