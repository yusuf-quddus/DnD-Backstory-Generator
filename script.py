import openai
openai.api_key = '<api key>'
model_id = 'gpt-3.5-turbo'

def backstory_gpt(player_race="Human", player_class="fighter"):
    message = "Make a dnd character backstory for a " + player_race + " " + player_class
    response = openai.ChatCompletion.create(
    model = model_id,
    messages = [{
        "role": 'user',
        "content": message
    }]
    )
    return response.choices[0].message.content

print('\n')
input_race = input("Input PC race: ")
input_class = input("Input PC class: ")
print('\n\n')

print(backstory_gpt(input_race, input_class) + '\n')
