import requests

class Partner:
    def get_street_liquidity(name, month=6):
        try:
            url = 'http://127.0.0.1:5000/api/liquidity/street?name={}&month={}'.format(name,month)        
            response = requests.get(url)                    
            return response.json() 
        except Exception as ex:
            error = "Partner Service - get_street_liquidity error: {} \n".format(ex)
            raise Exception(error)  

    def get_all_street_liquidity(month=6):
        try:
            url = 'http://127.0.0.1:5000/api/liquidity/street/all?month={}'.format(month)        
            response = requests.get(url)                    
            return response.json() 
        except Exception as ex:
            error = "Partner Service - get_all_street_liquidity error: {} \n".format(ex)
            raise Exception(error)                      

    def get_district_liquidity(name, month=6):
        try:
            url = 'http://127.0.0.1:5000/api/liquidity/district?name={}&month={}'.format(name,month)        
            response = requests.get(url)                    
            return response.json() 
        except Exception as ex:
            error = "Partner Service - get_district_liquidity error: {} \n".format(ex)
            raise Exception(error)  

    def get_all_district_liquidity(month=6):
        try:
            url = 'http://127.0.0.1:5000/api/liquidity/district/all?month={}'.format(month)        
            response = requests.get(url)                    
            return response.json() 
        except Exception as ex:
            error = "Partner Service - get_all_district_liquidity error: {} \n".format(ex)
            raise Exception(error)      

    def get_region_liquidity(name, month=6):
        try:
            url = 'http://127.0.0.1:5000/api/liquidity/region?name={}&month={}'.format(name,month)        
            response = requests.get(url)                    
            return response.json() 
        except Exception as ex:
            error = "Partner Service - get_region_liquidity error: {} \n".format(ex)
            raise Exception(error)  

    def get_all_region_liquidity(month=6):
        try:
            url = 'http://127.0.0.1:5000/api/liquidity/region/all?month={}'.format(month)        
            response = requests.get(url)
            
            return response.json() 
        except Exception as ex:
            error = "Partner Service - get_all_region_liquidity error: {} \n".format(ex)
            raise Exception(error)     