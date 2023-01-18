import csv
import openai

# Use the API key provided in the openai API documentation
openai.api_key = ""

# Set the model
model_engine = "text-davinci-003"

# Read the input CSV file
with open("prompts.csv", "r") as file:
    reader = csv.reader(file)
    # Open the output CSV file
    with open("output.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            prompt = row[0]
            # Make the API request
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.7,
            )
            # Write the prompt and response to the output CSV file
            response = completion.choices[0]["text"]
            response = completion.choices[0].get("text", "").replace("\n", "")
            print(response)
            writer.writerow([response])

