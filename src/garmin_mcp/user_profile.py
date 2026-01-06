"""
User Profile functions for Garmin Connect MCP Server
"""
import datetime
from typing import Any, Dict, List, Optional, Union

# The garmin_client will be set by the main file
garmin_client = None


def configure(client):
    """Configure the module with the Garmin client instance"""
    global garmin_client
    garmin_client = client


def register_tools(app):
    """Register all user profile tools with the MCP server app"""
    
    @app.tool()
    async def get_full_name():
        """Get user's full name from profile"""
        try:
            full_name = garmin_client.get_full_name()
            return full_name
        except Exception as e:
            return f"Error retrieving user's full name: {str(e)}"

    @app.tool()
    async def get_unit_system():
        """Get user's preferred unit system from profile"""
        try:
            unit_system = garmin_client.get_unit_system()
            return unit_system
        except Exception as e:
            return f"Error retrieving unit system: {str(e)}"
    
    @app.tool()
    async def get_user_profile():
        """Get user profile information"""
        try:
            profile = garmin_client.get_user_profile()
            if not profile:
                return "No user profile information found."
            return profile
        except Exception as e:
            return f"Error retrieving user profile: {str(e)}"

    @app.tool()
    async def get_userprofile_settings():
        """Get user profile settings"""
        try:
            settings = garmin_client.get_userprofile_settings()
            if not settings:
                return "No user profile settings found."
            return settings
        except Exception as e:
            return f"Error retrieving user profile settings: {str(e)}"

    return app