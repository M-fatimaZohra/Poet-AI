import asyncio
from agents import Runner
from my_agents.poet import poet




poetAI_history = []
while True:
    input_prompt = input("Enter the initial prompt for the Poet AI: ")
    if input_prompt.lower() == "":
          
          break
    poetAI_history.append({"role": "user", "content": input_prompt })
    async def main():
            result = await Runner.run(poet, poetAI_history)
            print(result.final_output)
            poetAI_history.append({"role": "assistant", "content": result.final_output})


    asyncio.run(main()) 
     