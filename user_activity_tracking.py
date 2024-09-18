class UserActivityTracker:
    def __init__(self):
        self.activity_log = {}
    
    def log_activity(self, user_id, activity_type, details):
        """
        Logs the user's activities, such as editing or creating a recipe.
        """
        timestamp = time.time()
        log_entry = {
            'activity_type': activity_type,
            'details': details,
            'timestamp': timestamp
        }
        
        if user_id in self.activity_log:
            self.activity_log[user_id].append(log_entry)
        else:
            self.activity_log[user_id] = [log_entry]
    
    def get_user_activity(self, user_id):
        return self.activity_log.get(user_id, [])

class PrivacySettings:
    def __init__(self):
        self.privacy_settings = {}

    def set_privacy(self, user_id, privacy_level):
        """
        Adjust the privacy level of user data (e.g., public, friends-only, private).
        """
        self.privacy_settings[user_id] = privacy_level
    
    def get_privacy(self, user_id):
        return self.privacy_settings.get(user_id, 'public')
