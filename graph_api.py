import facebook
import json

token = {''}
graph = facebook.GraphAPI(token)

def main():
    fields = ['id','name']
    get_field(fields)
    fields=['friends']
    get_field(fields)
    fields=['age_range']
    get_field(fields)
    fields=['birthday']
    get_field(fields)
    fields=['gender']
    get_field(fields)
    
def get_field(fields):
    id='me'
    profile = json.dumps(graph.get_object(id,fields=fields),indent=4)
    print(f'{profile}\n')


if __name__ == "__main__":
    main()