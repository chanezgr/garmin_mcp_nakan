"""
Activity Management functions for Garmin Connect MCP Server
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
    """Register all activity management tools with the MCP server app"""
    
    @app.tool()
    async def get_activities_by_date(start_date: str, end_date: str, activity_type: str = ""):
        """Get activities data between specified dates, optionally filtered by activity type
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            activity_type: Optional activity type filter (e.g., cycling, running, swimming)
        """
        try:
            activities = garmin_client.get_activities_by_date(start_date, end_date, activity_type)
            if not activities:
                return f"No activities found between {start_date} and {end_date}" + \
                       (f" for activity type '{activity_type}'" if activity_type else "")
            
            return activities
        except Exception as e:
            return f"Error retrieving activities by date: {str(e)}"

    @app.tool()
    async def get_activities_fordate(date: str):
        """Get activities for a specific date
        
        Args:
            date: Date in YYYY-MM-DD format
        """
        try:
            activities = garmin_client.get_activities_fordate(date)
            if not activities:
                return f"No activities found for {date}"
            
            return activities
        except Exception as e:
            return f"Error retrieving activities for date: {str(e)}"

    @app.tool()
    async def get_activity(activity_id: int):
        """Get basic activity information
        
        Args:
            activity_id: ID of the activity to retrieve
        """
        try:
            activity = garmin_client.get_activity(activity_id)
            if not activity:
                return f"No activity found with ID {activity_id}"
            
            return activity
        except Exception as e:
            return f"Error retrieving activity: {str(e)}"

    @app.tool()
    async def get_activity_splits(activity_id: int):
        """Get splits for an activity
        
        Args:
            activity_id: ID of the activity to retrieve splits for
        """
        try:
            splits = garmin_client.get_activity_splits(activity_id)
            if not splits:
                return f"No splits found for activity with ID {activity_id}"
            
            return splits
        except Exception as e:
            return f"Error retrieving activity splits: {str(e)}"

    @app.tool()
    async def get_activity_typed_splits(activity_id: int):
        """Get typed splits for an activity
        
        Args:
            activity_id: ID of the activity to retrieve typed splits for
        """
        try:
            typed_splits = garmin_client.get_activity_typed_splits(activity_id)
            if not typed_splits:
                return f"No typed splits found for activity with ID {activity_id}"
            
            return typed_splits
        except Exception as e:
            return f"Error retrieving activity typed splits: {str(e)}"

    @app.tool()
    async def get_activity_split_summaries(activity_id: int):
        """Get split summaries for an activity
        
        Args:
            activity_id: ID of the activity to retrieve split summaries for
        """
        try:
            split_summaries = garmin_client.get_activity_split_summaries(activity_id)
            if not split_summaries:
                return f"No split summaries found for activity with ID {activity_id}"
            
            return split_summaries
        except Exception as e:
            return f"Error retrieving activity split summaries: {str(e)}"

    @app.tool()
    async def get_activity_weather(activity_id: int):
        """Get weather data for an activity
        
        Args:
            activity_id: ID of the activity to retrieve weather data for
        """
        try:
            weather = garmin_client.get_activity_weather(activity_id)
            if not weather:
                return f"No weather data found for activity with ID {activity_id}"
            
            return weather
        except Exception as e:
            return f"Error retrieving activity weather data: {str(e)}"

    @app.tool()
    async def get_activity_hr_in_timezones(activity_id: int):
        """Get heart rate data in different time zones for an activity
        
        Args:
            activity_id: ID of the activity to retrieve heart rate time zone data for
        """
        try:
            hr_zones = garmin_client.get_activity_hr_in_timezones(activity_id)
            if not hr_zones:
                return f"No heart rate time zone data found for activity with ID {activity_id}"
            
            return hr_zones
        except Exception as e:
            return f"Error retrieving activity heart rate time zone data: {str(e)}"

    @app.tool()
    async def get_activity_gear(activity_id: int):
        """Get gear data used for an activity
        
        Args:
            activity_id: ID of the activity to retrieve gear data for
        """
        try:
            gear = garmin_client.get_activity_gear(activity_id)
            if not gear:
                return f"No gear data found for activity with ID {activity_id}"
            
            return gear
        except Exception as e:
            return f"Error retrieving activity gear data: {str(e)}"

    @app.tool()
    async def get_activity_exercise_sets(activity_id: int):
        """Get exercise sets for strength training activities
        
        Args:
            activity_id: ID of the activity to retrieve exercise sets for
        """
        try:
            exercise_sets = garmin_client.get_activity_exercise_sets(activity_id)
            if not exercise_sets:
                return f"No exercise sets found for activity with ID {activity_id}"
            
            return exercise_sets
        except Exception as e:
            return f"Error retrieving activity exercise sets: {str(e)}"

    return app
