def calculate_duration(current_date, last_service_date, length_to_check):
        date_to_start_service = current_date.replace(year= current_date.year - length_to_check)  
        return last_service_date <= date_to_start_service