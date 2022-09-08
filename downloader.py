import urllib.request, json 

def get(tick="SPY"):
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/"+ tick +"?region=US&lang=en-US&includePrePost=false&interval=1d&useYfid=true&range=20y"

        with urllib.request.urlopen(url) as url2:
            data = json.load(url2)
            #parse array 
            res = data['chart']['result'][0]['indicators']['quote'][0]   #open close low high volme
            res.update(data['chart']['result'][0]) # add timestamp

            return res
    except:
        print('Opss .. Error downloading data')


def download(tick="SPY"):
    url = "https://query1.finance.yahoo.com/v8/finance/chart/"+ tick +"?region=US&lang=en-US&includePrePost=false&interval=1d&useYfid=true&range=20y"
    data=''
    with urllib.request.urlopen(url) as url2:
        data = json.load(url2)

    with open('data/'+ tick + '.json', 'w') as f:
        json.dump(data, f)


def get_local(tick="SPY"):
    
        with open('data/'+ tick + '.json', 'r') as f:
            data = json.load(f)

            #parse array 
            res = data['chart']['result'][0]['indicators']['quote'][0]   #open close low high volme
            res.update(data['chart']['result'][0]) # add timestamp

            return res

# This class is to be exported as PathLike from os,
# but we define it here as _PathLike to avoid import cycle issues.
# See https://github.com/python/typeshed/pull/991#issuecomment-288160993
def get2(tick="SP",online_priority=1):
    

    if online_priority:
        try:
            download(tick)
        except:
            try:
                r = get_local(tick)
                return r
            except IOError:
                print("cannot download latest data and also cannot get from local copy")
                
        else:
            return get_local(tick)

    else: #ofline priority
        try:
            r = get_local(tick)
            return r
        except IOError:
            try:
                download(tick)
                r = get_local(tick)
                return r
            except:
                print("cannot get from local copy and also cannot download latest data")
                