# Chat bot configuration soon to add docker details once i figure out a few more things.

# Configure

Create a `.env` file from the environment template file `env.example`

## LLM Configuration
MacOS and Linux users can use any LLM that's available via Ollama. Check the "tags" section under the model page you want to use on https://ollama.ai/library and write the tag for the value of the environment variable `LLM=` in th e`.env` file.
All platforms can use GPT-3.5-turbo and GPT-4 (bring your own API keys for OpenAIs models).

# Applications
## App 1 - Support Agent Bot

UI: http://localhost:8501
DB client: http://localhost:7474
