# Import necessary libraries
import discord
import os
import logging
import sys

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Define intents
intents = discord.Intents.default()
intents.members = True  # Enable the members intent to receive member join events
intents.guilds = True # Enable guild intents to access guild information (roles, etc.)

# Create a Discord client instance with the specified intents
client = discord.Client(intents=intents)

# Event handler for when the bot is ready and connected to Discord
@client.event
async def on_ready():
    """Prints a message to the console when the bot is connected."""
    logger.info(f'{client.user} has connected to Discord!')

# Event handler for when a new member joins a server
@client.event
async def on_member_join(member):
    """Handles the event when a new member joins a server."""
    logger.info(f"New member joined: {member.name}")

    # Retrieve role name from environment variable
    role_name = os.getenv("ROLE_NAME")
    if not role_name:
        logger.error("ROLE_NAME environment variable not set.")
        return

    # Find the role in the server
    # discord.utils.get returns the first role that matches the name or None if not found
    role = discord.utils.get(member.guild.roles, name=role_name)

    if role:
        try:
            # Assign the role to the new member
            await member.add_roles(role)
            logger.info(f"Assigned role '{role_name}' to {member.name}")
        except discord.Forbidden:
            logger.error(f"Bot does not have permission to assign the role '{role_name}' to {member.name}.")
        except discord.HTTPException as e:
            logger.error(f"Failed to assign role '{role_name}' to {member.name}. HTTPException: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred while assigning role '{role_name}' to {member.name}: {e}")
    else:
        logger.error(f"Role '{role_name}' not found in server {member.guild.name}.")

# Main part of the script
if __name__ == "__main__":
    # Retrieve bot token from environment variable
    bot_token = os.getenv("BOT_TOKEN")

    if not bot_token:
        logger.error("BOT_TOKEN environment variable not set.")
        # It's better to exit if the token is not available, as the bot cannot run.
        exit("BOT_TOKEN environment variable is required to run the bot.")
    
    if not os.getenv("ROLE_NAME"):
        # Warn if ROLE_NAME is not set, as on_member_join will fail to find a role.
        logger.warning("ROLE_NAME environment variable not set. The bot will not be able to assign roles.")


    try:
        # Run the bot with the token
        client.run(bot_token)
    except discord.LoginFailure:
        logger.error("Invalid bot token. Please check your BOT_TOKEN environment variable.")
    except Exception as e:
        logger.error(f"An unexpected error occurred while trying to run the bot: {e}")
