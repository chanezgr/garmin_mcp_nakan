FROM python:3.12-slim

# Configure l'environnement
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080
    
WORKDIR /app

# Copie les fichiers de configuration et d'installation
COPY setup.py requirements.txt ./

# Installe les dépendances en une seule étape
RUN pip install --no-cache-dir -r requirements.txt

# Copie les fichiers nécessaires
COPY run.py ./
COPY src ./src
RUN pip install --no-cache-dir -e .

# Expose le port MCP
EXPOSE 8080

# Commande par défaut : exécute le script d'entrée
CMD ["python", "run.py"]