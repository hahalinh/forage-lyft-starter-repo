def calculate_duration(current_date, last_service_date):
        # Get the interval between two dates
        duration  = current_date - last_service_date
        duration_in_seconds = duration.total_seconds()      
        years = divmod(duration_in_seconds, 31536000)[0]    
        return years 