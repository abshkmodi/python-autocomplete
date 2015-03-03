import redis

r = redis.Redis()

def initialise(filename):
	file =open(filename,"r")

	for i,line in enumerate(file):
		line=line.strip()
		r.hset("data",i,line)
		tokens = line.split()
		for token in tokens:
			token=token.lower()
			for j in range(0,len(token)):
				r.zadd("index:%s" % token[0:j+1],i,0)

def autocomplete (query):
	
	query=query.strip()
	tokens=query.split()
	
	for i,token in enumerate(tokens):
		token=token.lower()
		token="index:%s" % token
		tokens[i]=token
		
	r.zinterstore("cache:%s" % query,tokens)
	r.expire("cache:%s" % query,30)
	
	data=[]
	for i in r.zrange ("cache:%s" % query, 0, -1):
		data.append(r.hget("data",i))
		
	return data
