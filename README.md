# ai-agent-travel-agent

Run travel agent in the terminal: $ adk run travel_planner_agent

Enter text at the prompt [user]:

To exit the travel agent: [user] exit

Run travel agent with web interface: $ adk web --port 8000

navigate to: [http://localhost:8000](http://localhost:8000)

Start Airbnb MCP server in a separate terminal: $ npx -y @openbnb/mcp-server-airbnb@0.1.2 --ignore-robots-txt

## create agent steps 

Override existing content? [y/N]: y
Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models (fill later)
Choose model (1, 2): 1

Choose model (1, 2): 1
1. Google AI
2. Vertex AI
3. Login with Google
Choose a backend (1, 2, 3): 1

Choose a backend (1, 2, 3): 1

Don't have API Key? Create one in AI Studio: https://aistudio.google.com/apikey

Enter Google API key:    

## Pre-reqs:

Verify python: $ python --version

Create virtual env: $ python3 -m venv .venv

Activate virtual env: $ source .venv/bin/activate

Install dependencies: $ pip install --upgrade pip
$ pip install requests

Install google-adk: $pip install google-adk

Help guide: [https://renukas-organization-2.gitbook.io/create-your-first-agent-travel-agent/create-your-first-ai-travel-planner-using-multi-agents/create-the-travel-agent](https://renukas-organization-2.gitbook.io/create-your-first-agent-travel-agent/create-your-first-ai-travel-planner-using-multi-agents/create-the-travel-agent)