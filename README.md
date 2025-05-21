# Discord Role Assignment Bot

This bot automatically assigns a specified role to new members when they join a Discord server.

## Overview

This bot is written in Python and packaged as a Docker container. It listens for new member join events and assigns them a pre-configured role. Configuration is handled via environment variables.

## Configuration

The bot requires the following environment variables to be set:

*   `BOT_TOKEN`: Your Discord bot token. This is required for the bot to connect to Discord.
*   `ROLE_NAME`: The exact name of the role you want to assign to new members on your server.

Ensure these variables are set in the environment where the bot is run (e.g., in your Docker run command or your deployment environment).

## Running Locally with Docker

You can build and run the bot locally using Docker.

1.  **Build the Docker image:**
    Open your terminal in the project's root directory (where the `Dockerfile` is located) and run:
    ```bash
    docker build -t discord-role-bot .
    ```

2.  **Run the Docker container:**
    Replace `"YOUR_BOT_TOKEN"` and `"YourRoleName"` with your actual bot token and desired role name.
    ```bash
    docker run -d --env BOT_TOKEN="YOUR_BOT_TOKEN" --env ROLE_NAME="YourRoleName" --name discord-bot discord-role-bot
    ```
    The `-d` flag runs the container in detached mode.

## Automated Publishing to GitHub Container Registry (GHCR)

This project uses GitHub Actions to automatically build and publish the Docker image to the GitHub Container Registry (GHCR) whenever changes are pushed to the `main` branch.

The image is tagged with the commit SHA and `latest`.

## Running from GitHub Container Registry

You can pull and run the latest image directly from GHCR.

1.  **Pull the image:**
    Replace `<OWNER>` with the GitHub username or organization that owns this repository.
    ```bash
    docker pull ghcr.io/<OWNER>/discord-role-bot:latest
    ```

2.  **Run the container:**
    Replace `<OWNER>`, `"YOUR_BOT_TOKEN"`, and `"YourRoleName"` accordingly.
    ```bash
    docker run -d --env BOT_TOKEN="YOUR_BOT_TOKEN" --env ROLE_NAME="YourRoleName" --name discord-bot ghcr.io/<OWNER>/discord-role-bot:latest
    ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
