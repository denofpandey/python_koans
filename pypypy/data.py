data =[dict(number=x) for x in '019234']
data.sort(key=lambda x: float(x['number']))
