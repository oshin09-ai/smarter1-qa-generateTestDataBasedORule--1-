Pre-requisite: 
install openai: pip install openai
insert openai.api_key in openAiGenerateTestDataBasedOnRule.py file from: https://platform.openai.com/api-keys
run main.py file

Expected steps:
1. send GET request to get the rule for specific classification
2. save the rule in json file ex: "rule-IS_OTC_GRUG.json"
3. use open AI prompts with rules and other instructions to generate test data based on rules 
4. save response in jason file ex. "test_output+2024-02-14 20:00:45.988435.json"
