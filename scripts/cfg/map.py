# Mapping of platform and campaign data for classification and changes
MAP = {
    "platforms": [
        {
            # Column to check
            "check_col": "platform",
            # Values to search for in the column
            "search_values": ["Platform_A", "Platform_B", "Unknown"],
            # Changes to apply if condition is met
            "apply_changes": {"platform": "Platform_X"},
        }
    ],
    "ad_types": [
        {
            # Column to check
            "check_col": "ad_type",
            # Values to search for in the column
            "search_values": ["Ad_Type_1", "Ad_Type_2"],
            # Changes to apply
            "apply_changes": {"channel": "NBC"},
        },
        {
            "check_col": "ad_type",
            "search_values": ["Ad_Type_3"],
            "apply_changes": {"platform": "Platform_B"},
        },
    ],
}
"""
MAP is a dictionary used for mapping and classifying platform, ad type, and campaign data.
- It allows changes to be applied based on specific column values for better categorization.
- Each entry has:
    - `check_col`: the column to be checked in the data.
    - `search_values`: the list of values to search for in the `check_col`.
    - `apply_changes`: the changes to apply when a match is found.
    
Example usage:
    - If the platform is "Platform_X", apply the changes specified (e.g., setting the platform to "Platform_A").
    - If the ad type is "Ad_Type_1", change the channel to "NBC".
    - If the campaign objective is "Objective_1", change it to "Goal_1".

This structure is highly flexible for any use case where you need to classify and update data based on conditional mappings.
"""
