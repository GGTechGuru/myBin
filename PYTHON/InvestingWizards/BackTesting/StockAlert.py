import fix_yahoo_finance as yf  
import datetime

def recent_quote(sym):
    start_date = datetime.datetime.today() - datetime.timedelta(days=1000)
    start_date = start_date.strftime('%Y-%m-%d')
    
    end_date = datetime.datetime.today().strftime('%Y-%m-%d')
    data = yf.download(sym, start_date, end_date)
    
    # print data.tail()

    print( data )

    l = data["Close"].tolist()
    return l[-1]
    

##########################

print ("USO:" , recent_quote("USO"))

# print ("IBM:" , recent_quote("IBM"))
# print ("GOOG:" , recent_quote("GOOG"))
