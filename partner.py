class Agent:
    agents = {}
    agent_id = 1
    def __init__(self, name, phone):
        self.agent_id = Agent.agent_id
        Agent.agent_id+=1
        self.name = name
        self.phone = phone
        self.status = "Available"