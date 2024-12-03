## Puffo Backend

This demo project, designed for learning purposes, allows users to mix and match various elements. Leveraging generative AI, it creates new characters by blending these elements. [See API Document](http://localhost:8000/docs)

## Local Development

### Set up virtual environment

- Create a virtual environment
```bash
python -m venv venv
```

- Activate the virtual environment
```bash
source venv/bin/activate
```

- Install dependencies
```bash
pip install requirements.txt
```

### Run Development Mode
```bash
fastapi dev ./app/main.py --port 8000
```


## Docker Compose Development
> **Note:** coming soon

## Progress
- [x] Connect to OpenAI (Basic)
- [ ] Cache generated result