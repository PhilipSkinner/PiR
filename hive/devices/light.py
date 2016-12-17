class HiveLight:
    id = None
    name = None    
    brightness = None
    state = None

    def __init__(self, node):
        if 'name' in node:
            self.name = node['name']
        
        if 'id' in node:
            self.id = node['id']

        if 'attributes' in node:
            attr = node['attributes']

            if 'brightness' in attr:
                self.brightness = attr['brightness']['reportedValue']

            if 'state' in attr:
                self.state = attr['state']['reportedValue']