import requests
import json
from openAiGenerateTestDataBasedOnRule import generate_test_data_based_on_rule_and_write_to_a_file
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

openai_api_key = os.getenv("openai_api_key")
CLASSIFICATION_BASE_URL = os.getenv("CLASSIFICATION_BASE_URL")
AUTHORIZATION = os.getenv("AUTHORIZATION")


rule = "IS_OTC_DRUG"

def main():
    # not needed for now but will be used when we have more than IS_OTC_DRUG rule
    # def get_all_classifications():
    #     all_cs_res = requests.get(url=CLASSIFICATION_BASE_URL, headers=AUTHORIZATION)
    #     print(all_cs_res.status_code)
    #     # assert all_cs_response.status_code == 200  # Assuming 200 is the success status code
    #     res = all_cs_res.json()
    #     print(res)
    # get_all_classifications()

    # def get_classification():
    #     cs_res = requests.get(url=f'{CLASSIFICATION_BASE_URL}/{rule}', headers=AUTHORIZATION)
    #     print(cs_res.status_code)
    #     # assert all_cs_response.status_code == 200  # Assuming 200 is the success status code
    #     res = cs_res.json()
    #     print(res)
    #     with open(f"rule-IS_OTC_DRUG.json", "w") as f:
    #         json.dump(res, f)
           
    def get_classification():
    # Construct the headers dictionary using the token
        headers = {"Authorization": f"Bearer {AUTHORIZATION}"}
        cs_res = requests.get(url=f'{CLASSIFICATION_BASE_URL}/{rule}', headers=headers)
        print(cs_res.status_code)
        res = cs_res.json()
        print(res)
        with open(f"rule-IS_OTC_DRUG.json", "w") as f:
            json.dump(res, f)


    get_classification()

    generate_test_data_based_on_rule_and_write_to_a_file(rule)


if __name__ == '__main__':
    main()
