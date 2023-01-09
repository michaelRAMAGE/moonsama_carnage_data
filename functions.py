def get_and_load_dictionary(input):
    import requests, json
    return json.loads(requests.get(input).text)

def sama_counter(week):
    from inputs import raw_gganbu_array, raw_result_array
    week_index = week - 17
    gganbu_dictionary = get_and_load_dictionary(raw_gganbu_array[week_index])
    result_dictionary = get_and_load_dictionary(raw_result_array[week_index])
    moonsama_count = 0
    exosama_count = 0
    gromlinvip_count = 0
    for player in result_dictionary.keys():
        if result_dictionary.get(player).get("stone")*5%1 == 0:
            gromlinvip_count = gromlinvip_count + 1
        elif result_dictionary.get(player).get("stone") >= gganbu_dictionary.get("stone")*10 and result_dictionary.get(player).get("wood") >= gganbu_dictionary.get("wood")*10 and result_dictionary.get(player).get("iron") >= gganbu_dictionary.get("iron")*10 and result_dictionary.get(player).get("gold") >= gganbu_dictionary.get("gold")*10:
            moonsama_count = moonsama_count + 1
        else:
            exosama_count = exosama_count + 1
    return moonsama_count, exosama_count, gromlinvip_count

def sama_lister(week):
    from inputs import raw_gganbu_array, raw_result_array
    week_index = week - 17
    gganbu_dictionary = get_and_load_dictionary(raw_gganbu_array[week_index])
    result_dictionary = get_and_load_dictionary(raw_result_array[week_index])
    player_list = []
    for player in result_dictionary.keys():
        player_list.append(player)
    return player_list

def attendance_counter(first_week, last_week):
    attendance_log = []
    for week in range(first_week, last_week+1):
        for player in sama_lister(week):
            attendance_log.append(player)
    attendance_log.sort()
    attendance_name = []
    attendance_number = []
    attendance_final = []
    for player in attendance_log:
        if attendance_name.count(player) == 0:
            attendance_name.append(player)
            attendance_number.append(attendance_log.count(player))
    for names in range (0, len(attendance_number)):
        pair = (attendance_number[names], attendance_name[names])
        attendance_final.append(pair)
    attendance_final.sort()
    attendance_final.reverse()
    return attendance_final
