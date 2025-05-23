# ADK Geo Frontend

Goal:
This project provides a one-command-launch frontend for exploring geospatial data using ADK agents. It’s built for anyone – from curious beginners to researchers – who wants a simple, interactive UI (map + chat + info) without having to set up a full stack from scratch.

Framework:

    Frontend: Streamlit (Map + Chat + Info Panel)

    Backend: FastAPI serving an ADK agent

    Deployment: Docker Compose (no local setup needed)

Just clone the repo, run one command, and start exploring geospatial datasets using natural language.


# Goal 1: One-Command Launchable UI for Geo Agents

Build a Dockerized, zero-install setup that spins up a complete UI to explore geospatial datasets using ADK agents – designed for curious users with no Python or frontend experience.

Steps:

Create a Docker setup (docker-compose.yml) that runs both backend (FastAPI + ADK agent) and frontend (Streamlit app)

Provide OS-specific launch commands (Mac, Windows, Linux)

Auto-open browser at localhost:8000 with live app

Include minimal fallback error handling (e.g. Docker not installed)

Write README with exact steps, <60 seconds from clone to browser



# Goal 2: Base UI with Map, Chat, and Info Panel

Build a minimal Streamlit interface for interacting with a geospatial ADK agent. The UI should feel like a stripped-down Earth Engine console with chat.

Steps:

Add Leaflet or equivalent as map base layer

Add right-side chat panel wired to Gemini via ADK

Add info panel to display hyperparameters or metadata

Hook up backend to a prebuilt ADK agent that:

Searches GEE dataset catalog

Answers simple queries like “Where was this data collected?”

Include example prompt buttons for first-time users (e.g., “Show datasets on deforestation”)



# Goal 3: Modular Kit for Developers and Researchers

Design the codebase to support developers building on top and researchers customizing workflows. Separate concerns and provide clean extensibility points.

Steps:

Expose config and component stubs for:

Map layers

Agent selection

Data rendering logic

Document architecture (Streamlit ↔ FastAPI ↔ ADK agent)

Add hooks for plugging in custom agents or new data sources

Offer three usage profiles:

A: Play mode (non-coders, just click and explore)

B: Developer mode (override agents, add routes)

C: Researcher mode (modify workflows, evaluate outputs)

Write examples of modifying chat prompts, adding visualizations
