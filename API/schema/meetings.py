def individual_serial(meeting)->dict:
    return {
        "id":str(meeting["_id"]),
        "date_heure":meeting["date_heure"],
        "latitude":meeting["latitude"],
        "longitude":meeting["longitude"],
        "nb_participants":meeting["nb_participants"],
    }

def list_serial(meetings)->list:
    return [individual_serial(meeting) for meeting in meetings]