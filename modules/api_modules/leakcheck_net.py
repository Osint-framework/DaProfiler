from leakcheck import InvalidParamsException, LeakCheckAPI

def leak_check_api(mail):
    full_results = []
    api = LeakCheckAPI()
    # GET YOUR KEY AT https://leakcheck.net/ 
    try:
        api.set_key("YOUR_KEY")
        api.set_type("email")
        api.set_query(mail)
        result = api.lookup(with_sources=1)[0:10]
        for i in result:
            try:
                password  = i['line']
            except IndexError:
                password = None
            try:
                leak_name = i['sources']
            except IndexError:
                leak_name = None
            try:
                leak_date = i['last_breach']
            except IndexError:
                leak_date = None
            dict_res = {
                'password':password,
                'leak_name':leak_name,
                'leak_date':leak_date
            }
            full_results.append(dict_res)
        if len(full_results) == 0:
            return None
        return full_results
    except InvalidParamsException:
        return None

# By Lui#6166 from Prism Intelligence Group
