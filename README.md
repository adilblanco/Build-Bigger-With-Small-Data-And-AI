# Build-Bigger-With-Small-Data-And-AI

Conference : https://www.youtube.com/watch?v=P-55pV6ss3k&t=876s     
Ollama : https://github.com/ollama/ollama       
Python : https://github.com/ollama/ollama-python        
Docker : https://hub.docker.com/r/ollama/ollama     

```bash
# Start the Docker container
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# Pull the LLaMA model
docker exec -it ollama ollama pull llama3.2

# List available models
docker exec -it ollama ollama list
```
